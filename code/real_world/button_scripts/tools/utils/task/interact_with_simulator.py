
# perfect grounding: no need remap actions 

# proposed grounding: need to remap actions 

import sys 
import os 
import json 
import copy
import re 
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.extract_python_code import extract_python_code
from simulated.utils.task.prepare_simulator import load_oracle_generated_and_goal_simulator

def parse_action(action_string):

    pattern = r"run_action\s*\(\s*'([^']+)'\s*(?:,\s*execution_times\s*=\s*(\d+))?\s*(?:,\s*duration\s*=\s*(\d+))?\s*\)"
    match = re.match(pattern, action_string)
    
    if match:
        action_name = match.group(1)
        execution_times = int(match.group(2)) if match.group(2) else 1  # Default to 1 if not provided
        duration = int(match.group(3)) if match.group(3) else None 
        return action_name, execution_times, duration
    else:
        raise ValueError(f"Invalid action string format: {action_string}")


def match_generated_world_model_actions_to_simulator_actions(input_action_name, mapping_filepath, setting = "action", verbose=False):

    if mapping_filepath == '':
            return input_action_name
        
    # load the mapping dict as a dict from json
    with open(mapping_filepath, "r") as f:
        mapping = json.load(f)

        
    if setting == "action":     
        # if the input action name is in the dict, output the result, otherwise output None 
        for proposed_action in mapping.keys():
            #print("proposed_action: ", proposed_action)
            a = proposed_action in input_action_name
            #print("condition: ", a)
            if proposed_action in input_action_name:
                target = mapping[proposed_action]

                # out of all options, map the closest action to the input action name

                if len(target) > 0:
                    response = input_action_name.replace(proposed_action, target[0])
                    if verbose:
                        print(f"proposed action: {proposed_action},\ngrounded action: {response}")
                    
                    return response
                else:
                    print(f"proposed action: {proposed_action},\n cannot find any grounded action")
                    return None
        print(f"proposed action: {input_action_name},\n cannot find any grounded action")
        return None
    elif setting == "button":
        # input_action_name = (action_type, bbox_index)
        action_type = input_action_name[0]
        bbox_index = input_action_name[1]
        if isinstance(bbox_index, int):
            if str(bbox_index) not in mapping:
                print(f"proposed action: {input_action_name},\n cannot find any grounded action")
                return None 
            bbox_dict = mapping[str(bbox_index)] 
        elif isinstance(bbox_index,(list, tuple)) and len(bbox_index) == 2:
            index_key = f"{bbox_index[0]}_{bbox_index[1]}"
            if index_key not in mapping:
                print(f"proposed action: {input_action_name},\n cannot find any grounded action")
                return None
            bbox_dict = mapping[index_key]
        else:
            return None
        
        if action_type in bbox_dict["actions"]:
            action_name = bbox_dict["actions"][action_type]
            print(f"proposed action: {input_action_name},\ngrounded action: {action_name}") 
            return action_name
        else:
            print(f"proposed action: {input_action_name},\n cannot find any grounded action")
            return None
        pass 
    
    
    #exit()


def interact_with_appliance_simulator(simulator, action, mapping_filepath, setting = "action", verbose = False):
    # returns: simulator, termination_flag, current_observation, grounded_action
    execution_times = None 
    duration = None
    action_name = None
    
    #print("action in interact with appliance simulator: ", action)
    #print("setting in interact with appliance simulator: ", setting)
    if setting == "action":
        response_string, execution_times, duration = None, None, None
        if isinstance(action, tuple):
            response_string = action[0]
            execution_times = action[1]
            if len(action) == 3:
                duration = action[2]
        elif isinstance(action, str):
            
            response_string, execution_times, duration = parse_action(action)
    elif setting == "button":
        action_type = action[0]
        bbox_index = action[1]
        response_string = (action_type, bbox_index)
        execution_times = action[2]
        if len(action) == 4:
            duration = action[3] 
    
    #print(f"in interact with appliance simulator, response_string: {response_string}, execution_times: {execution_times}, duration: {duration}")
    #print(f"response_string in interaction: {response_string}, execution_times: {execution_times}", flush=True)
    copy_simulator = copy.deepcopy(simulator)

    if setting == "action":
        if mapping_filepath != '':
            #print("response_string in interaction: ", response_string)
            action_name = match_generated_world_model_actions_to_simulator_actions(response_string, mapping_filepath, setting = "action", verbose = verbose)
        else:
            action_name = response_string

    elif setting == "button" and mapping_filepath != '':
        action_name = match_generated_world_model_actions_to_simulator_actions(response_string, mapping_filepath, setting = "button", verbose = verbose)

    
    #print(f"Grounded action in interaction: ({action_name}, {execution_times})")
    
    if action_name is None:
        error_message = "No action taken. The suggested action is not executable, The task cannot be completed"
        #print(error_message)
        return copy_simulator, True, error_message, "No action taken"
    
    if action_name == "end":
        
        return copy_simulator, True, "No action taken", "end"
    
    
    
    if duration is not None:
        current_observation = copy_simulator.run_action(action_name, execution_times, duration = duration)
    else:
        current_observation = copy_simulator.run_action(action_name, execution_times)
    # Create a dictionary for the local namespace
    
    if verbose:
        print(f"###################")
        print(f"actual executed action:{action_name}")
        print(f"current_observation: ", current_observation)
   
    return copy_simulator, False, current_observation, action_name


def interact_with_user_manual_simulator(simulator, action, verbose = False):

    response_string, execution_times, duration = None, None, None
    if isinstance(action, tuple):
        response_string = action[0]
        execution_times = action[1]
        if len(action) == 3:
            duration = action[2]
    elif isinstance(action, str):
        response_string, execution_times, duration = parse_action(action)
    
    #print(f"response_string in interaction: {response_string}, execution_times: {execution_times}")
    copy_simulator = copy.deepcopy(simulator)

    try:
        if duration is not None:
            current_observation = copy_simulator.run_action(response_string, execution_times, duration = duration)
        else:
            current_observation = copy_simulator.run_action(response_string, execution_times)
    
        #current_observation = copy_simulator.run_action(response_string, execution_times)
        if verbose:
            print(f"Action executed successfully: action_name={response_string}, execution_times={execution_times}")
        return copy_simulator, "", False # termination flag
    except Exception as e:
        print(f"Error during action execution in user manual: {str(e)}")
        if verbose:
            print(f"Error during action execution: {str(e)}")
        return copy_simulator, f"Error: {str(e)}", True 

    # returns: simulator, current observation (no need) 
    pass 

def compress_planning_result(lst):
    if not lst:
        return []
    
    compressed_list = []
    current_item = lst[0]
    count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == current_item:
            count += 1
        else:
            compressed_list.append((current_item, count))
            current_item = lst[i]
            count = 1
    
    # Add the last item
    compressed_list.append((current_item, count))
    
    return compressed_list


def execute_action(current_action, appliance_simulator, current_state_simulator,  grounding_mapping_filepath, step_index, execution_history, feedbacks, verbose):

    appliance_simulator, current_state_simulator, feedback, user_manual_appliance_error_message, grounded_action, termination_flag = execute_action_and_get_feedback(current_action, appliance_simulator, current_state_simulator,  grounding_mapping_filepath, verbose) 
    
    step_index += 1
    current_step_record = {}
    current_step_record["step_index"] = step_index
    current_step_record["proposed_action"] = current_action
    current_step_record["grounded_action"] = grounded_action
    current_step_record["current_observation"] = feedback
    

    if user_manual_appliance_error_message!="" :
        # the user manual is faulty. may need to resolve to llm agents 
        print(f"Our modelling of the user manual is faulty. error message: {user_manual_appliance_error_message}. Possibly resort to LLM agents.")
        current_step_record["error_message"] = user_manual_appliance_error_message

    if termination_flag:
        print("action is not grounded, terminating the loop.")
        current_step_record["error_message"] = "proposed action can not be grounded, has visual grounding faults."

    execution_history.append(current_step_record)
    feedbacks.append(f"applied action: {current_action}, feedback: {feedback}")

    return step_index, appliance_simulator, current_state_simulator, termination_flag, execution_history, feedbacks 
    pass 

def execute_action_and_get_feedback(current_action, appliance_simulator, current_state_simulator, grounding_mapping_filepath, verbose = False):
    # currently because the generated code is 100% correct so no need to translate actions
    #print("in execute action and get feedback, proposed action: ", current_action)
    appliance_simulator, termination_flag_oracle, feedback, grounded_action = interact_with_appliance_simulator(appliance_simulator, current_action, grounding_mapping_filepath)
    
    if verbose:
        print(f"action: {current_action}, feedback: {feedback}")

    current_state_simulator, error_message, termination_flag_proposed = interact_with_user_manual_simulator(current_state_simulator, current_action)

    termination_flag = termination_flag_oracle or termination_flag_proposed
    
    #print("oracle termination flag: ", termination_flag_oracle)
    #print("proposed termination flag: ", termination_flag_proposed)
    return appliance_simulator, current_state_simulator, feedback,  error_message, grounded_action, termination_flag 


def revert_to_previous_state_for_oracle_simulator(past_actions, oracle_appliance_code, grounding_mapping_filepath, verbose = False):
    oracle_globals = {}
    exec(oracle_appliance_code, oracle_globals)
    ApplianceSimulator = oracle_globals.get('Oracle', None)
    appliance_simulator = ApplianceSimulator()
    feedbacks = [] 
    for action in past_actions:
        appliance_simulator, termination_flag, feedback, grounded_action = interact_with_appliance_simulator(appliance_simulator, action, grounding_mapping_filepath)
        if isinstance(action, str):
            pure_action, execution_times, duration = parse_action(action)
        else: 
            pure_action = action[0]
        feedbacks.append(f"applied action: {pure_action}, feedback: {feedback}")
    if len(feedbacks) > 0:
        return appliance_simulator, feedbacks[-1]
    else:
        return appliance_simulator, []
    # Execute generated_appliance_code in its own dictionary

    pass 

def revert_to_previous_state(past_actions, oracle_appliance_code, generated_appliance_code, generated_goal_code, step_index, grounding_mapping_filepath, execution_history, setting="agnostic", verbose = False):

    appliance_simulator, current_state_simulator, goal_state_simulator, feature_sequence, AStarSearch = load_oracle_generated_and_goal_simulator(oracle_appliance_code, generated_appliance_code, generated_goal_code, setting)
    feedbacks = []
    
    if verbose:
        print("reverting to previous state!!!")
        print("all past actions: ", past_actions)
    
    for action in past_actions:
        step_index, appliance_simulator, current_state_simulator, termination_flag, execution_history, feedbacks = execute_action(action, appliance_simulator, current_state_simulator, grounding_mapping_filepath, step_index, execution_history, feedbacks, verbose = False)
        if verbose:
            print(f"after apply action {action}\n, the state of the user manual simulator is: \n {current_state_simulator}\n {current_state_simulator.get_current_value()}")
    #exit()
        

    return appliance_simulator, current_state_simulator, goal_state_simulator, feedbacks, step_index, execution_history

def obtain_debug_record_for_oracle_simulator(action, appliance_simulator, grounding_mapping_filepath, verbose = False):
    if isinstance(action, tuple):
        response_string = action[0]
        execution_times = action[1]
        if len(action) == 3:
            duration = action[2]
    elif isinstance(action, str):
        response_string, execution_times, duration = parse_action(action)

    debug_record = []
    for i in range(100):

        appliance_simulator, termination_flag, feedback, grounded_action = interact_with_appliance_simulator(appliance_simulator, (response_string, 1), grounding_mapping_filepath)
        debug_record.append(f"applied action: {response_string}, feedback: {feedback}") 
        if debug_record[-1] in debug_record[:-1]:
            break

    if verbose:
        print("added all debug record.\n\n\n")
        print(debug_record)
    return debug_record, appliance_simulator
    pass 
def obtain_debug_record(action, appliance_simulator, current_state_simulator, grounding_mapping_filepath, step_index, execution_history, verbose = False):
    # format: ('press_program_button', 4)
    print(f"current_action: {action}")

    if isinstance(action, tuple):
        response_string = action[0]
        execution_times = action[1]
        if len(action) == 3:
            duration = action[2]
    elif isinstance(action, str):
        response_string, execution_times, duration = parse_action(action)

    # keep trying until the feedback has been observed before.
    #execution_times = max(20, execution_times)
    debug_record = []
    for i in range(100):
        step_index, appliance_simulator, current_state_simulator, termination_flag, execution_history, debug_record = execute_action((response_string, 1), appliance_simulator, current_state_simulator, grounding_mapping_filepath, step_index, execution_history, debug_record, verbose)
        if debug_record[-1] in debug_record[:-1]:
            break

    if verbose:
        print("added all debug record.\n\n\n")
        print(debug_record)
    return debug_record, execution_history, step_index 


if __name__ == "__main__":
    # test the function interact_with_appliance_simulator
    action = "run_action('press_time_cook_button', execution_times=1)"
    result = parse_action(action)
    print(result)
