# quote astar planner 
# firstly generate the final code, then connect with astar, then generate a plan 


# can use a oracle simulator to use astar planner to generate plan first. 


import sys 
import os
import contextlib
import io
sys.path.append(os.path.expanduser("~/TextToActions/code"))
import textwrap
import re
import traceback
import warnings

from simulated.utils.load_string_from_file import load_string_from_file, load_string_from_files
from simulated.utils.extract_python_code import extract_python_code
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.create_or_replace_path import create_or_replace_path
from simulated.utils.extract_list_from_file import extract_list_from_file


# use prompt to generate the goal state in format language 
# generate a dictionary of goal states, key is the variable name, value is the target value. 
# the value range and step value must also be set explicitly. 

# format checker: all the variables in the simulator must be mentioned in the goal state. the target value must be one of the value from the variable value range. 

def format_valid_goal_state(code, feature_list, feature_sequence):

    # all the changing_variables should be in feature_list  
    #feature_variables = set(
    #    step["variable"]
    #    for feature in feature_list.values()
    #    for step in feature
    #    if "variable" in step
    #)
    feature_variables =  set(
    item["variable"]
    for feature in feature_sequence
    if feature in feature_list
    for item in feature_list[feature]
    if "variable" in item and feature != "null"
    )
    #print("feature variables: ", feature_variables)
    #exit()
    # Regex to find assignments of the form "goal_state.variable_xxx_xxx."
    feature_sequence_pattern = r"feature_sequence\s*=\s*\[.*\]"
    changing_variables_pattern = r"changing_variables\s*=\s*\[(.*)\]"
    
    if not re.search(feature_sequence_pattern, code):
        error_msg = "Error: 'feature_sequence' is not defined in the code."
        return False, error_msg
    
    # Validate and extract changing_variables
    changing_variables_match = re.search(changing_variables_pattern, code)
    if not changing_variables_match:
        error_msg = "Error: 'changing_variables' is not defined in the code."
        return False, error_msg
    
    missing_features = [feature for feature in feature_sequence if feature not in feature_list]

    if missing_features:
        error_msg =  "Error: you should only include feature names existant in the given feature list. currently, {missing_features} are non-existant features, please use the correct name."

        return False, error_msg

    # Extract changing_variables as a list
    changing_variables_str = changing_variables_match.group(1)
    changing_variables = [var.strip().strip('"').strip("'") for var in changing_variables_str.split(",")]

    redundant_variables = [var for var in changing_variables if var not in feature_variables]
    missing_variables = [var for var in feature_variables if var not in changing_variables]
    
    # Check if all changing_variables exist in the feature_list variables
    error_msg = ""
    # removing redundant variables because they might be directly set in the action effects rather than in feature list.
    #if redundant_variables:
    #    error_msg += f"Error: The following variables are not included in the feature list: {redundant_variables}. Depending on the request of the user command, you need to decide either to remove it or add the feature name into feature_sequence. \n"
    # missing variables might be implicitly mentioned in menu settings, so remove this check
    if missing_variables:
       error_msg += f"Error: The following variables are missing from the changing_variables list and should be added in: {missing_variables}\n"    
    if error_msg != "":
        return False, error_msg
    
    pattern = r"goal_state\.(variable_[a-zA-Z0-9_]+)\."
    matches = re.findall(pattern, code)

    # Get unique variable names from matches
    assigned_variables = set(matches)
    
    # Check if all changing_variables are assigned
    unassigned_variables = [var for var in changing_variables if var not in assigned_variables]
    
    if not unassigned_variables:
        print("All changing_variables are correctly assigned.")
        return True, ""
    else:
        error_msg = f"The following variables are not included in the goal specification: {unassigned_variables}"
        return False, error_msg
    
def generate_goal_state(gpt_model_type,prompt_filepath, save_goal_state_filepath,  template_code_filepaths, generated_code_filepaths, command_text, user_manual_filepath, consolidated_code_filepath, use_history = True):

    if use_history and os.path.exists(save_goal_state_filepath):
        #print(f"extracting control panel labels files available {save_goal_state_filepath}")
        return 
    model = GPT4O()
    # template_code includes: given variable, feature, action and 
    # generated_ code filepaths generated variable, feature, action. 
    prompt = load_string_from_file(prompt_filepath)
    if consolidated_code_filepath != "":
        code_content = load_string_from_files(template_code_filepaths + generated_code_filepaths + [consolidated_code_filepath]) 
    else:
        code_content = load_string_from_files(template_code_filepaths + generated_code_filepaths)
    user_manual_text = load_string_from_file(user_manual_filepath)
    
    prompt = prompt.replace("yyyyy", code_content)
    prompt = prompt.replace("zzzzz", command_text) 
    prompt = prompt.replace("xxxxx", user_manual_text)
    with open("temp_prompt.txt", "w") as f:
        f.write(prompt)
    
    error_msg = ""
    previous_response = ""
    trials = 5
    for i in range(trials):
        print("attempt: ", i)
        updated_prompt = prompt + "\n" + f"Previously, your generated code is as follows. {previous_response}\n Please make sure your code does not have the following errors: {error_msg}\n " 
        goal_state_code = model.chat_with_text(updated_prompt, temperature = 0, top_p=1, gpt_model_type= gpt_model_type)
        goal_state_code = extract_python_code(goal_state_code)

        goal_state_code = textwrap.dedent(goal_state_code)
        print("generated goal state code: ", goal_state_code)
        goal_state_code_list = goal_state_code.splitlines()
        try:
            for i in range(len(goal_state_code_list)):
                all_code = code_content + "\n" + "\n".join(goal_state_code_list[:i+1])
                with open("test.py", "w") as f:
                    f.write(all_code)
                
                with warnings.catch_warnings(record=True) as w:
                    warnings.simplefilter("always") 
                    #print(f"executing code: {goal_state_code_list[:i+1]}\n")
                    exec(all_code, globals())  # Execute the code
                    if w:
                        problematic_code = goal_state_code_list[i]
                        warning_message = w[0].message
                        error_message = f"Error occurred during execution of this code: \n{problematic_code}\n. The warning message is: {warning_message}."
                        print("code has error!!")
                        raise RuntimeError(error_message)
                
            all_code = code_content + "\n" + goal_state_code
            with open("test.py", "w") as f:
                f.write(all_code)
            stdout_capture = io.StringIO()
            stderr_capture = io.StringIO()
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                exec(all_code, globals())  # Execute the code

            # Retrieve feature_sequence from globals
            feature_sequence = globals().get('feature_sequence', None)
            changing_variables = globals().get('changing_variables', None)
            feature_list = globals().get('feature_list', None)
            # Check if feature_sequence exists and is not None
           
            if feature_sequence is None:
                raise ValueError("feature_sequence not found in the global scope.")
            
            if feature_list is None or changing_variables is None:
                raise ValueError("feature_list or changing_variables not found in the global scope.")

            # Check if all items in feature_sequence exist as keys in feature_list
            for feature in feature_sequence:
                if feature not in feature_list:
                    raise KeyError(f"Feature '{feature}' not found in feature_list.")
            valid, error_msg = format_valid_goal_state(goal_state_code, feature_list, feature_sequence)
            previous_response = goal_state_code
            print("formatting done")
            if not valid:
                error_msg = f"Your previously generated code was: \n {goal_state_code} \n" + error_msg
                raise ValueError(error_msg)
            # Write the goal state code to a file after successful execution
            create_or_replace_path(save_goal_state_filepath)
            with open(save_goal_state_filepath, "w") as f:
                f.write(goal_state_code)

            # if possible, check the feasible list all comes from feature_list
            #exit()
            break
        except KeyError as ke:
            print(f"KeyError: {ke}")
            error_msg = str(ke) + "Please remove this feature."
        
        except ValueError as ve:
            print(f"ValueError: {ve}")
            full_traceback = str(traceback.format_exc())
            error_msg = f"Error occurred during execution: {full_traceback}. This might be because your goal variable value has invalid data format."
        except RuntimeError as re:
            error_msg = str(re)
            print(f"RuntimeError: {re}")
        except AssertionError as ae:
            error_msg = str(ae)
            print(f"AssertionError: {ae}")
        except Exception as e:
            error_msg = "Error occurred during execution: "+ str(e) + ". This might be because you referred to non-existent variables or features."
            print(f"Error occurred during execution: {error_msg}. ")
        print("finishing one round of test...")
        with open("./temp.txt", "w") as f:
            f.write(all_code)
        #exit()
    


# this code is for intermediate instructions for G_R_E_, other testing environments subject to changes. 
def batch_generate_goal_state_for_G_R_E_setting(prompt_filepath, save_goal_state_dir, user_manual_dir, template_code_filepaths, generated_code_dir, command_dir):

    # all should add _0 
    user_manual_root = "/".join(user_manual_dir.split("/")[:-2])
    machine_types = os.listdir(user_manual_root)
    for machine_type in machine_types:
        # list all files if ends with txt 
        machine_ids = [f for f in os.listdir(os.path.join(user_manual_root, machine_type)) if f.endswith(".txt")]
        
        for machine_id_filename in machine_ids:
            # Washing machine: 0, 2, 3 || 1, 4
            # Rice cooker: 0, 2, 4 || 1, 3
            # Air purifier: 1, 2, 3 || 0, 4
            # Microwave: || 0, 1, 2, 3, 4
            machine_id = str(machine_id_filename.split(".")[0].split("_")[-1])

            # this file has repetitive prompt and should be modified.
            if machine_type != "_1_microwave" or machine_id != "2":
                continue

            if machine_type in [ "_6_coffee_machine"]: # "_2_washing_machine"
                continue
                
            if machine_type == "_1_microwave" and not any(s in machine_id for s in ["1","2", "3"]): # "0", "2", "3"
                continue

            if machine_type == "_2_washing_machine" and not any(s in machine_id for s in ["0", "1","2", "3", "4"]): # "0", "2", "3"
                continue
            if machine_type == "_3_rice_cooker" and not any(s in machine_id for s in ["0", "2", "4"]): 
                continue
            if machine_type == "_4_air_purifier" and not any(s in machine_id for s in ["1", "2", "3"]):
                continue

            
            user_manual_filepath = user_manual_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id)
            os.path.join(user_manual_dir, machine_type, machine_id)
            generated_code_filepath = generated_code_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id)
            command_filepath = command_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id)

            commands = extract_list_from_file(command_filepath)
            for command_info in commands:

                command_text = command_info['command']
                command_id = str(command_info['id'])
                save_goal_state_filepath = save_goal_state_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id).replace("zzzzz", "_"+command_id)

                print("processing machine type: ", machine_type, " machine id: ", machine_id, " command id: ", command_id)
                
                #if command_id != "1":
                #    continue
                generate_goal_state(prompt_filepath, save_goal_state_filepath, user_manual_filepath, template_code_filepaths, [generated_code_filepath], command_text)
                
    pass


# this code is for intermediate instructions for G_R_E_, other testing environments subject to changes. 
def batch_generate_goal_state_for_G_RE_setting(prompt_filepath, save_goal_state_dir, user_manual_dir, template_code_filepaths, generated_code_dirs, command_dir, consolidated_code_dir):

    # still need the code for the generated variable and feature files.
    # all should add _0 
    user_manual_root = "/".join(user_manual_dir.split("/")[:-2])
    machine_types = os.listdir(user_manual_root)
    for machine_type in machine_types:
        # list all files if ends with txt 
        machine_ids = [f for f in os.listdir(os.path.join(user_manual_root, machine_type)) if f.endswith(".txt")]
        
        for machine_id_filename in machine_ids:
            # Washing machine: 0, 2, 3 || 1, 4
            # Rice cooker: 0, 2, 4 || 0, 4
            # Air purifier: 1, 2, 3 || 1, 2
            # Microwave: || 0, 1, 2, 3, 4

            
            machine_id = str(machine_id_filename.split(".")[0].split("_")[-1])

            # this file has repetitive prompt and should be modified.
            if machine_type != "_4_air_purifier" or machine_id != "3":
                continue
            #print(f"current machine_type: {machine_type} current machine id: {machine_id}")
            #if not (
                #(machine_type == "_2_washing_machine" and machine_id in {"3", "0"}) or
            #    (machine_type == "_1_microwave" and machine_id in ["1"]) #or
                #(machine_type == "_4_air_purifier" and machine_id == "3")
            #):
            #    continue

            if machine_type in [ "_6_coffee_machine"]: # "_2_washing_machine"
                continue
            
            if machine_type == "_1_microwave" and not any(s in machine_id for s in ["1", "2", "3"]): # "0", "2", "3"
                continue
            if machine_type == "_2_washing_machine" and not any(s in machine_id for s in ["0", "2", "3"]): # "0", "2", "3"
                continue
            if machine_type == "_3_rice_cooker" and not any(s in machine_id for s in ["0", "2", "4"]): 
                continue
            if machine_type == "_4_air_purifier" and not any(s in machine_id for s in ["1", "2", "3"]):
                continue

            
            user_manual_filepath = user_manual_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id)
            #os.path.join(user_manual_dir, machine_type, machine_id)
            generated_code_filepaths = [generated_code_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id) for generated_code_dir in generated_code_dirs]
            command_filepath = command_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id)

            commands = extract_list_from_file(command_filepath)
            i = 0
            for command_info in commands:
                i+=1 
                
                #if i!= 2 :
                #    continue
                command_text = command_info['command']
                command_id = str(command_info['id'])
                save_goal_state_filepath = save_goal_state_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id).replace("zzzzz", "_"+command_id)

                print("processing machine type: ", machine_type, " machine id: ", machine_id, " command id: ", command_id)
                consolidated_code_filepath = consolidated_code_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id).replace("zzzzz", "_"+command_id)
                generate_goal_state(prompt_filepath, save_goal_state_filepath, user_manual_filepath, template_code_filepaths, generated_code_filepaths, command_text, consolidated_code_filepath)


if __name__ == "__main__":
    ##################################################
    # Goal State for oracle modelling 
    ##################################################
    prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/close_loop/_2_generate_goal_state.txt')
    
    # for each testcase, save goal state code
     
    save_goal_state_filepath = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_0_G_R_E_results/_1_easy_testcases/_2_washing_machine/_0/_2_goal_states/_0.py')

    easy_save_goal_state_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_0_G_R_E_results/_1_easy_testcases/xxxxx/yyyyy/_2_goal_states/zzzzz.py')

    hard_save_goal_state_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_0_G_R_E_results/_2_hard_testcases/xxxxx/yyyyy/_2_goal_states/zzzzz.py')

    user_manual_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_1_user_manual/_2_text/xxxxx/yyyyy.txt")

    user_manual_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_1_user_manual/_2_text/_2_washing_machine/_0.txt")

    template_code_root = os.path.expanduser("~/TextToActions/code/simulated/samples")
    template_code_filepaths = [os.path.join(template_code_root, f) for f in ["_1_variables.py", "_2_features.py", "_3_actions.py"]]
    template_code_filepath = os.path.expanduser("~/TextToActions/code/simulated/samples/_0_logic_units.py")
    
    generated_code_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_4_simulators_with_states_and_display/xxxxx/yyyyy.py")

    generated_code_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_4_simulators_with_states_and_display/_2_washing_machine/_0.py")

    easy_command_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_6_testcases_specific_formatted/xxxxx/yyyyy.py")

    hard_command_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_9_testcases_compound_formatted/xxxxx/yyyyy.py")

    

    command_text = "Turn on the washing machine and set the washing cycle to Heavy."
    #generate_goal_state(prompt_filepath , save_goal_state_filepath, user_manual_filepath, template_code_filepaths, [generated_code_filepath], command_text)

    # generate goals for easy testcases
    #batch_generate_goal_state_for_G_R_E_setting(prompt_filepath, easy_save_goal_state_dir, user_manual_dir, template_code_filepaths, generated_code_dir, easy_command_dir)

    # generate goals for hard testcases
    #batch_generate_goal_state_for_G_R_E_setting(prompt_filepath, hard_save_goal_state_dir, user_manual_dir, template_code_filepaths, generated_code_dir, hard_command_dir)

    #########################################
    # Goal State for G*R generated modelling 
    #########################################

    easy_G_RE_save_goal_state_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_1_G_RE_results/_1_easy_testcases/xxxxx/yyyyy/_2_goal_states/zzzzz.py')

    hard_G_RE_save_goal_state_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_1_G_RE_results/_2_hard_testcases/xxxxx/yyyyy/_2_goal_states/zzzzz.py')

    G_RE_generated_code_dirs = [os.path.expanduser("~/TextToActions/dataset/simulated/_5_reasoning/_0_proposed_variables_for_oracle_grounding/xxxxx/yyyyy.py"), os.path.expanduser("~/TextToActions/dataset/simulated/_5_reasoning/_3_proposed_feature_list_for_oracle_grounding/xxxxx/yyyyy.py"), os.path.expanduser("~/TextToActions/dataset/simulated/_5_reasoning/_6_proposed_world_model_for_oracle_grounding/xxxxx/yyyyy.py")]

    G_RE_generated_code_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_5_reasoning/_6_proposed_world_model_for_oracle_grounding/_2_washing_machine/_0.py")

    easy_G_RE_consolidated_code_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_1_G_RE_results/_1_easy_testcases/xxxxx/yyyyy/_1_consolidation_checks/zzzzz.py")

    hard_G_RE_consolidated_code_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_1_G_RE_results/_2_hard_testcases/xxxxx/yyyyy/_1_consolidation_checks/zzzzz.py")

    # generate goals for easy testcases
    #batch_generate_goal_state_for_G_RE_setting(prompt_filepath, easy_G_RE_save_goal_state_dir, user_manual_dir, template_code_filepaths, G_RE_generated_code_dirs, easy_command_dir, easy_G_RE_consolidated_code_dir)

    # generate goals for hard testcases
    #batch_generate_goal_state_for_G_RE_setting(prompt_filepath, hard_G_RE_save_goal_state_dir, user_manual_dir, template_code_filepaths, G_RE_generated_code_dirs, hard_command_dir, hard_G_RE_consolidated_code_dir)

    # srun -u -o "log.out" -w crane1 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3


    #########################################
    # Goal State for GR generated modelling 
    #########################################

    easy_GRE_save_goal_state_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_2_GRE_results/_1_easy_testcases/xxxxx/yyyyy/_2_goal_states/zzzzz.py')

    hard_GRE_save_goal_state_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_2_GRE_results/_2_hard_testcases/xxxxx/yyyyy/_2_goal_states/zzzzz.py')

    GRE_generated_code_dirs = [os.path.expanduser("~/TextToActions/dataset/simulated/_5_reasoning/_1_proposed_variables_for_proposed_grounding/xxxxx/yyyyy.py"), os.path.expanduser("~/TextToActions/dataset/simulated/_5_reasoning/_4_proposed_feature_list_for_proposed_grounding/xxxxx/yyyyy.py"), os.path.expanduser("~/TextToActions/dataset/simulated/_5_reasoning/_7_proposed_world_model_for_proposed_grounding/xxxxx/yyyyy.py")]

    easy_GRE_consolidated_code_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_2_GRE_results/_1_easy_testcases/xxxxx/yyyyy/_1_consolidation_checks/zzzzz.py")

    hard_GRE_consolidated_code_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_2_GRE_results/_2_hard_testcases/xxxxx/yyyyy/_1_consolidation_checks/zzzzz.py")

    # generate goals for easy testcases
    batch_generate_goal_state_for_G_RE_setting(prompt_filepath, easy_GRE_save_goal_state_dir, user_manual_dir, template_code_filepaths, GRE_generated_code_dirs, easy_command_dir, easy_GRE_consolidated_code_dir)

    # generate goals for hard testcases
    #batch_generate_goal_state_for_G_RE_setting(prompt_filepath, hard_GRE_save_goal_state_dir, user_manual_dir, template_code_filepaths, GRE_generated_code_dirs, hard_command_dir, hard_GRE_consolidated_code_dir)



    
    

    
     