
import os
import contextlib
import io
import sys
sys.path.append(os.path.expanduser("~/TextToActions/code"))
import simulated._0_t2a_config
from simulated.utils.create_or_replace_path import create_or_replace_path
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code
from simulated.utils.load_string_from_file import load_string_from_file
from simulated.utils.extract_python_code import extract_python_code
import re

def extract_define_feature_prompt_content(input_string):
    match = re.search(r"The user manual of an appliance\s*(.*)", input_string)
    return match.group(1).strip() if match else ""

def format_different_features_start_with_duplicate_actions(feature_dict):
    """
    Validate if the first step's actions between every two features contain duplicate actions.

    Args:
        feature_dict (dict): Dictionary where keys are features, and values are lists of steps.

    Returns:
        bool: True if any two features have overlapping actions in their first step's actions, False otherwise.
    """

    action_to_features = {}  # To map each action to the features it belongs to

    for feature_name, steps in feature_dict.items():
        for step in steps:
            if step["step"] == 1:  # Only consider step 1
                for action in step["actions"]:  # Check each action individually
                    if action in action_to_features:
                        # Duplicate found, print error message
                        existing_feature = action_to_features[action]
                        error_msg = (
                            f"Error: Features '{existing_feature}' and '{feature_name}' have the same step 1 action: {action}. It is possible you created non-existent or duplicate features. Please take a look at the ' Modelling rules to avoid ambiguity' section and try again."
                        )
                        return True, error_msg
                    else:
                        action_to_features[action] = feature_name  # Map action to feature name
                break  # Only consider step 1 for each feature
    return False, ""



    

def format_consecutive_steps_contain_duplicate_actions(feature_dict):
    """
    Validate if, within the same dictionary key, consecutive steps have duplicate actions.

    Args:
        feature_dict (dict): Dictionary where keys are features, and values are lists of steps.

    Returns:
        bool: True if all features have no duplicate actions between consecutive steps, False otherwise.
    """
    for feature, steps in feature_dict.items():
        # Sort steps by their "step" index
        steps_sorted = sorted(steps, key=lambda x: x["step"])
        
        # Check for duplicates between consecutive steps
        for i in range(len(steps_sorted) - 1):
            current_actions = set(steps_sorted[i].get("actions", []))
            next_actions = set(steps_sorted[i + 1].get("actions", []))
            
            # Check for common actions between the current and next steps
            if current_actions & next_actions:
                error_msg = f"Feature '{feature}' has duplicate actions between steps {i + 1} and {i + 2}"
                return True, error_msg  # Found duplicate actions between consecutive steps
    
    return False, ""  # No duplicates found in any feature

def format_feature_step_contain_no_variables(feature_list):
    """
    Generate a list of formatted strings for features with steps that have no 'actions' or an empty 'actions'.
    except for "null" and "empty".
    Args:
        feature_dict (dict): A dictionary of features.

    Returns:
        tuple: A list of feature strings for features containing steps with no 'actions'.
    """
    features_with_no_variables = []

    for feature, steps in feature_list.items():
        # Start with the feature title
        feature_string = f"The feature is: {feature}.\n"
        has_no_variable = False
        if feature == "null" or feature == "empty":
            continue
        for step in steps:
            # Construct a detailed string for each step
            step_details = ', '.join([f"{key}: {value}" for key, value in step.items()])
            feature_string += f"  {step_details}\n"

            # Check if the step has no 'actions' or an empty 'actions'
            if "variable" not in step:
                has_no_variable = True

        # If the feature has steps with no actions, add to the no-actions list
        if has_no_variable:
            features_with_no_variables.append(feature_string)
   
    return features_with_no_variables

def format_action_not_missing_variable(feature_list, user_manual_text, verify_feature_list_prompt, define_feature_list_task_prompt_filepath,list_of_variables, verbose = False):
    # not including this step anymore because it is highly error prone. 
    # !!!
    # firstly check for features that contains actions with no variables. 
    # write a prompt to specifically check the validity of this prompt against the user manual text. If return invalid, then generate again. 
    define_feature_instruction = load_string_from_file(define_feature_list_task_prompt_filepath)
    define_feature_instruction = extract_define_feature_prompt_content(define_feature_instruction)
    features_containing_steps_with_no_variables = format_feature_step_contain_no_variables(feature_list)
    print("features_containing_steps_with_no_variables", features_containing_steps_with_no_variables)
    error_msgs = ""
    feature_has_error = False 
    if len(features_containing_steps_with_no_variables) > 0:
        for feature in features_containing_steps_with_no_variables:
            prompt = load_string_from_file(verify_feature_list_prompt)
            prompt = prompt.replace("xxxxx", user_manual_text)
            prompt = prompt.replace("yyyyy", "\n".join(feature))
            prompt = prompt.replace("zzzzz", list_of_variables)
            
            prompt = prompt.replace("wwwww", define_feature_instruction)
            model = GPT4O()
            response = model.chat_with_text(prompt)   
            #response = response.lower()
            #print(f"verify feature validity response: \n\n {response} \n\n")
            print(f"examining feature: {feature}")
            response = extract_python_code(response)
            print("extracted response: ", response)
            #exit()
            local_namespace = {}
            exec(response, local_namespace)
            has_error = local_namespace.get('has_error', None)
            step_index = local_namespace.get('step_index', None)
            missing_variable = local_namespace.get('missing_variable', None)

            if verbose: 
                print(f"prompt: \n\n {prompt} \n\n")
                #print(f"response: \n\n {response} \n\n")
            
            if has_error:  
                error_msgs += f"The following feature should have an additional variable with name {missing_variable} added to step {step_index}. \n {feature}. \n"
                feature_has_error = True

    if feature_has_error:
        print("error_msgs: ", error_msgs)
        
        return True, error_msgs + "\n Note that this is an suggestion, and you can decide whether to follow it. And the actions used to process numbers and alphabets should be abstracted to meta_actions_on_xxx. \n"
    return False, ""

def format_input_string(feature_list):
    for feature, steps in feature_list.items():
        for step in steps:
            if "variable" in step and step["variable"] == "variable_input_string":
                return False, f"In feature {feature}, step: {step}, please list the actual variable that is being adjusted. 'variable_input_string' is just for processing the raw input and should not be listed."
    return True, ""
                               
def format_action_all_modelled(feature_list, list_of_actions_string):
    list_of_actions = [line.strip() for line in list_of_actions_string.splitlines() if line.strip()]
    print("list_of_actions", list_of_actions)
    #exit()
    error_msg = "There are actions being proposed but not modelled in the feature list."
    # Gather all actions from the feature list
    all_feature_actions = set()
    for feature, steps in feature_list.items():
        for step in steps:
            all_feature_actions.update(step.get("actions", []))
    condition = all_feature_actions.issuperset(list_of_actions)
    if condition:
        return True, ""
    else:
        return False, f"{error_msg} Missing actions: {set(list_of_actions) - all_feature_actions}"
       #return False, f"{error_msg} proposed actions: {list_of_actions}, modelled actions: {all_feature_actions}, Missing actions: {set(list_of_actions) - all_feature_actions}"

def format_action_meta_actions(feature_list, verify_feature_list_meta_actions_prompt, list_of_variables, verbose = False):

    for feature in feature_list:
        steps = feature_list[feature]
        for step in steps:
            if "actions" in step:
                actions = step["actions"]
                if isinstance(actions, list) and len(actions) >= 4:
                    # check if meta actions are present
                    # if yes, then return True, else return False 
                    #print(f"list of variables: {list_of_variables}")
                    #exit()
                    prompt = load_string_from_file(verify_feature_list_meta_actions_prompt)
                    prompt = prompt.replace("xxxxx", str(actions))
                    model = GPT4O()
                    response = model.chat_with_text(prompt)   
                    response = response.lower()
                    if verbose: 
                        print(f"prompt: \n\n {prompt} \n\n")
                        #print(f"response: \n\n {response} \n\n")
                    print(f"verify feature validity response: \n\n {response} \n\n")
                    if "yes" in response:    
                        return False, f"Meta actions are missing for feature '{feature}'"
                    
    return True, ""

def verify_feature_syntax(feature_list, user_manual_text, list_of_actions_string, define_feature_list_task_prompt_filepath, verify_feature_list_prompt, list_of_variables, verify_feature_list_meta_actions_prompt, check_different_features_start_with_duplicate_actions = True):

    """
    Policy template bug:
        1. Same feature, two consecutive steps have the same action (code) verify_feature_syntax(feature_list, same)
        2. Two different features have the same starting action (code)
        3. An action is supposed to be tied to a variable (e.g. menu button can adjust menu), but was not mentioned.  (针对那些没有action 的step重点检查）verify_steps_with_no_variabls(feature, user_manual_text)
        4. Missing feature, not all actions are present in the feature list, meaning it is not exhaustively used. Maybe use a “redundant action” list to ensure no action is left off (code) check_no_missing_actions(action_list, feature_list)
        5. missing meta actions when it is needed to be created. check when number of actions is a list and lengths >= 4 
    """
    valid, error_msg = format_input_string(feature_list)
    if not valid: 
        print(f"syntax error 1: {error_msg}")
        return False, error_msg
    print("passed syntax check 1")

    valid, error_msg = format_action_all_modelled(feature_list, list_of_actions_string)
    if not valid:
        print(f"syntax error 2: {error_msg}")
        return False, error_msg
    print("passed syntax check 2")

    contain_error, error_msg = format_consecutive_steps_contain_duplicate_actions(feature_list)
    if contain_error:
        print(f"syntax error 3: {error_msg}")
        return False, error_msg
    print("passed syntax check 3")
    if check_different_features_start_with_duplicate_actions:
        contain_error, error_msg = format_different_features_start_with_duplicate_actions(feature_list)
        if contain_error:
            print(f"syntax error 4: {error_msg}")
            return False, error_msg
        print("passed syntax check 4")

    # the following check is highly error prone, omitting.
    #contain_error, error_msg = format_action_not_missing_variable(feature_list, user_manual_text, verify_feature_list_prompt, define_feature_list_task_prompt_filepath, list_of_variables)
    #if contain_error:
    #    print(f"syntax error 5: {error_msg}")
    #    return False, error_msg
    #print("passed syntax check 5")
    
    
    # make sure all actions appeared in the feature. use a code to do that, given the variable list, and the feature list, just check whether all actions are involved. 
    return True, ""
    pass 

def define_feature_list(proposed_actions_filepath, proposed_variables_filepath, user_manual_filepath, define_feature_list_task_prompt_filepath, feature_list_filepath, feature_sample_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions_prompt, check_different_features_start_with_duplicate_action = True, verbose=False):
    
    prompt = ""
    
    with open(define_feature_list_task_prompt_filepath, "r") as f:
        prompt = f.read()

    with open(user_manual_filepath, "r") as f:
        user_manual_text = f.read()
    prompt = prompt.replace("xxxxx", user_manual_text)

    with open(proposed_actions_filepath, "r") as f:
        list_of_actions = f.read()
    list_of_actions = re.sub(r"\s*\(.*?\)", "", list_of_actions)
    prompt = prompt.replace("yyyyy", list_of_actions) 

    with open(proposed_variables_filepath, "r") as f:
        list_of_variables = f.read()
    prompt = prompt.replace("zzzzz", list_of_variables)

    with open(feature_sample_code_filepath, "r") as f: 
        feature_sample_code = f.read()
    prompt = prompt.replace("hhhhh", feature_sample_code)
    updated_prompt = prompt 
    for i in range(5):
        print(f"Attempt {i + 1} to generate valid feature list.")
        model = GPT4O()
        response = model.chat_with_text(updated_prompt)
        response = extract_python_code(response)
        if verbose:
            print(f"response: {response}")
        try:
            # firstly import the sample feature file, then execute this code 
            # feature_list 

            """
            Policy template bug:
                1. Same feature, two consecutive steps have the same action (code) verify_feature_syntax(feature_list, same)
                2. Two different features have the same starting action (code)
                3. An action is supposed to be tied to a variable (e.g. menu button can adjust menu), but was not mentioned.  (针对那些没有action 的step重点检查）verify_steps_with_no_variabls(feature, user_manual_text)
                4. Missing feature, not all actions are present in the feature list, meaning it is not exhaustively used. Maybe use a “redundant action” list to ensure no action is left off (code) check_no_missing_actions(action_list, feature_list)
                5. missing meta actions when it is needed to be created
            """

            stdout_capture = io.StringIO()
            stderr_capture = io.StringIO()
            
            entire_code_environment = feature_sample_code + "\n" + response
            # Redirect stdout and stderr to capture outputs
            #print("entire_code\n", entire_code_environment)
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                exec(entire_code_environment, globals())  # Execute the code
            
            
            # feature_sequence = ["power_on", "set_program", "set_temperature", "set_load_size", "start_washing"]

            # Retrieve feature_sequence from globals
            feature_list = globals().get('feature_list', None)
            #print("feature_list\n", feature_list)
            if feature_list is None:
                raise ValueError("feature_list not found in the global scope.")

            valid_flag, error_msg = verify_feature_syntax(feature_list, user_manual_text, list_of_actions, define_feature_list_task_prompt_filepath,verify_feature_list_prompt, list_of_variables, verify_feature_list_meta_actions_prompt, check_different_features_start_with_duplicate_actions = False)
            # Check if feature_sequence exists and is not None
            if valid_flag:
                # save response to task list filepath
                with open(feature_list_filepath, "w") as f:
                    f.write(str(response))
                    print(f"Task list saved to {feature_list_filepath}")
                return True
            else:
                error_report = f"In your previous attempt, you generated a feature list as follows:\n\n {response} \n\n However, the feature list is invalid due to the following reasons:\n\n {error_msg} \n\n Please try again."
                updated_prompt = prompt + "\n" + error_report
        except KeyError as ke:
            print(f"KeyError: {ke}")
            
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"Stderr from exec(): {e}")
            print(stderr_capture.getvalue())

    print("Failed to generate valid feature list after 3 attempts.")
    print(response)
    return False

def batch_define_feature_list(proposed_actions_dir = "", proposed_variables_dir="", user_manual_dir = "", feature_list_dir = "", define_feature_list_task_prompt_filepath = "", feature_code_filepath="", verify_feature_list_prompt="", verify_feature_list_meta_actions = "", have_prefix = True):   
    machine_type_dirs = [os.path.join(user_manual_dir, d) for d in os.listdir(user_manual_dir) if os.path.isdir(os.path.join(user_manual_dir, d))]
        
    for dir1 in machine_type_dirs:
        # List all subdirectories in each level one directory
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith(('.txt'))]
        for dir2 in machine_id_dirs:
            # Washing machine: 0, 2, 3
            # Rice cooker: 0, 2, 4 || 0, 4
            # Air purifier: 1, 2, 3 || 1, 2
            machine_type = dir1.split("/")[-1]
            machine_id = dir2.split("/")[-1].split(".")[0].split("_")[-1]
            print(f"passing by: {machine_type}, {machine_id}")

            if not any(s in f"{machine_type}/{machine_id}" for s in ["_5_induction_cooker/1"]): # "_1_washing_machine/1", "_2_rice_cooker/1"
                continue
            #if machine_type == "_1_washing_machine" and any(s in machine_id for s in ["1"]): # "0", "2", "3"
            #    continue
            #if machine_type == "_4_microwave_oven" and not any(s in machine_id for s in ["2"]): # "0", "2", "3"
            #    continue
            relative_path = os.path.relpath(dir2, user_manual_dir).replace(".txt", ".py")
            relative_path_last_file_no_prefix = relative_path.split("/")[-1].split("_")[1]
            relative_path_last_file_have_prefix = relative_path.split("/")[-1]
            relative_path_dir = "/".join(relative_path.split("/")[:-1])
            if have_prefix:
                proposed_actions_filepath = os.path.join(proposed_actions_dir, relative_path_dir,relative_path_last_file_have_prefix).replace(".py", ".txt")
                save_feature_list_filepath = os.path.join(feature_list_dir, relative_path_dir,relative_path_last_file_have_prefix)
                proposed_variables_filepath = os.path.join(proposed_variables_dir, relative_path_dir,relative_path_last_file_have_prefix)
            else:
                proposed_actions_filepath = os.path.join(proposed_actions_dir, relative_path_dir,relative_path_last_file_no_prefix).replace(".py", ".txt")
                save_feature_list_filepath = os.path.join(feature_list_dir, relative_path_dir,relative_path_last_file_no_prefix)
                proposed_variables_filepath = os.path.join(proposed_variables_dir, relative_path_dir,relative_path_last_file_no_prefix)
            
            
            
            create_or_replace_path(save_feature_list_filepath)
            define_feature_list(proposed_actions_filepath, proposed_variables_filepath, dir2, define_feature_list_task_prompt_filepath, save_feature_list_filepath, feature_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions, check_different_features_start_with_duplicate_action = False)
            #exit()
            
    pass 
if __name__ == "__main__":

    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Generate Policy Template given oracle actions
    #
    #######################################

    oracle_actions_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_1_oracle_available_actions')
     
    user_manual_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text')

    feature_code_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_2_features.py')
    
    feature_list_for_oracle_grounding_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_5_reasoning/_3_proposed_feature_list_for_oracle_grounding')

    proposed_variables_for_oracle_grounding_dir=os.path.expanduser('~/TextToActions/datasetv2/real_world/_5_reasoning/_0_proposed_variables_for_oracle_grounding')

    define_feature_list_task_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_15_define_feature_list.txt')

    verify_feature_list_prompt = os.path.expanduser('~/TextToActions/code/simulated/prompts/_15_verify_feature_list.txt')
    verify_feature_list_meta_actions_prompt = os.path.expanduser('~/TextToActions/code/simulated/prompts/_15_verify_meta_actions.txt')
    print("test")
    batch_define_feature_list(oracle_actions_dir, proposed_variables_for_oracle_grounding_dir, user_manual_dir, feature_list_for_oracle_grounding_dir, define_feature_list_task_prompt_filepath, feature_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions_prompt, have_prefix = True)

    #######################################
    #
    # Generate Policy Template (Feature List) given proposed actions
    #
    #######################################

    proposed_actions_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_4_visual_grounding/_1_action_names/_1_proposed_action_names')

    proposed_variables_for_proposed_grounding_dir=os.path.expanduser('~/TextToActions/datasetv2/real_world/_5_reasoning/_1_proposed_variables_for_proposed_grounding')

    feature_list_for_proposed_grounding_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_5_reasoning/_4_proposed_feature_list_for_proposed_grounding')

    #batch_define_feature_list(proposed_actions_dir, proposed_variables_for_proposed_grounding_dir, user_manual_dir, feature_list_for_proposed_grounding_dir, define_feature_list_task_prompt_filepath, feature_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions_prompt)

    
