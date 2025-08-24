
import os
import _0_t2a_config
from utils.create_or_replace_path import create_or_replace_path
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code
import inspect
import re
# for number inputs, the prompt need to modify to add a map string to action. so during search, it is hard to search using astar. instead should find another strategy....

# for action effect, should choose from templates, not generating on its own 

# for action effects on changing variable ranges, should modify the original variable instead of the point of interest. 

# do format check: 
# if self.meta_actions_on_number is existant on the generated code, then the function get_original_input must be present in the object. 


def check_variable_format_exists(code, combinations):
    """
    Check whether the given variable and feature combinations appear in the code.

    :param code: The Python code as a string.
    :param combinations: List of (variable_name, feature_name) tuples to check.
    :return: A tuple (bool, error_message). False and error message if missing combinations, True and empty string if all exist.
    """
    # Regex pattern to capture variable_name and intended_feature in conditions
    pattern = re.compile(
        r'\(\s*(?:variable_name\s*==\s*"(.*?)"\s*and\s*intended_feature\s*(?:==\s*"(.*?)"|in\s*\[(.*?)\])|intended_feature\s*==\s*"(.*?)"\s*and\s*variable_name\s*==\s*"(.*?)")\s*\)'
    )

    # Find all matches in the code
    matches = pattern.findall(code)

    # Normalize matches to account for both `==` and `in [...]`
    normalized_matches = []
    for match in matches:
        variable_name = match[0] or match[4]  # First pattern or reversed pattern
        single_feature = match[1] or match[3]  # Single feature in either order
        feature_list = match[2]
        
        if single_feature:
            # Single feature case
            normalized_matches.append((variable_name, single_feature))
        elif feature_list:
            # List of features case: Split and normalize
            features = [item.strip().strip('"') for item in feature_list.split(",")]
            normalized_matches.extend((variable_name, feature) for feature in features)

    # Prepare an error message for missing combinations
    missing_combinations = [
        (variable_name, feature_name)
        for feature_name, variable_name in combinations
        if (variable_name, feature_name) not in normalized_matches
    ]

    if missing_combinations:
        # Build the error message
        error_message = "\n".join(
            f"The variable '{variable_name}' in feature '{feature_name}' is required to be included in the 'get_original_input' method of the Simulator class."
            for variable_name, feature_name in missing_combinations
        )
        return False, error_message

    return True, ""


def check_input_string_compatibility(generated_code, given_code):
    # need to find a way to tell whether the variable is included in get_original_input. 
    # so check all the feature list, and if the actions are inside the meta_actions_dict, try a variable name in the get_original_input 


    # Execute the generated code
    namespace = {}
    exec(given_code + "\n" + generated_code , namespace)
    
    

    # Check if the Simulator class is defined
    if 'Simulator' in namespace:
        simulator_instance = namespace['Simulator']()  # Instantiate the Simulator object
        

        # Check if `self.meta_actions_dict` exists
        if hasattr(simulator_instance, 'meta_actions_dict'):
            print("Simulator has 'meta_actions_dict'.")

            # Check if `get_origianl_input` is a method of Simulator
            if inspect.ismethod(getattr(simulator_instance, 'get_original_input', None)):
                feature_list = namespace['feature_list']
                variables_require_input_format = []
                meta_actions = simulator_instance.meta_actions_dict.values()
                for feature_name, steps in feature_list.items():  # Iterate over feature names and their corresponding steps
                    for step in steps:  # Iterate over each step in the feature
                        actions = step["actions"]
                        if any(action in meta_actions for action in actions):
                            variable = step.get("variable") 
                            if variable:
                                variables_require_input_format.append((feature_name, variable))  
                #print(f"Meta actions dict: {meta_actions}")
                #print("Variables require input format: ", variables_require_input_format)
                try:
                    valid, error_msg = check_variable_format_exists(generated_code, variables_require_input_format)
                    if not valid:
                        return False, error_msg
                except:
                    return False, f"All the variables that requires meta actions to input values should be included in the 'get_original_input' method of the Simulator class. Note that both the variable name and feature name must exists in the condition in the format: (variable_name == 'variable_name' and intended_feature == 'feature_name')."
                return True, ""
            else:
                return False, "The generated code has 'meta_actions_dict' created as a variable, but does not have the required method 'get_origianl_input'. "
        else:
            return True, ""
    else:
        return False, "Simulator class is not defined in the code."
     
def define_world_model(proposed_actions_filepath, proposed_variables_filepath, proposed_feature_list_filepath, user_manual_filepath, define_world_model_task_prompt_filepath, saved_world_model_filepath, template_variable_filepath, template_feature_filepath, template_action_filepath):
    
    prompt = ""
    
    with open(define_world_model_task_prompt_filepath, "r") as f:
        prompt = f.read()
    #with open("temp_a.txt", "w") as f:
    #    f.write(prompt)
    with open(user_manual_filepath, "r") as f:
        user_manual_text = f.read()
    prompt = prompt.replace("xxxxx", user_manual_text)

    with open(proposed_actions_filepath, "r") as f:
        action_list = f.read()
    prompt = prompt.replace("yyyyy", action_list)

    template_variable = ""
    template_feature = ""
    template_action = ""
    with open(template_variable_filepath, "r") as f:
        template_variable = f.read()
    with open(template_feature_filepath, "r") as f:
        template_feature = f.read()
    with open(template_action_filepath, "r") as f:
        template_action = f.read()
    prompt = prompt.replace("zzzzz", template_variable + "\n" + template_feature + "\n" + template_action)

    with open(proposed_variables_filepath, "r") as f:
        variable_list = f.read()
    prompt = prompt.replace("hhhhh", variable_list) 

    with open(proposed_feature_list_filepath, "r") as f:
        proposed_feature_list = f.read() 
    prompt = prompt.replace("wwwww", proposed_feature_list)
    
    #print(prompt)
    # load prompt from file

    given_code = template_variable + "\n" + template_feature + "\n" + template_action + "\n" + variable_list + "\n" + proposed_feature_list + "\n"
    model = GPT4O()

    attempt_count = 0
    error_message = ""
    response = ""
    print(response)
    while attempt_count < 5:
        updated_prompt = prompt + f"In your previous attempt, the generated response is:\n {response}\n The following error was found:\n{error_message}\n Please correct these errors."
        print("Attempt to generate world model: ", attempt_count)
        response = model.chat_with_text(updated_prompt)
        response = extract_python_code(response)
        # save response to task list filepath
        with open("temp.txt", "w") as f:
            f.write(str(response))
        is_ok, error_message = check_input_string_compatibility(response, given_code)
        
        if is_ok:
            with open(saved_world_model_filepath, "w") as f:
                f.write(str(response))
                print(f"Task list saved to {saved_world_model_filepath}")
            break
        else:
            print(error_message)
            error_message = error_message.replace("\n", " ")
            attempt_count += 1
            if attempt_count >= 5:
                print(response)
        #exit()



    
def batch_define_world_model(proposed_actions_dir = "/data/home/jian/RLS_microwave/benchmark_2/proposed_actions", proposed_variables_dir="/data/home/jian/RLS_microwave/benchmark_2/user_manual_variable_list", proposed_feature_list_dir="/data/home/jian/RLS_microwave/benchmark_2/user_manual_feature_list", user_manual_dir = "/data/home/jian/RLS_microwave/benchmark_2/user_manual_extracted_text_gpt4o", define_world_model_task_prompt_filepath = "/data/home/jian/RLS_microwave/utils/_5_build_world_model/prompts/define_world_model.txt", save_world_model_dir="/data/home/jian/RLS_microwave/benchmark_2/proposed_world_model", template_variable_filepath="", template_feature_filepath="", template_action_filepath="", have_prefix = True):   
    machine_type_dirs = [os.path.join(user_manual_dir, d) for d in os.listdir(user_manual_dir) if os.path.isdir(os.path.join(user_manual_dir, d))]
    

    # Washing machine: 0, 2, 3
    # Rice cooker: 0, 2, 4 || 0, 4
    # Air purifier: 1, 2, 3 || 1, 2

    
    for dir1 in machine_type_dirs:
        # List all subdirectories in each level one directory
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith(('.txt'))]
        for dir2 in machine_id_dirs:
            #if not ("_1_microwave" in dir1 and any(s in dir2 for s in ["2.txt"])):
            #    continue
            
            machine_type = dir1.split("/")[-1]
            machine_id = dir2.split("/")[-1].split(".")[0].split("_")[-1]
            print(f"passing by: {machine_type}, {machine_id}")

            #if not any(s in machine_type for s in ["_2_bottle_washer", "_4_microwave_oven"]):
            #    continue

            #if machine_type == "_2_bottle_washer" and not any(s in machine_id for s in ["1", "4"]): # "0", "2", "3"
            #    continue
            #if machine_type == "_4_microwave_oven" and not any(s in machine_id for s in ["2"]): # "0", "2", "3"
            #    continue
            if not any(s in f"{machine_type}/{machine_id}" for s in ["_4_water_dispenser/1"]): # "_1_washing_machine/1", "_2_rice_cooker/1"
                continue
            print("processing: ", dir2)
            relative_path = os.path.relpath(dir2, user_manual_dir).replace(".txt", ".py")
            relative_path_last_file_no_prefix = relative_path.split("/")[-1].split("_")[1]
            relative_path_last_file_have_prefix = relative_path.split("/")[-1]
            relative_path_dir = "/".join(relative_path.split("/")[:-1])
            if have_prefix:
                proposed_actions_filepath = os.path.join(proposed_actions_dir, relative_path_dir, relative_path_last_file_have_prefix).replace(".py", ".txt")
                proposed_feature_list_filepath = os.path.join(proposed_feature_list_dir, relative_path_dir, relative_path_last_file_have_prefix)
                proposed_variables_filepath = os.path.join(proposed_variables_dir, relative_path_dir, relative_path_last_file_have_prefix)
                save_world_model_filepath = os.path.join(save_world_model_dir, relative_path_dir, relative_path_last_file_have_prefix)
            else:
                proposed_actions_filepath = os.path.join(proposed_actions_dir, relative_path_dir, relative_path_last_file_no_prefix).replace(".py", ".txt")
                proposed_feature_list_filepath = os.path.join(proposed_feature_list_dir, relative_path_dir, relative_path_last_file_no_prefix)
                proposed_variables_filepath = os.path.join(proposed_variables_dir, relative_path_dir, relative_path_last_file_no_prefix)
                save_world_model_filepath = os.path.join(save_world_model_dir, relative_path_dir, relative_path_last_file_no_prefix)
            
            create_or_replace_path(save_world_model_filepath)
            define_world_model(proposed_actions_filepath, proposed_variables_filepath, proposed_feature_list_filepath, dir2, define_world_model_task_prompt_filepath, save_world_model_filepath, template_variable_filepath, template_feature_filepath, template_action_filepath)
            #exit()
            
    pass 

if __name__ == "__main__":

    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Create World Model for oracle actions
    #
    #######################################
    oracle_actions_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_1_oracle_available_actions')
    
    user_manual_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text')
    
    #define_world_model_task_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_16_define_world_model.txt')

    define_world_model_task_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/paper_exp/real_world/_4_HV_M_SR_MA_agnostic/_4_define_world_model.txt')
    #TextToActions/code/simulated/prompts/paper_exp/real_world/_4_HV_M_SR_MA_agnostic/_4_define_world_model.txt

    proposed_variables_for_oracle_grounding_dir=os.path.expanduser('~/TextToActions/datasetv2/real_world/_5_reasoning/_0_proposed_variables_for_oracle_grounding')

    proposed_feature_list_for_oracle_grounding_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_5_reasoning/_3_proposed_feature_list_for_oracle_grounding')
    
    save_world_model_for_oracle_grounding_dir=os.path.expanduser('~/TextToActions/datasetv2/real_world/_5_reasoning/_6_proposed_world_model_for_oracle_grounding')

    template_variable_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples_real_world/_1_variables.py')
    template_feature_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_2_features.py')
    template_action_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_3_actions.py')

    batch_define_world_model(oracle_actions_dir, proposed_variables_for_oracle_grounding_dir, proposed_feature_list_for_oracle_grounding_dir, user_manual_dir, define_world_model_task_prompt_filepath, save_world_model_for_oracle_grounding_dir, template_variable_filepath, template_feature_filepath, template_action_filepath, have_prefix= True)

    #######################################
    #
    # Create World Model for proposed actions
    #
    #######################################

    proposed_actions_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_1_action_names/_1_proposed_action_names')

    proposed_variables_for_proposed_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_1_proposed_variables_for_proposed_grounding')

    proposed_feature_list_for_proposed_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_4_proposed_feature_list_for_proposed_grounding')

    save_world_model_for_proposed_grounding_dir=os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_7_proposed_world_model_for_proposed_grounding')

    #batch_define_world_model(proposed_actions_dir, proposed_variables_for_proposed_grounding_dir, proposed_feature_list_for_proposed_grounding_dir, user_manual_dir, define_world_model_task_prompt_filepath, save_world_model_for_proposed_grounding_dir, template_variable_filepath, template_feature_filepath, template_action_filepath,)


    