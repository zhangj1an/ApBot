import os
import sys
import re
import textwrap
import io  
import contextlib
import traceback
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.load_string_from_file import load_string_from_file
from simulated.utils.extract_list_from_file import extract_list_from_file
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code
from simulated.utils.create_or_replace_path import create_or_replace_path
from simulated.utils.task.propose_feature_list import format_different_features_start_with_duplicate_actions, format_contain_empty_actions_or_nonexistant_actions, format_consecutive_steps_contain_duplicate_actions
from simulated.utils.task.propose_world_model_agnostic_to_command import check_simulator_validity_of_meta_actions
# only applicable for proposed world model, both oracle grounding and proposed grounding

# based on user command, check the generated code again for missing feature list and action effects. 

# if can modify, modify. if cannot modify, report and directly uses LLM to generate actions.



def check_code_validity_for_one_appliance_command(gpt_model_type, sample_code_filepaths, action_option_filepath,generated_code_filepaths, model_prompt_text, output_filepath, user_manual_filepath, user_command_text, validity_check_prompt_filepath):

    
    code_validity_prompt = load_string_from_file(validity_check_prompt_filepath)
    #oracle_action_list = load_string_from_file(oracle_action_list_filepath)
    user_manual_text = load_string_from_file(user_manual_filepath)

    list_of_actions_string = load_string_from_file(action_option_filepath)

    code_validity_prompt = code_validity_prompt.replace("xxxxx", user_manual_text).replace("yyyyy", model_prompt_text)

    sample_code = ""
    for sample_code_filepath in sample_code_filepaths:
        sample_code += load_string_from_file(sample_code_filepath) + "\n"
    
    code_validity_prompt = code_validity_prompt.replace("zzzzz", sample_code)

    generated_code = ""
    for generated_code_dir in generated_code_filepaths:
        generated_code += load_string_from_file(generated_code_dir) + "\n"
    code_validity_prompt = code_validity_prompt.replace("wwwww", generated_code)

    code_validity_prompt = code_validity_prompt.replace("hhhhh", user_command_text)
    code_validity_prompt = code_validity_prompt.replace("uuuuu", list_of_actions_string)


    # need to add constraints that different features cannot have the same starting action. Solution: either modify the existing feature, or replace the existing feature with a new feature. 

    model = GPT4O()
    error_msg = ""
    success = False
    for i in range(3):
        print("attempt: ", i)
        updated_prompt = code_validity_prompt + "\n" + error_msg + "\n"
        with open("temp_regenerate_world_model.txt", "w") as f:
            f.write(updated_prompt)
        
        validated_code = model.chat_with_text(updated_prompt, temperature=1, top_p=1, gpt_model_type=gpt_model_type)
        validated_code = extract_python_code(validated_code) 
        validated_code = textwrap.dedent(validated_code)
        #print("validated code: \n", validated_code)

        try:
            is_ok, error_message = check_simulator_validity_of_meta_actions(generated_code + "\n" + validated_code, sample_code, list_of_actions_string, simulator_type= "ExtendedSimulator")
            if not is_ok:
                raise RuntimeError(error_message)
            
            all_code = sample_code + "\n" + generated_code + "\n" + validated_code
            
            with open("test.py", "w") as f:
                f.write(all_code)

           
            stdout_capture = io.StringIO()
            stderr_capture = io.StringIO()
            # Redirect stdout and stderr to capture outputs
            local_namespace = {}
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                exec(all_code, local_namespace)  # Execute the code


            ExtendedSimulator = local_namespace.get('ExtendedSimulator', None)

            if ExtendedSimulator is not None:
                # Create an instance of ExtendedSimulator
                updated_simulator_instance = ExtendedSimulator()  # Call the constructor

                # if the action options dont have press number buttons, then the simulator should not have press number button function , or press input string, or get original input. 

                updated_simulator_instance.reset()  # Ensure that the reset method initializes everything
                updated_feature_list = updated_simulator_instance.feature.feature_list
                #print("updated_feature_list: ", updated_feature_list)
                has_error, feedback = format_different_features_start_with_duplicate_actions(updated_feature_list, mode="specific")
                if has_error:
                    error_msg = feedback 
                    raise RuntimeError(feedback)
                has_error, feedback = format_contain_empty_actions_or_nonexistant_actions(updated_feature_list, list_of_actions_string)
                if has_error:
                    error_msg = feedback + "\n Please do not create new actions. You should only use the actions given in the Simulator() class."
                    raise RuntimeError(feedback)
                has_error, feedback = format_consecutive_steps_contain_duplicate_actions(updated_feature_list)
                if has_error:
                    error_msg = feedback 
                    raise RuntimeError(feedback)
            else:
                error_msg = "ExtendedSimulator class not found. Please create ExtendedSimulator in your response."
                raise RuntimeError(error_msg)
            
            create_or_replace_path(output_filepath)
            with open(output_filepath, "w") as f:
                f.write(validated_code)
            print(f"appliance capability is modelled in {output_filepath}.")
            success = True
            #exit()
            break 
            # as long as the code is executable, can be considered as valid code.

        except KeyError as ke:
            error_message = str(ke)
        except RuntimeError as re:
            error_msg = str(re)
            print(f"Error occurred during execution: {error_msg}")
        except ValueError as ve:
            full_traceback = str(traceback.format_exc())
            error_msg = f"Error occurred during execution: {full_traceback}. This might be because your goal variable value has invalid data format."
        except Exception as e:
            print(f"Error occurred during execution: {e}")
        
        
        print(error_message)
        #exit()
    if not success:
        print("failed to generate extendedsimulator code.")
    pass

    # > < 

# this function only applies for paper_baseline code. 
def generate_world_model_specific_to_command(gpt_model_type,prompt_filepaths,action_option_filepath, reasoning_filepaths, template_code_filepaths, testcases_result_filepaths, user_manual_filepath, command_string, use_history = True):
    
    world_model_specific_to_command_filepath = testcases_result_filepaths["world_model_specific_to_command"]

    if use_history and os.path.exists(world_model_specific_to_command_filepath):
        #print(f"extracting control panel labels files available {world_model_specific_to_command_filepath}")
        return 
    model_prompt_filepaths = [prompt_filepaths["define_variables"], prompt_filepaths["define_feature_list"], prompt_filepaths["define_world_model"]]
    regex_requirements = [r"The user manual of an appliance.*", r"The user manual of an appliance.*", r"Please help me write a Simulator.*"]
    model_prompt_text = extract_model_prompt_text(model_prompt_filepaths, regex_requirements)
    generated_code_filepaths = [reasoning_filepaths["proposed_variables"], reasoning_filepaths["proposed_features"], reasoning_filepaths["proposed_world_model"]]
    check_code_validity_for_one_appliance_command(gpt_model_type, template_code_filepaths, action_option_filepath,generated_code_filepaths, model_prompt_text, world_model_specific_to_command_filepath, user_manual_filepath, command_string, prompt_filepaths["make_world_model_specific_to_command"])
    #exit()

def check_code_validity_for_one_appliance(sample_code_filepaths, generated_code_filepaths, model_prompt_text, output_dir, user_manual_filepath, user_command_filepath, validity_check_prompt_filepath):
    commands = extract_list_from_file(user_command_filepath)
    for command_info in commands:
        command_text = command_info['command']
        command_id = str(command_info['id'])
        output_filepath = os.path.join(output_dir, "_" +command_id + ".py")
        #if command_id != "1" and command_id != "3":
        #    continue
        print("processing command id: ", command_id)
        
        check_code_validity_for_one_appliance_command( sample_code_filepaths, generated_code_filepaths, model_prompt_text, output_filepath, user_manual_filepath, command_text, validity_check_prompt_filepath)
       


    
    pass 

def check_code_validity_for_all_appliance(sample_code_filepaths, generated_code_dirs, model_prompt_text, output_dir, user_manual_dir, user_command_dir, validity_check_prompt_filepath):

    user_manual_root = "/".join(user_manual_dir.split("/")[:-2])
    machine_types = os.listdir(user_manual_root)
    for machine_type in machine_types:
        machine_ids = [f for f in os.listdir(os.path.join(user_manual_root, machine_type)) if f.endswith(".txt")]
    
        for machine_id_filename in machine_ids:
            machine_id = str(machine_id_filename.split(".")[0].split("_")[-1])
            if not (
                #(machine_type == "_2_washing_machine" and machine_id in {"3", "0"}) or
                #(machine_type == "_1_microwave" and machine_id in ["2"]) #or
                (machine_type == "_4_air_purifier" and machine_id == "3")
            ):
                continue

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

            generated_code_filepaths = [generated_code_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id) for generated_code_dir in generated_code_dirs]

            output_folder = output_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id)

            user_command_filepath = user_command_dir.replace("xxxxx", machine_type).replace("yyyyy", "_"+machine_id)

            

            print("processing machine type: ", machine_type, " machine id: ", machine_id)

            check_code_validity_for_one_appliance(sample_code_filepaths, generated_code_filepaths, model_prompt_text, output_folder, user_manual_filepath, user_command_filepath, validity_check_prompt_filepath)



def extract_model_prompt_text(prompt_filepaths, regex_requirements):
    model_prompt_text = ""

    for prompt_filepath, regex_requirment in zip(prompt_filepaths, regex_requirements):
        current_prompt_text = load_string_from_file(prompt_filepath)
        match = re.search(regex_requirment, current_prompt_text, re.DOTALL)
        current_processed_text = match.group(0) if match else "" 
        model_prompt_text += current_processed_text  + "\n\n"

    return model_prompt_text 

if __name__ == "__main__":

    # srun -u -o "log.out" -w crane1 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3

    sample_code_dir = os.path.expanduser('~/TextToActions/code/simulated/samples/')
    sample_code_filenames = ["_1_variables.py", "_2_features.py", "_3_actions.py"]
    sample_code_filepaths = [os.path.join(sample_code_dir, filename) for filename in sample_code_filenames]

    generated_code_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning')
    generated_code_for_oracle_grounding_foldernames = ["_0_proposed_variables_for_oracle_grounding", "_3_proposed_feature_list_for_oracle_grounding", "_6_proposed_world_model_for_oracle_grounding"]
    generated_code_for_proposed_grounding_foldernames = ["_1_proposed_variables_for_proposed_grounding", "_4_proposed_feature_list_for_proposed_grounding", "_7_proposed_world_model_for_proposed_grounding"]
    generated_code_for_oracle_grounding_dirs = [os.path.join(generated_code_dir, foldername, "xxxxx/yyyyy.py") for foldername in generated_code_for_oracle_grounding_foldernames]

    generated_code_for_proposed_grounding_dirs = [os.path.join(generated_code_dir, foldername, "xxxxx/yyyyy.py") for foldername in generated_code_for_proposed_grounding_foldernames]

   

    model_prompt_dir = os.path.expanduser('~/TextToActions/code/simulated/prompts')

    model_prompt_filenames = ["_14_define_variables.txt", "_15_define_feature_list.txt", "_16_define_world_model.txt"]
    model_prompt_filepaths = [os.path.join(model_prompt_dir, filename) for filename in model_prompt_filenames]
    regex_requirements = [r"The user manual of an appliance.*", r"The user manual of an appliance.*", r"Please help me write a Simulator.*"]
    model_prompt_text = extract_model_prompt_text(model_prompt_filepaths, regex_requirements)

    validity_check_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/close_loop/_1_regenerate_model.txt')

    user_manual_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_2_text/xxxxx/yyyyy.txt')

    G_RE_easy_command_code_calibration_output_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_1_G_RE_results/_1_easy_testcases/xxxxx/yyyyy/_1_consolidation_checks')

    G_RE_hard_command_code_calibration_output_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_1_G_RE_results/_2_hard_testcases/xxxxx/yyyyy/_1_consolidation_checks')

    easy_command_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_6_testcases_specific_formatted/xxxxx/yyyyy.py")

    hard_command_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_9_testcases_compound_formatted/xxxxx/yyyyy.py")

    #########################################
    # G_RE case 
    #########################################

    # check code against user command, easy command 
    #check_code_validity_for_all_appliance(sample_code_filepaths, generated_code_for_oracle_grounding_dirs, model_prompt_text, G_RE_easy_command_code_calibration_output_dir, user_manual_dir, easy_command_dir, validity_check_prompt_filepath)

    # check code against user command, hard command
    #check_code_validity_for_all_appliance(sample_code_filepaths, generated_code_for_oracle_grounding_dirs, model_prompt_text, G_RE_hard_command_code_calibration_output_dir, user_manual_dir, hard_command_dir, validity_check_prompt_filepath)


    #########################################
    # GRE case 
    #########################################

    GRE_easy_command_code_calibration_output_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_2_GRE_results/_1_easy_testcases/xxxxx/yyyyy/_1_consolidation_checks')

    GRE_hard_command_code_calibration_output_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_6_results/_5_astar_planner/_2_GRE_results/_2_hard_testcases/xxxxx/yyyyy/_1_consolidation_checks')

    # check code against user command, easy command 
    check_code_validity_for_all_appliance(sample_code_filepaths, generated_code_for_proposed_grounding_dirs, model_prompt_text, GRE_easy_command_code_calibration_output_dir, user_manual_dir, easy_command_dir, validity_check_prompt_filepath)

    # check code against user command, hard command
    check_code_validity_for_all_appliance(sample_code_filepaths, generated_code_for_proposed_grounding_dirs, model_prompt_text, GRE_hard_command_code_calibration_output_dir, user_manual_dir, hard_command_dir, validity_check_prompt_filepath)




