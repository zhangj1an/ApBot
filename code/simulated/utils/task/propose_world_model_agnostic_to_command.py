
import os
import sys
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.create_or_replace_path import create_or_replace_path
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code
import inspect
import re
import ast 
# for number inputs, the prompt need to modify to add a map string to action. so during search, it is hard to search using astar. instead should find another strategy....

# for action effect, should choose from templates, not generating on its own 

# for action effects on changing variable ranges, should modify the original variable instead of the point of interest. 

# do format check: 
# if self.meta_actions_on_number is existant on the generated code, then the function get_original_input must be present in the object. 


def check_action_effect_conditions(feature_list, code):
    # Step 1: Extract action-to-feature mapping
    action_to_features = {}
    for feature, steps in feature_list.items():
        if feature == "null":
            continue
        for step in steps:
            for action in step["actions"]:
                action_to_features.setdefault(action, set()).add(feature)

    # Step 2: Parse the provided code to extract action effect function conditions
    parsed_code = ast.parse(code)
    action_conditions = {}

    for node in parsed_code.body:
        if isinstance(node, ast.FunctionDef):
            action_name = node.name
            conditions = set()
            for sub_node in ast.walk(node):
                if isinstance(sub_node, ast.Compare):  # Find if-statements checking conditions
                    for operand in sub_node.comparators:
                        if isinstance(operand, ast.Constant) and isinstance(operand.value, str):
                            conditions.add(operand.value)
            action_conditions[action_name] = conditions

    # Step 3: Find missing feature conditions for each action
    error_messages = []
    for action, expected_features in action_to_features.items():
        if action in action_conditions:
            actual_features = action_conditions[action]
            expected_mapped = {feature.replace("_", " ") for feature in expected_features}  # Match naming
            missing_features = expected_mapped - actual_features
            if missing_features:
                error_messages.append(f"Action '{action}': There is no action effects modelled for its related feature: {', '.join(missing_features)}. Please include the action effects for this feature in the '{action}' method.")
        #else:
        #    error_messages.append(f"Action '{action}': there is no explicit condition checks for its related features.")
    
    if len(error_messages) == 0:
        return True, ""
    else:
        return False, "\n".join(error_messages)
    

def check_variable_format_exists(code, combinations):
    """
    Check whether the given variable and feature combinations appear in the code.

    :param code: The Python code as a string.
    :param combinations: List of (variable_name, feature_name) tuples to check.
    :return: A tuple (bool, error_message). False and error message if missing combinations, True and empty string if all exist.
    """
    # Regex pattern to capture variable_name and intended_feature in conditions
    pattern = re.compile(
        r'(?:'
            r'\(\s*variable_name\s*==\s*"([^"]+)"\s*and\s*intended_feature\s*==\s*"([^"]+)"\s*\)'  # variable == X and feature == Y
        r'|'
            r'\(\s*variable_name\s*==\s*"([^"]+)"\s*and\s*intended_feature\s*in\s*\[([^\]]+)\]\s*\)'  # variable == X and feature in [A, B]
        r'|'
            r'\(\s*intended_feature\s*==\s*"([^"]+)"\s*and\s*variable_name\s*==\s*"([^"]+)"\s*\)'  # feature == Y and variable == X
        r'|'
            r'(?:elif|if)\s+variable_name\s*==\s*"([^"]+)"\s*and\s*intended_feature\s*==\s*"([^"]+)"'  # if/elif variable == X and feature == Y
        r'|'
            r'(?:elif|if)\s+variable_name\s*==\s*"([^"]+)"\s*and\s*intended_feature\s*in\s*\[([^\]]+)\]'  # if/elif variable == X and feature in [A, B]
        r')'
    )


    # Find all matches in the code
    matches = pattern.findall(code)

    # Normalize matches to account for both `==` and `in [...]`
    normalized_matches = []

    for match in matches:
        # Flatten the match tuple and remove empty strings
        groups = [g for g in match if g.strip()]

        if len(groups) == 2:
            if "," in groups[1]:  # Feature list case
                variable_name = groups[0]
                feature_list = [f.strip().strip('"') for f in groups[1].split(',')]
                normalized_matches.extend((variable_name, f) for f in feature_list)
            else:
                if groups[0].startswith("variable_"):
                    variable_name, feature = groups
                else:
                    feature, variable_name = groups
                normalized_matches.append((variable_name, feature))

        elif len(groups) == 1:
            # Not enough info, skip
            continue

        elif len(groups) == 3:
            # Likely (variable, "", list of features)
            variable_name, _, feature_list = groups
            features = [f.strip().strip('"') for f in feature_list.split(',')]
            normalized_matches.extend((variable_name, f) for f in features)

        elif len(groups) == 4:
            # Likely (feature, "", "", variable) or other 4-field variants
            # Find the variable and the list of features
            variable_name = next(g for g in groups if g.startswith("variable_"))
            feature_list = next(g for g in groups if not g.startswith("variable_"))
            features = [f.strip().strip('"') for f in feature_list.split(',')]
            normalized_matches.extend((variable_name, f) for f in features)



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
        #print(code)

        #print("\n\n\n")
        #print(matches)
        #exit()
        return False, error_message

    return True, ""

def check_simulator_validity_of_meta_actions(generated_code, given_code, action_list, simulator_type = "Simulator"):
    # if the action list has not meta actions, the simulator should not have meta actions. 

    # this include meta_actions_dict, process_input_string, get_original_input, press_number_button 

    # if the action list has meta actions, the simlator should have meta actions. 

    try:
        namespace = {}
        exec(given_code + "\n" + generated_code , namespace)
        
        

        # Check if the Simulator class is defined
        if simulator_type in namespace:
            simulator_instance = namespace[simulator_type]() 

        if "press_number" not in action_list:
            if hasattr(simulator_instance, 'meta_actions_dict') or hasattr(simulator_instance, 'process_input_string') or hasattr(simulator_instance, 'get_original_input') or hasattr(simulator_instance, 'variable_input_string') or "variable_input_string" in generated_code:
                #print(dir(simulator_instance))
                #exit()
                return False, "The appliance does not have any number pads, so the simulator should not have methods like 'press_number_button', 'get_original_input', 'process_input_string', or variables like 'meta_actions_dict' and 'variable_input_string'. Please remove these methods and variables from the generated code." 
        else:
            if not hasattr(simulator_instance, 'meta_actions_dict') or not hasattr(simulator_instance, 'process_input_string') or not hasattr(simulator_instance, 'get_original_input'):
                return False, "The appliance has number pads, so the simulator should have 'meta_actions_dict', 'process_input_string', and 'get_original_input' methods."
    except Exception as e:
        return False, f"Error during execution: {str(e)}"
    return True, ""

def check_input_string_compatibility(generated_code, given_code, action_list_string):
    # need to find a way to tell whether the variable is included in get_original_input. 
    # so check all the feature list, and if the actions are inside the meta_actions_dict, try a variable name in the get_original_input 
    
    print("checking input string compatibility")
    # Execute the generated code
    try:
        namespace = {}
        exec(given_code + "\n" + generated_code , namespace)
        with open("temp.py", "w") as f:
            f.write(given_code + "\n" + generated_code)
        

        # Check if the Simulator class is defined
        if 'Simulator' in namespace:
            simulator_instance = namespace['Simulator']()  # Instantiate the Simulator object
            print("check 1")
            # Check if `self.meta_actions_dict` exists
            if hasattr(simulator_instance, 'meta_actions_dict'):
                print("check 2")
                print("Simulator has 'meta_actions_dict'.")

                # Check if `get_origianl_input` is a method of Simulator
                if hasattr(simulator_instance, 'variable_input_string') and inspect.ismethod(getattr(simulator_instance, 'get_original_input', None)):
                    print("check 3")
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
                    run_action_fn = getattr(simulator_instance, 'run_action', None)

                    error_msg =  "Since this appliance has variable_input_string, please add the following code chunk in your Simulator class:\n\n" + \
                            "def run_action(self, action_name, execution_times=1, **kwargs):\n" + \
		                    "   if action_name not in meta_actions_dict.values():\n" + \
                            "   self.variable_input_string.input_string = '' \n"
                    if not inspect.ismethod(run_action_fn):
                        return False, error_msg + "place 1"
                    else:
                        try:
                            print("check 4")
                            def contains_input_string_reset(code_str):
                                # Match the definition of run_action and capture its body
                                match = re.search(r'def run_action\(self,.*?\):([\s\S]+?)(?=^def |\Z)', code_str, re.MULTILINE)
                                if match:
                                    body = match.group(1)
                                    pattern = re.compile(r'self\.variable_input_string\.input_string\s*=\s*["\']{2}')
                                    if pattern.search(body):
                                        return True
                                return False
                            if not contains_input_string_reset(generated_code):
                                return False, error_msg + "place 2 (string scan fallback)"
                        except (OSError, TypeError):
                            return False, error_msg + "place 3"
                    try:
                        valid, error_msg = check_variable_format_exists(generated_code, variables_require_input_format)
                        if not valid:
                            return False, error_msg
                    except:
                        
                        return False, f"All the variables that requires meta actions to input values should be included in the 'get_original_input' method of the Simulator class. Note that both the variable name and feature name must exists in the condition in the format: (variable_name == 'variable_name' and intended_feature == 'feature_name')."
                        
                    return True, ""
                else:
                    return False, "The generated code has 'meta_actions_dict' created as a variable, but does not have the required method 'get_origianl_input'. "
            
            # if simulator does not have an attribute called self.variable_input_string, it cannot have a function called process_input_string.
            else:
                if hasattr(simulator_instance, 'variable_input_string') or hasattr(simulator_instance, 'process_input_string') or hasattr(simulator_instance, 'get_original_input'):
                    return False, "The appliance does not have number pads. Please remove the 'self.variable_input_sring', 'process_input_string' and 'get_original_input' method from the generated code."
            return True, ""
        else:
            return False, "Simulator class is not defined in the code."
    except Exception as e:
        return False, f"Error during execution: {str(e)}"
     
def define_world_model(gpt_model_type,proposed_actions_filepath, proposed_variables_filepath, proposed_feature_list_filepath, user_manual_filepath, define_world_model_task_prompt_filepath, saved_world_model_filepath, template_variable_filepath, template_feature_filepath, template_action_filepath, command_string, use_history = True):
    
    # if no feature list, directly return 
    if not os.path.isfile(proposed_feature_list_filepath):
        print("Feature cannot be modelled")
        return 

    if use_history and os.path.exists(saved_world_model_filepath):
        print(f"World model already exists at {saved_world_model_filepath}. Skipping...")
        return 
    
    prompt = ""
    
    with open(define_world_model_task_prompt_filepath, "r") as f:
        prompt = f.read()

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

    # Read feature_list
    feature_ns = {}
    with open(proposed_feature_list_filepath, "r") as f:
        file_content = f.read()
    file_content = template_feature + "\n" + re.sub(r'^simulator_feature.*\n?', '', file_content, flags=re.MULTILINE)
    exec(file_content, feature_ns)
    proposed_feature_list = feature_ns["feature_list"]
    with open(proposed_feature_list_filepath, "r") as f:
        proposed_feature_string = f.read() 
    prompt = prompt.replace("wwwww", str(proposed_feature_list))
    prompt = prompt.replace("uuuuu", command_string)
    
    with open("temp_define_world_model_prompt.txt", "w") as f:
        f.write(prompt)
    
    #print(prompt)
    # load prompt from file

    given_code = template_variable + "\n" + template_feature + "\n" + template_action + "\n" + variable_list + "\n" + proposed_feature_string + "\n"
    model = GPT4O()

    attempt_count = 0
    error_message = ""
    response = ""
    print(response)

    validation_functions = [
        check_input_string_compatibility,
        check_simulator_validity_of_meta_actions,
        check_action_effect_conditions
    ]

    while attempt_count < 5:
        updated_prompt = prompt + f"In your previous attempt, the generated response is:\n {response}\n The following error was found:\n{error_message}\n Please correct these errors."
        print("Attempt to generate world model:", attempt_count)
        
        response = model.chat_with_text(updated_prompt, temperature=0, top_p=1, gpt_model_type=gpt_model_type)
        response = extract_python_code(response)
        with open(f"temp_world_model_{attempt_count}.py", "w") as f:
            f.write(response)
        for validate in validation_functions:
            if validate == check_action_effect_conditions:
                is_ok, error_message = validate(proposed_feature_list, response)
            else:
                is_ok, error_message = validate(response, given_code, action_list)
            #is_ok, error_message = validate(response, given_code, action_list)
            if not is_ok:
                print(error_message)
                error_message = error_message.replace("\n", " ")
                print("Error message: ", error_message)
                break  # Exit validation loop and retry
        else:  # If no errors in any validation function
            with open(saved_world_model_filepath, "w") as f:
                f.write(str(response))
                #exit()
            print(f"Task list saved to {saved_world_model_filepath}")
            break

        attempt_count += 1
        if attempt_count >= 5:
            print(response)
        

def batch_define_world_model(proposed_actions_dir = "/data/home/jian/RLS_microwave/benchmark_2/proposed_actions", proposed_variables_dir="/data/home/jian/RLS_microwave/benchmark_2/user_manual_variable_list", proposed_feature_list_dir="/data/home/jian/RLS_microwave/benchmark_2/user_manual_feature_list", user_manual_dir = "/data/home/jian/RLS_microwave/benchmark_2/user_manual_extracted_text_gpt4o", define_world_model_task_prompt_filepath = "/data/home/jian/RLS_microwave/utils/_5_build_world_model/prompts/define_world_model.txt", save_world_model_dir="/data/home/jian/RLS_microwave/benchmark_2/proposed_world_model", template_variable_filepath="", template_feature_filepath="", template_action_filepath="", have_prefix = True):   
    machine_type_dirs = [os.path.join(user_manual_dir, d) for d in os.listdir(user_manual_dir) if os.path.isdir(os.path.join(user_manual_dir, d))]
    

    # Washing machine: 0, 2, 3
    # Rice cooker: 0, 2, 4 || 0, 4
    # Air purifier: 1, 2, 3 || 1, 2

    
    for dir1 in machine_type_dirs:
        # List all subdirectories in each level one directory
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith(('.txt'))]
        for dir2 in machine_id_dirs:
            if not ("_1_microwave" in dir1 and any(s in dir2 for s in ["2.txt"])):
                continue
            
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

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Create World Model for oracle actions
    #
    #######################################
    oracle_actions_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_3_simulators/_1_oracle_available_actions')
    
    user_manual_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_2_text')
    
    define_world_model_task_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_16_define_world_model.txt')

    proposed_variables_for_oracle_grounding_dir=os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_0_proposed_variables_for_oracle_grounding')

    proposed_feature_list_for_oracle_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_3_proposed_feature_list_for_oracle_grounding')
    
    save_world_model_for_oracle_grounding_dir=os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_6_proposed_world_model_for_oracle_grounding')

    template_variable_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_1_variables.py')
    template_feature_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_2_features.py')
    template_action_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_3_actions.py')

    #batch_define_world_model(oracle_actions_dir, proposed_variables_for_oracle_grounding_dir, proposed_feature_list_for_oracle_grounding_dir, user_manual_dir, define_world_model_task_prompt_filepath, save_world_model_for_oracle_grounding_dir, template_variable_filepath, template_feature_filepath, template_action_filepath, have_prefix= True)

    #######################################
    #
    # Create World Model for proposed actions
    #
    #######################################

    proposed_actions_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_1_action_names/_1_proposed_action_names')

    proposed_variables_for_proposed_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_1_proposed_variables_for_proposed_grounding')

    proposed_feature_list_for_proposed_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_4_proposed_feature_list_for_proposed_grounding')

    save_world_model_for_proposed_grounding_dir=os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_7_proposed_world_model_for_proposed_grounding')

    batch_define_world_model(proposed_actions_dir, proposed_variables_for_proposed_grounding_dir, proposed_feature_list_for_proposed_grounding_dir, user_manual_dir, define_world_model_task_prompt_filepath, save_world_model_for_proposed_grounding_dir, template_variable_filepath, template_feature_filepath, template_action_filepath,)


    