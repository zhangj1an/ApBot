import os
import sys
import re
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.load_string_from_file import load_string_from_file, load_string_from_files
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code

from simulated.utils.task.derive_variable_definition import analyze_continuous_sequence, analyze_discrete_sequence

from simulated.utils.task.propose_world_model_agnostic_to_command import check_input_string_compatibility, check_simulator_validity_of_meta_actions, check_action_effect_conditions

def calibrate_current_value(gpt_model_type,calibration_prompt_filepath, variable_name, debug_record, define_variable_task_prompt_filepath, template_code_filepaths, generated_code_filepaths, current_action, before_action_state, goal_state_string, feedback, analyse_feedback_prompt_filepath, correct_world_model_prompt_filepath, updated_variables_filepath, updated_world_model_filepath, revert_back_later = True, verbose = False):
    # debug record: 
    
    # if the debug record suggest the range is totally off, need to generate the goal, feature or llm 
    existing_variable_files = template_code_filepaths +  generated_code_filepaths # now needs to include extended simulator, so all code must be used 

    entire_code = load_string_from_files(existing_variable_files) 

    debug_record_string = ""
    for i in range(len(debug_record)):
        debug_record_string += f"step: {i}, {debug_record[i]}\n"
    print(f"debug record string: {debug_record_string}")

    analyse_feedback_prompt = load_string_from_file(analyse_feedback_prompt_filepath)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("wwwww", entire_code)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("xxxxx", variable_name)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("sssss", str(current_action))
    analyse_feedback_prompt = analyse_feedback_prompt.replace("ttttt", before_action_state)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("qqqqq", goal_state_string)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("rrrrr", str(feedback))
    analyse_feedback_prompt = analyse_feedback_prompt.replace("yyyyy", debug_record_string)

    analysis_results = ""
    # ccccc
    error_msg = ""
    valid_flag = False
    for attempt in range(3):
        model = GPT4O()
        print(f"Attempt {attempt + 1}: Trying to analyse the past debug record.")
        
        updated_analyse_feedback_prompt = f"{analyse_feedback_prompt}\n In your previous attempt, the following error occurred. {error_msg} Please avoid such errors."
        response = model.chat_with_text(updated_analyse_feedback_prompt, temperature=1, top_p=1, gpt_model_type = gpt_model_type)
        #with open("temp.txt", 'w') as f:
        #    f.write(updated_analyse_feedback_prompt)
        #print(f"Response:\n {response}")
        #exit()
        response = extract_python_code(response)
        
        try:
            #print(f"Debug Record summary: {response}")
            calibration_ns = {}
            exec(response, calibration_ns)
            variable_is_continous = calibration_ns.get('variable_is_continuous', None)
            record_sequences = calibration_ns.get('record_sequence', None)
            step_index = calibration_ns.get('step_index', None)
            first_observed_action_taken = calibration_ns.get('first_observed_action_taken', None)
            effective_action = calibration_ns.get('effective_action', None)
            updating_variable_name = calibration_ns.get('variable_name', None)

            # variable name must be existing in entire_code 
            if updating_variable_name not in entire_code:
                error_msg = f"The variable name {updating_variable_name} is not found in the existing code. Please only use variable names from our internal model code. "
                print(error_msg)
                continue
            being_affected_by_actions = (first_observed_action_taken == effective_action)
            print(f"The effective action is {effective_action}. The first observed action is {first_observed_action_taken}.")
            
            if variable_is_continous:
                piecewise, current_value = analyze_continuous_sequence(record_sequences , being_affected_by_actions, revert_back_later)
                
                if piecewise is None:
                    piecewise = "the same as previously defined"
                analysis_results = f"The variable {updating_variable_name} is ContinuousVariable with value ranges and step values to be {piecewise}. The current value is {current_value}.  "
            else:
                value_range, current_value = analyze_discrete_sequence(record_sequences, being_affected_by_actions, revert_back_later)
                analysis_results = f"The variable {updating_variable_name} is DiscreteVariable with value ranges to be {value_range}. The current value is {current_value}. "
            if len(record_sequences) < len(debug_record) - step_index:
                error_msg = f"Your previos response is as follows. {response} \nThe generated record sequence with length {len(record_sequences)} is shorter than the debug record with length { len(debug_record)}. Please generate again and do not miss feedbacks in any step."
                print(error_msg)
                continue
            print(f"Analysis results: {analysis_results}")
            valid_flag = True
            break
            # Execute generated_appliance_code in its own dictionary
        except Exception as e:
            # Print the exception message and try again
            print(f"An error occurred on attempt {attempt + 1}: {e}")
    if not valid_flag:
        print("Cannot analyse the past debug record. Returning None.")
        return False
        #exit()
    calibration_prompt = load_string_from_file(calibration_prompt_filepath)
    calibration_prompt = calibration_prompt.replace("wwwww", entire_code)
    calibration_prompt = calibration_prompt.replace("xxxxx", updating_variable_name)
    calibration_prompt = calibration_prompt.replace("sssss", str(current_action))
    calibration_prompt = calibration_prompt.replace("ttttt", before_action_state)
    calibration_prompt = calibration_prompt.replace("qqqqq", goal_state_string)
    
    #calibration_prompt = calibration_prompt.replace("yyyyy", debug_record_string)
    
    calibration_prompt = calibration_prompt.replace("ccccc", analysis_results)
    var_format = load_string_from_file(define_variable_task_prompt_filepath)
    calibration_prompt = calibration_prompt.replace("zzzzz", var_format)
    pattern = r"\$\$\$(.*)"  # Use a capturing group for the content

   
    # Use re.search with the re.DOTALL flag
    match = re.search(pattern, var_format, re.DOTALL)
    if match:
        result = match.group()  # Extract the matched text
        print(f"Located Var Format")
    else:
        result = "Sorry, the text is not available"
    calibration_prompt = calibration_prompt.replace("zzzzz", result)

    if verbose:
        print(f"Prompt: {calibration_prompt}\n\n\n")
    # Try up to 3 times to execute the generated code
    update_variable_attempt = False
    updated_variable_code = ""
    error_msg = ""
    for attempt in range(3):
        model = GPT4O()
        print(f"Attempt {attempt + 1}: Trying to update variable definition.")
        

        updated_variable_code = model.chat_with_text(calibration_prompt + "\n" + error_msg, temperature=0, top_p=1, gpt_model_type = gpt_model_type) # "o4-mini"
        updated_variable_code = extract_python_code(updated_variable_code)
        #print(f"Analysis: {response}")
        print(f"Updated Variable code: {updated_variable_code}")
        #exit()

        try:
            execution_code = load_string_from_files(template_code_filepaths+generated_code_filepaths[:2]) + updated_variable_code
            
            exec(execution_code, globals())

            # need to make sure the variables created passes synatx checker
            # firstly, the timevariable current value should be a string, the continuous variable current value should be a number.
            
            # If no exceptions, return the response code
            
            #print(f"Execution successful, returning the code : {updated_variable_code}")
            update_variable_attempt = True
            # replace the variable line 
            content = load_string_from_file("temp_generated_variable.py")
            with open("temp_generated_variable.py", 'w') as f:
                content  += "\n" + updated_variable_code
                f.write(content)
                print("Updated variable code saved to temp_generated_variable.py.")
            with open(updated_variables_filepath, 'w') as f:
                f.write(content)
               
            print(f"Successfully updated the variable definition and saved to temp_generated_variable.py.")
            break
  

        except Exception as e:
            # Print the exception message and try again
            print(f"An error occurred on attempt {attempt + 1}: {e}")
            error_msg = f"During last attempt, the generated code is: \n{updated_variable_code}\n This results in an error: {e}. Please correct the error and try again."
            #exit()
    
    if not update_variable_attempt:
        print("Cannot re-define variable. Returning None.")
        return False

    # re-generate the world model code

    validation_functions = [
        check_input_string_compatibility,
    ]

    correct_world_model_prompt = load_string_from_file(correct_world_model_prompt_filepath)
    
    previous_world_model_code = load_string_from_files(template_code_filepaths+ generated_code_filepaths) 

    correct_world_model_prompt = correct_world_model_prompt.replace("xxxxx", previous_world_model_code)
    correct_world_model_prompt = correct_world_model_prompt.replace("yyyyy", variable_name)
    correct_world_model_prompt = correct_world_model_prompt.replace("zzzzz", updated_variable_code)

    error_msg = ""

    print("generated_code filepaths: ", generated_code_filepaths)
    
    environment_code = load_string_from_files(template_code_filepaths + generated_code_filepaths)
    
    for attempt in range(3):
        model = GPT4O()
        print(f"Attempt {attempt + 1}: Trying to update world model code.")
        updated_correct_world_model_prompt = correct_world_model_prompt + "\n" + error_msg
        
        response = model.chat_with_text(updated_correct_world_model_prompt, temperature=1, top_p=1, gpt_model_type = gpt_model_type)
        response = extract_python_code(response)

        
        is_ok = True 
        for validate in validation_functions:
            is_ok, error_message = validate(response, environment_code, "")
            if not is_ok:
                print(error_message)
                error_message = error_message.replace("\n", " ")
                print("Error message: ", error_message) 
        if not is_ok:
            print("response: ", response)
            continue 
        
        if "__init__" in response:
            error_msg = f"Please do not include __init__ function in Simulator or ExtendedSimulator. Please correct the error and try again."
            continue

        try:
            #print("generated_code filepaths: ", generated_code_filepaths)
            #print("##################")
            
            execution_code = environment_code +"\n" +response

            # below line only for debug
            with open("temp.py", 'w') as f:
                f.write(execution_code)
            #exit()
            exec(execution_code, globals())

            # need to make sure the variables created passes synatx checker
            # firstly, the timevariable current value should be a string, the continuous variable current value should be a number.
            
            # If no exceptions, return the response code
            print("Execution successful, returning the code.")

            with open("temp_generated_world_model.py", 'w') as f:
                f.write(response)
                print("Updated world model code saved to temp_generated_world_model.py.")
            with open(updated_world_model_filepath, 'w') as f:
                f.write(response)
            # update world model code using the generate world model code
            return True

        except Exception as e:
            # Print the exception message and try again
            print(f"An error occurred on attempt {attempt + 1}: {e}")
            
            error_msg = f"During last attempt, the generated code is: \n{response}\n This results in an error: {e}. Please correct the error and try again."
            
    
    # If all attempts failed, return None
    print("Cannot generate updated world model. Returning None.")
    return False
    pass



def calibrate_current_value_for_variables(gpt_model_type, calibration_prompt_filepath, variable_name, debug_record, define_variable_task_prompt_filepath, template_code_filepath, generated_code_filepath, current_action, expected_feedback, analyse_feedback_prompt_filepath, update_goal_value_prompt_filepath, command_string, revert_back_later = True, verbose = False):
    # debug record: 
    
    # if the debug record suggest the range is totally off, need to generate the goal, feature or llm 
    existing_variable_files = [template_code_filepath,  generated_code_filepath] # now needs to include extended simulator, so all code must be used 

    entire_code = load_string_from_files(existing_variable_files) 

    debug_record_string = ""
    for i in range(len(debug_record)):
        debug_record_string += f"step: {i}, {debug_record[i]}\n"
    print(f"debug record string: {debug_record_string}")

    analyse_feedback_prompt = load_string_from_file(analyse_feedback_prompt_filepath)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("wwwww", entire_code)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("xxxxx", variable_name)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("sssss", str(current_action))
    analyse_feedback_prompt = analyse_feedback_prompt.replace("qqqqq", expected_feedback)
    analyse_feedback_prompt = analyse_feedback_prompt.replace("yyyyy", debug_record_string)

    analysis_results = ""
    # ccccc
    error_msg = ""
    valid_flag = False
    for attempt in range(3):
        model = GPT4O()
        print(f"Attempt {attempt + 1}: Trying to analyse the past debug record.")
        
        updated_analyse_feedback_prompt = f"{analyse_feedback_prompt}\n In your previous attempt, the following error occurred. {error_msg} Please avoid such errors."
        response = model.chat_with_text(updated_analyse_feedback_prompt, temperature=1, top_p=1, gpt_model_type= gpt_model_type)
        with open("temp.txt", 'w') as f:
            f.write(updated_analyse_feedback_prompt)
        print(f"Response:\n {response}")
        #exit()
        response = extract_python_code(response)
        
        try:
            #print(f"Debug Record summary: {response}")
            calibration_ns = {}
            exec(response, calibration_ns)
            variable_is_continous = calibration_ns.get('variable_is_continuous', None)
            record_sequences = calibration_ns.get('record_sequence', None)
            step_index = calibration_ns.get('step_index', None)
            first_observed_action_taken = calibration_ns.get('first_observed_action_taken', None)
            effective_action = calibration_ns.get('effective_action', None)
            updating_variable_name = calibration_ns.get('variable_name', None)
            being_affected_by_actions = (first_observed_action_taken == effective_action)
            print(f"The effective action is {effective_action}. The first observed action is {first_observed_action_taken}.")
            
            if variable_is_continous:
                piecewise, current_value = analyze_continuous_sequence(record_sequences , being_affected_by_actions, revert_back_later)
                
                if piecewise is None:
                    piecewise = "the same as previously defined"
                analysis_results = f"The variable {updating_variable_name} is ContinuousVariable with value ranges and step values to be {piecewise}. The current value is {current_value}.  "
            else:
                value_range, current_value = analyze_discrete_sequence(record_sequences, being_affected_by_actions, revert_back_later)
                analysis_results = f"The variable {updating_variable_name} is DiscreteVariable with value ranges to be {value_range}. The current value is {current_value}. "
            if len(record_sequences) < len(debug_record) - step_index:
                error_msg = f"Your previos response is as follows. {response} \nThe generated record sequence with length {len(record_sequences)} is shorter than the debug record with length { len(debug_record)}. Please generate again and do not miss feedbacks in any step."
                print(error_msg)
                continue
            print(f"Analysis results: {analysis_results}")
            valid_flag = True
            break
            # Execute generated_appliance_code in its own dictionary
        except Exception as e:
            # Print the exception message and try again
            print(f"An error occurred on attempt {attempt + 1}: {e}")
    if not valid_flag:
        print("Cannot analyse the past debug record. Returning None.")
        return False, "", ""
        #exit()
    calibration_prompt = load_string_from_file(calibration_prompt_filepath)
    calibration_prompt = calibration_prompt.replace("wwwww", entire_code)
    calibration_prompt = calibration_prompt.replace("xxxxx", updating_variable_name)
    
    calibration_prompt = calibration_prompt.replace("ccccc", analysis_results)
    var_format = load_string_from_file(define_variable_task_prompt_filepath)
    calibration_prompt = calibration_prompt.replace("zzzzz", var_format)
    pattern = r"\$\$\$(.*)"  # Use a capturing group for the content

   
    # Use re.search with the re.DOTALL flag
    match = re.search(pattern, var_format, re.DOTALL)
    if match:
        result = match.group()  # Extract the matched text
        print(f"Located Var Format")
    else:
        result = "Sorry, the text is not available"
    calibration_prompt = calibration_prompt.replace("zzzzz", result)

    if verbose:
        print(f"Prompt: {calibration_prompt}\n\n\n")
    # Try up to 3 times to execute the generated code
    update_variable_attempt = False
    updated_variable_code = ""
    error_msg = ""
    for attempt in range(3):
        model = GPT4O()
        print(f"Attempt {attempt + 1}: Trying to update variable definition.")
        

        updated_variable_code = model.chat_with_text(calibration_prompt + "\n" + error_msg, temperature=1, top_p=1, gpt_model_type = gpt_model_type)
        updated_variable_code = extract_python_code(updated_variable_code)
        #print(f"Analysis: {response}")
        print(f"Updated Variable code: {updated_variable_code}")
        #exit()

        try:
            execution_code = load_string_from_file(template_code_filepath) + "\n" + updated_variable_code
            exec(execution_code, globals())

            update_variable_attempt = True
            # replace the variable line 
            content = load_string_from_file("temp_generated_variable.py")
            with open("temp_generated_variable.py", 'w') as f:
                content  += "\n" + updated_variable_code
                f.write(content)
                print("Updated variable code saved to temp_generated_variable.py.")
                
            print(f"Successfully updated the variable definition and saved to temp_generated_variable.py.")
            
            #return True
            break
  

        except Exception as e:
            # Print the exception message and try again
            print(f"An error occurred on attempt {attempt + 1}: {e}")
            error_msg = f"During last attempt, the generated code is: \n{updated_variable_code}\n This results in an error: {e}. Please correct the error and try again."
    
    if not update_variable_attempt:
        print("Cannot re-define variable. Returning None.")
        return False, "", ""

    update_goal_value_prompt = load_string_from_file(update_goal_value_prompt_filepath)
    update_goal_value_prompt = update_goal_value_prompt.replace("xxxxx", load_string_from_file("temp_generated_variable.py"))
    update_goal_value_prompt = update_goal_value_prompt.replace("yyyyy", f"adjust {variable_name} so it helps achieves the task of {command_string}")
    
    variable_value = ""
    valid_flag = False 
    error_msg = ""
    for attempt in range(3):
        model = GPT4O()
        print(f"Attempt {attempt + 1}: Trying to update goal variable value.")

        response = model.chat_with_text(update_goal_value_prompt + "\n" + error_msg, temperature=1, top_p=1, gpt_model_type = gpt_model_type)
        
        response = extract_python_code(response)

        
        try:
            calibration_ns = {}
            print("the response of variable value is: ", response)
            exec(response, calibration_ns)
            variable_value = calibration_ns.get('variable_value', None)
            #print("the response of variable value is: ", response)

            entire_code = load_string_from_files([template_code_filepath, "temp_generated_variable.py"])
            exec(entire_code, calibration_ns)
            current_variable = calibration_ns.get(variable_name, None) 
            # check if current_variable is of type DiscreteVariable or ContinuousVariable
            is_discrete = (type(current_variable).__name__  == "DiscreteVariable")
            
            

            entire_code = load_string_from_files([template_code_filepath, "temp_generated_variable.py"])
            with open("temp.py", 'w') as f:
                f.write("import copy\n")
                f.write(entire_code + "\n")
                f.write(response + "\n")
                if is_discrete:
                    f.write(f"""updated_variable = copy.deepcopy({variable_name})\nupdated_variable.set_current_value("{variable_value}")""")
                else:
                    f.write(f"""updated_variable = copy.deepcopy({variable_name})\nupdated_variable.set_current_value({variable_value})""")
                
            entire_code = load_string_from_file("temp.py")
            exec(entire_code, calibration_ns)

            # return current variable and updated_variable 
            
            current_variable = calibration_ns.get(variable_name, None) 
            goal_variable = calibration_ns.get("updated_variable", None)

            return True, current_variable, goal_variable
        except Exception as e:
            print(f"An error occurred on attempt {attempt + 1}: {e}")
            #print(entire_code)
            #exit()
            error_msg = f"During last attempt, the generated code is: \n{response}\n This results in an error: {e}. Please correct the error and try again."
            continue

    return False, "", ""
