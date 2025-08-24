
import os
import contextlib
import io
import sys
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.create_or_replace_path import create_or_replace_path
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code
from simulated.utils.load_string_from_file import load_string_from_file
import re
import copy

def extract_define_feature_prompt_content(input_string):
    match = re.search(r"The user manual of an appliance\s*(.*)", input_string)
    return match.group(1).strip() if match else ""

def format_different_features_start_with_duplicate_actions(feature_dict_copy, mode = "agnostic"):
    """
    Validate if the first step's actions between every two features contain duplicate actions.

    Args:
        feature_dict (dict): Dictionary where keys are features, and values are lists of steps.

    Returns:
        bool: True if any two features have overlapping actions in their first step's actions, False otherwise.
    """
    feature_dict = copy.deepcopy(feature_dict_copy)
    feature_dict.pop("empty", None)  # Remove the "empty" feature if it exists
    action_to_features = {}  # To map each action to the features it belongs to

    for feature_name, steps in feature_dict.items():
        for step in steps:
            if step["step"] == 1:  # Only consider step 1
                for action in step["actions"]:  # Check each action individually
                    if action in action_to_features:
                        # Duplicate found, print error message
                        existing_feature = action_to_features[action]
                        error_msg = f"Error: Features '{existing_feature}' and '{feature_name}' have the same step 1 action: {action}. "
                        
                        if mode == "agnostic":
                            error_msg += f"The first possibility is the features you created are parts of features with longer steps. Then you should merge existing features into bigger ones. The second possibility is the first step itself is a seperate feature. Then single out the first step as a feature, the rest steps as another feature. "
                        elif mode == "specific":
                            error_msg += f"Please directly overwrite the feature {existing_feature} in the feature_list instead of creating a new one {feature_name} in the updated_feature_list."
                        return True, error_msg
                    else:
                        action_to_features[action] = feature_name  # Map action to feature name
                break  # Only consider step 1 for each feature
    return False, ""



def format_consecutive_steps_contain_duplicate_variables(feature_dict):
    """
    Validate if, within the same dictionary key, consecutive steps have duplicate variables.

    Args:
        feature_dict (dict): Dictionary where keys are features, and values are lists of steps.

    Returns:
        bool, str: True and an error message if duplicate variables are found in consecutive steps; False and empty string otherwise.
    """
    for feature, steps in feature_dict.items():
        # Sort steps by their "step" index
        steps_sorted = sorted(steps, key=lambda x: x["step"])
        
        for i in range(len(steps_sorted) - 1):
            current_var = steps_sorted[i].get("variable")
            next_var = steps_sorted[i + 1].get("variable")
            
            if current_var and next_var and current_var == next_var:
                error_msg = (
                    f"Feature '{feature}' has the same variable '{current_var}' "
                    f"in both step {i + 1} and step {i + 2}. Consider remove this variable from one of the step."
                )
                return True, error_msg  # Found duplicate variable in consecutive steps

    return False, ""  # No duplicate variables found
    


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
                error_msg = f"Feature '{feature}' has duplicate actions between steps {i + 1} and {i + 2}, usually these actions are adjusting the same variable. You can remove either step {i + 1} or step {i + 2} to avoid ambiguity. You only need to include the variable whose value will be assigned dynamically by executing the action. If the action will set the variable to a fixed value, only need to include it in the comment."
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

def format_missing_variables(feature_list, variable_text):
    variable_list = re.findall(r'\bvariable_\w+', variable_text)
    if "variable_input_string" in variable_list:
        variable_list.remove("variable_input_string")
    modelled_variables = [
        step["variable"]
        for feature in feature_list.values()
        for step in feature
        if "variable" in step
    ] + feature_list["null"][0]["missing_variables"]
    # Find variables in variable_list that are not in modelled_variables
    missing_variables = list(set(variable_list) - set(modelled_variables))
    if len(missing_variables) == 0:
        return False, ""
    return True, f"The following variables are not included in any feature step: {missing_variables}. Please refer the user manual again and add these variables in appropriate feature steps, strictly following the user manual description. If any feature cannot be added to any of the features, add this variable in feature_list['null']."
    pass 

def format_input_string(feature_list):
    for feature, steps in feature_list.items():
        for step in steps:
            if "variable" in step and step["variable"] == "variable_input_string":
                return False, f"In feature {feature}, step: {step}, please list the actual variable that is being adjusted. 'variable_input_string' is just for processing the raw input and should not be listed."
    return True, ""

def format_avoid_press_and_hold_actions(feature_list):
    # if a step already has a press action, it should not have a press and hold action.
    # condition to check press action is the string does not contain hold
    # condition to check press_and_hold action is the string contains hold 
    
    for feature, steps in feature_list.items():
        for step in steps:
            if "actions" in step:
                actions = step["actions"]
                if isinstance(actions, list):
                    for action in actions:
                        if "press_and_hold" in action and any("press" in action and "hold" not in action for action in actions):
                            return True, f"Feature '{feature}' has both 'press' and 'press_and_hold' actions. Please move the 'press_and_hold' action to feature['null'], as it likely is used for quickly adjusting the variable. The 'press' action should be used for adjusting the variable one by one."
    return False, ""


def format_action_all_modelled(feature_list, list_of_actions_string):
    list_of_actions = [line.strip() for line in list_of_actions_string.splitlines() if line.strip()]
    #print("list_of_actions", list_of_actions)
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
        return False, f"{error_msg} Missing actions: {set(list_of_actions) - all_feature_actions}. If any action cannot be added to any of the features, add this action in feature_list['null']."
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

def format_contain_empty_actions_or_nonexistant_actions(feature_list_copy, list_of_actions_string):
    feature_list = copy.deepcopy(feature_list_copy)
    feature_list.pop("empty", None)  # Remove the "empty" feature if it exists
    feature_list.pop("null", None)  # Remove the "null" feature if it exists
    #print("list of valid actions: ", list_of_actions_string)
    for feature, steps in feature_list.items():
        #if feature == "null":
        #    continue
        for step in steps:
            if not step["actions"]:  # Check if "actions" is an empty list
                return True, f"Feature '{feature}' contains a step with no actions. Please ensure that this feature step has at least one action."
    
    valid_action_list = [line.strip() for line in list_of_actions_string.splitlines()]

    meta_actions_on_number = ["press_number_1_button", "press_number_2_button", "press_number_3_button", "press_number_4_button", "press_number_5_button", "press_number_6_button", "press_number_7_button", "press_number_8_button", "press_number_9_button", "press_number_0_button"]

    for feature, steps in feature_list.items():
        for step in steps:
            for action in step["actions"]:
                #print(f"feature: {feature}, step: {step}, action: {action}")
                # Check if the action is in meta_actions_on_number but not in valid_action_set
                if action in meta_actions_on_number and action not in valid_action_list:
                    
                    return True, f"Please remove actions involving number pads in feature {feature} because the appliance does not have such actions."
                if not any(action in valid_action for valid_action in valid_action_list):
                    return True, f"Action '{action}' in feature '{feature}' is not a valid action. Please only use actions available in Simulator()."


    # actions can be split into lines 
    # if the actions does not contain numbers but the feature_list contain numbers, report error 
    return False, ""

    pass 
def verify_feature_syntax(feature_list,  list_of_actions_string, ):

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
    contain_error, error_msg = format_different_features_start_with_duplicate_actions(feature_list, mode="agnostic")
    if contain_error:
        print(f"syntax error 4: {error_msg}")
        return False, error_msg
    print("passed syntax check 4")

    # omit this because it cannot put variables to null section
    """
    contain_error, error_msg = format_missing_variables(feature_list, list_of_variables)
    if contain_error:
        print(f"syntax error 5: {error_msg}")
        print("feature_list", feature_list)
        return False, error_msg
    print("passed syntax check 5")
    """

    contain_error, error_msg = format_contain_empty_actions_or_nonexistant_actions(feature_list, list_of_actions_string)
    if contain_error:
        print(f"syntax error 5: {error_msg}")
        print("feature_list", feature_list)
        return False, error_msg
    print("passed syntax check 5")

    contain_error, error_msg = format_consecutive_steps_contain_duplicate_variables(feature_list)
    if contain_error:
        print(f"syntax error 6: {error_msg}")
        return False, error_msg
    print("passed syntax check 6")

    contain_error, error_msg = format_avoid_press_and_hold_actions(feature_list)
    if contain_error:
        print(f"syntax error 7: {error_msg}")
        return False, error_msg
    print("passed syntax check 7")

    # there cannot be empty actions. 
    # the following check is highly error prone, omitting.
    #contain_error, error_msg = format_action_not_missing_variable(feature_list, user_manual_text, verify_feature_list_prompt, define_feature_list_task_prompt_filepath, list_of_variables)
    #if contain_error:
    #    print(f"syntax error 6: {error_msg}")
    #    return False, error_msg
    #print("passed syntax check 6")
    return True, ""
    pass 

def define_feature_list(gpt_model_type,proposed_actions_filepath, proposed_variables_filepath, user_manual_filepath, define_feature_list_task_prompt_filepath, feature_list_filepath, feature_sample_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions_prompt, command_string, verbose=False, use_history= True):
    
    if use_history and os.path.exists(feature_list_filepath):
        print(f"Feature list already exists at {feature_list_filepath}")
        return 
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

    # extract the list of names starting with "variable"

    with open(feature_sample_code_filepath, "r") as f: 
        feature_sample_code = f.read()
    prompt = prompt.replace("hhhhh", feature_sample_code)
    prompt = prompt.replace("uuuuu", command_string)


    with open("temp.txt", "w") as f:
        f.write(prompt)
    trial_rounds = 3
    model = GPT4O()
    error_report = ""
    for i in range(trial_rounds):
        print(f"Attempt {i + 1} to generate valid feature list.")
        del model
        model = GPT4O()
        updated_prompt = prompt + "\n" + error_report
        response = model.chat_with_text(updated_prompt, temperature=1, top_p=1, gpt_model_type = gpt_model_type)
        response = extract_python_code(response)
        with open("temp.txt", "w") as f:
            f.write(prompt)
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

            valid_flag, error_msg = verify_feature_syntax(feature_list, list_of_actions)
            # Check if feature_sequence exists and is not None
            if valid_flag:
                # save response to task list filepath
                with open(feature_list_filepath, "w") as f:
                    f.write(str(response))
                    print(f"Task list saved to {feature_list_filepath}")
                #exit()
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

    print(f"Failed to generate valid feature list after {trial_rounds} attempts.")
    print(response)
    #exit()
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
            #if not ("1_microwave" in dir1 and any(s in dir2 for s in [ "1.txt"])):
            #    continue

            machine_type = dir1.split("/")[-1]
            machine_id = dir2.split("/")[-1].split(".")[0].split("_")[-1]
            print(f"passing by: {machine_type}, {machine_id}")
            
            if machine_type == "_1_microwave" and not any(s in machine_id for s in ["1", "2", "3"]): # "0", "2", "3"
                continue
            if machine_type == "_2_washing_machine" and not any(s in machine_id for s in ["0", "2", "3"]): # "0", "2", "3"
                continue
            if machine_type == "_3_rice_cooker" and not any(s in machine_id for s in ["0", "2", "4"]): 
                continue
            if machine_type == "_4_air_purifier" and not any(s in machine_id for s in ["1", "2", "3"]):
                continue
            if machine_type == "_6_coffee_machine":
                continue
            
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
            define_feature_list(proposed_actions_filepath, proposed_variables_filepath, dir2, define_feature_list_task_prompt_filepath, save_feature_list_filepath, feature_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions)
            #exit()
            
    pass 
if __name__ == "__main__":

    # srun -u -o "log.out" -w crane1 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Generate Policy Template given oracle actions
    #
    #######################################

    oracle_actions_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_3_simulators/_1_oracle_available_actions')
     
    user_manual_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_2_text')

    feature_code_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_2_features.py')
    
    feature_list_for_oracle_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_3_proposed_feature_list_for_oracle_grounding')

    proposed_variables_for_oracle_grounding_dir=os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_0_proposed_variables_for_oracle_grounding')

    define_feature_list_task_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_15_define_feature_list.txt')

    verify_feature_list_prompt = os.path.expanduser('~/TextToActions/code/simulated/prompts/_15_verify_feature_list.txt')
    verify_feature_list_meta_actions_prompt = os.path.expanduser('~/TextToActions/code/simulated/prompts/_15_verify_meta_actions.txt')

    #batch_define_feature_list(oracle_actions_dir, proposed_variables_for_oracle_grounding_dir, user_manual_dir, feature_list_for_oracle_grounding_dir, define_feature_list_task_prompt_filepath, feature_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions_prompt, have_prefix = True)

    #######################################
    #
    # Generate Policy Template (Feature List) given proposed actions
    #
    #######################################

    proposed_actions_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_1_action_names/_1_proposed_action_names')

    proposed_variables_for_proposed_grounding_dir=os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_1_proposed_variables_for_proposed_grounding')

    feature_list_for_proposed_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_4_proposed_feature_list_for_proposed_grounding')

    batch_define_feature_list(proposed_actions_dir, proposed_variables_for_proposed_grounding_dir, user_manual_dir, feature_list_for_proposed_grounding_dir, define_feature_list_task_prompt_filepath, feature_code_filepath, verify_feature_list_prompt, verify_feature_list_meta_actions_prompt)

    
