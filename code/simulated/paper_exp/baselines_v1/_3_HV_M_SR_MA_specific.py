# every command generate a different reasoning file? seems no need to do so. 
# should i follow the feature or directly generate button policy?
# if mismatch: retain previous records, start from now and only analyse using now. 
# maybe this version will be better?  

import os
import sys
import json
import textwrap
import copy 
import re

import shutil
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.load_string_from_file import load_string_from_file, load_string_from_files
from simulated.utils.extract_python_code import extract_python_code
from simulated.utils.extract_list_from_file import extract_list_from_file
from simulated.utils.create_or_replace_path import create_or_replace_path
from simulated.utils.task.derive_variable_definition import analyze_continuous_sequence, analyze_discrete_sequence
from simulated.utils.task.generate_score import generate_score
from simulated.utils.task.interact_with_simulator import interact_with_appliance_simulator, compress_planning_result, execute_action
from simulated.utils.task.matches_run_action_format import matches_run_action_format
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.task.propose_actions import propose_action
from simulated.utils.task.propose_variables import extract_control_panel_labels, define_variables
from simulated.utils.task.propose_feature_list import define_feature_list
from simulated.utils.task.propose_world_model_agnostic_to_command import define_world_model 
from simulated.utils.task.propose_world_model_specific_to_command import generate_world_model_specific_to_command
from simulated.utils.task.replace_placeholder_in_filepaths import replace_placeholder_in_filepaths
from simulated.utils.task.propose_goal_state import generate_goal_state
from simulated.utils.task.prepare_simulator import prepare_oracle_simulator, prepare_generated_simulator, load_oracle_generated_and_goal_simulator, load_generated_code
from simulated.utils.task.check_state_reached import check_state_reached
from simulated.utils.task.interact_with_simulator import revert_to_previous_state, obtain_debug_record
from simulated.utils.task.calibrate_current_value import calibrate_current_value
from simulated.utils.task.generate_updated_goal import generate_updated_goal
from simulated.utils.task.check_reasoning_file_existance import check_reasoning_file_existance
# assume the perception is done first, merge later 
# in one go, propose variable, feature list and world model, and task-specific model, goal state, and run. 

# here already have code. 

# 
# firstly generate variables, features and action effects. 

def test_one_appliance_type(gpt_model_type,appliance_type, instance_info_filepaths, reasoning_filepaths,  template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, selected_machine_id,  selected_testcase_difficulty, selected_question_id, verbose = False, mode = "batch"):

    appliance_ids = os.listdir(os.path.dirname(instance_info_filepaths["oracle_appliance_code_filepath"]))
    appliance_ids = sorted([f[:-3].split("_")[-1] for f in appliance_ids if re.fullmatch(r'_\d\.py', f)])
    
    # observations_dir, control_panel_element_names_filepath, control_panel_label_details_filepath,
    filepaths = {
        "instance_info_filepaths": instance_info_filepaths,
        "reasoning_filepaths": reasoning_filepaths,
        "testcase_input_filepaths": testcase_input_filepaths,
        "output_filepaths": output_filepaths,
    }

    for appliance_id in appliance_ids:
        updated_filepaths = replace_placeholder_in_filepaths(filepaths, "yyyyy", appliance_id)
        if mode == "test" and selected_machine_id != "":
            if appliance_id != selected_machine_id:
                continue
        test_one_appliance_instance(gpt_model_type,
            appliance_type, appliance_id, updated_filepaths["instance_info_filepaths"], updated_filepaths["reasoning_filepaths"], template_code_filepaths,
            updated_filepaths["testcase_input_filepaths"], updated_filepaths["output_filepaths"],
            prompt_filepaths,
            trial_rounds_per_testcase,  selected_testcase_difficulty, selected_question_id, verbose=verbose, mode = mode
        ) 

def test_all_appliance_types(gpt_model_type,
instance_info_filepaths, reasoning_filepaths, template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, selected_machine_type, selected_machine_id, selected_testcase_difficulty, selected_question_id, verbose = False, mode = "batch"):

    parent_dir = os.path.dirname(os.path.dirname(oracle_appliance_code_filepath))
    appliance_types = os.listdir(parent_dir)
    
    filepaths = {
        "instance_info_filepaths": instance_info_filepaths,
        "reasoning_filepaths": reasoning_filepaths, 
        "testcase_input_filepaths": testcase_input_filepaths,
        "output_filepaths": output_filepaths,
    }

    for appliance_type in appliance_types:
        updated_filepaths = replace_placeholder_in_filepaths(filepaths, "xxxxx", appliance_type)
        if mode == "test" and selected_machine_type != "":
            if appliance_type != selected_machine_type:
                continue
        test_one_appliance_type(gpt_model_type,
            appliance_type, 
            updated_filepaths["instance_info_filepaths"], updated_filepaths["reasoning_filepaths"], template_code_filepaths,
            updated_filepaths["testcase_input_filepaths"], updated_filepaths["output_filepaths"],
            prompt_filepaths,
            trial_rounds_per_testcase, selected_machine_id, selected_testcase_difficulty, selected_question_id, verbose=verbose, mode= mode
        )

def test_one_appliance_instance_multiple_testcases(gpt_model_type,appliance_type, appliance_id, testcase_difficulty, reasoning_filepaths,  user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath,testcase_input_filepath, testcases_result_filepaths, prompt_filepaths,grounding_mapping_filepath, trial_rounds_per_testcase, selected_question_id, verbose = False, mode = "batch"):

    # update world model specific to command.
    # update goal state. 
    # then propose   

    testcase_info_list = extract_list_from_file(testcase_input_filepath) 
    testcases_info = sorted(testcase_info_list, key=lambda x: x['id']) 
    for testcase_info in testcases_info:
        question_id = str(testcase_info["id"])
        if mode == "test" and selected_question_id != "":
            if question_id != selected_question_id:
                continue
        # testcase_difficulty : ["easy", "hard", "ambi"]:
        # appliance_type: ["_1_microwave", "_2_washing_machine", "_3_rice_cooker", "_4_air_purifier"]
        # appliance_id : ["1", "2", "3", "4", "5"]
        # question_id : ["1", "2", "3", "4", "5"]

        # Microwave: 1, 2, 3 || 0, 4
        # Washing machine: 0, 2, 3 || 
        # Rice cooker: 0, 2, 4 || 0, 2
        # Air purifier: 1, 2, 3 || 0, 4

        if (testcase_difficulty == "easy" and appliance_type == "_1_microwave" and appliance_id in ["0"] and question_id in ["1"]):#["2", "3", "4", "5"]):# ["2", "3", "4", "5"]):# 
            #print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
            continue
        print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
        testcases_result_filepaths_specific = replace_placeholder_in_filepaths(testcases_result_filepaths, "zzzzz", question_id)
        test_one_single_testcase_multiple_trials(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths, user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath,testcase_info, testcases_result_filepaths_specific,prompt_filepaths, grounding_mapping_filepath,  trial_rounds_per_testcase, verbose = verbose)
        
def test_one_single_testcase_multiple_trials(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath,testcase_info, testcases_result_filepaths,prompt_filepaths, grounding_mapping_filepath, trial_rounds_per_testcase, verbose = False):

    print("processing: ", appliance_type, appliance_id, question_id)
    for i in range(trial_rounds_per_testcase):
        print("trial: ", i+1)
        updated_testcases_result_filepaths = replace_placeholder_in_filepaths(testcases_result_filepaths, "wwwww", str(i+1))
        test_one_single_testcase_single_trial(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath,testcase_info, updated_testcases_result_filepaths, prompt_filepaths, grounding_mapping_filepath, verbose = verbose)
        
    #exit()



def test_one_appliance_instance(gpt_model_type,appliance_type, appliance_id, instance_info_filepaths, reasoning_filepaths, template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, selected_testcase_difficulty, selected_question_id, verbose = False, mode = "batch"):

    # for one appliance instance, extract its labels, variables, actions, world model. 
    control_panel_label_details_filepath = reasoning_filepaths["control_panel_label_details"]
    
    user_manual_filepath = instance_info_filepaths["user_manual_filepath"]
    action_option_filepath = instance_info_filepaths["action_option_filepath"]
    oracle_appliance_code_filepath = instance_info_filepaths["oracle_appliance_code_filepath"]
    grounding_mapping_filepath = instance_info_filepaths["grounding_mapping_filepath"]

    print("reasoning filepaths: ", reasoning_filepaths)
    #exit()
    extract_control_panel_labels(gpt_model_type,instance_info_filepaths["observations_dir"], appliance_type, appliance_id, control_panel_label_details_filepath,instance_info_filepaths["control_panel_element_names_filepath"],  use_history = True )

    easy_testcase_output_filepaths = replace_placeholder_in_filepaths(output_filepaths, "hhhhh", "_1_easy_testcases")
    hard_testcase_output_filepaths = replace_placeholder_in_filepaths(output_filepaths, "hhhhh", "_2_hard_testcases")
    ambiguous_testcase_output_filepaths = replace_placeholder_in_filepaths(output_filepaths, "hhhhh", "_3_ambiguous_testcases")

    if mode == "batch" or selected_testcase_difficulty == "":

        test_one_appliance_instance_multiple_testcases(gpt_model_type,appliance_type, appliance_id, "easy", reasoning_filepaths, user_manual_filepath,  action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath,testcase_input_filepaths["easy_testcase_input_filepath"], easy_testcase_output_filepaths, prompt_filepaths, grounding_mapping_filepath, trial_rounds_per_testcase, selected_question_id, verbose =verbose, mode=mode)
        test_one_appliance_instance_multiple_testcases(gpt_model_type,appliance_type, appliance_id, "hard",  reasoning_filepaths,user_manual_filepath,action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath,testcase_input_filepaths["hard_testcase_input_filepath"], hard_testcase_output_filepaths, prompt_filepaths,grounding_mapping_filepath,  trial_rounds_per_testcase, selected_question_id, verbose= verbose, mode=mode)
        test_one_appliance_instance_multiple_testcases(gpt_model_type,appliance_type, appliance_id, "ambi",  reasoning_filepaths,user_manual_filepath, action_option_filepath,oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath,testcase_input_filepaths["ambiguous_testcase_input_filepath"], ambiguous_testcase_output_filepaths, prompt_filepaths, grounding_mapping_filepath,  trial_rounds_per_testcase, selected_question_id, verbose = verbose,mode=mode) 
    else:
        test_one_appliance_instance_multiple_testcases(gpt_model_type,appliance_type, appliance_id, selected_testcase_difficulty, reasoning_filepaths, user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths,control_panel_label_details_filepath, testcase_input_filepaths[selected_testcase_difficulty+"_testcase_input_filepath"], easy_testcase_output_filepaths, prompt_filepaths, grounding_mapping_filepath, trial_rounds_per_testcase, selected_question_id, verbose = verbose, mode = mode)




def test_one_single_testcase_single_trial(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths, user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, control_panel_label_details_filepath, testcase_info, testcases_result_filepaths, prompt_filepaths,grounding_mapping_filepath, verbose = False):


    command_string = testcase_info["command"]

    proposed_variables_filepath = testcases_result_filepaths["proposed_variables"]
    proposed_features_filepath = testcases_result_filepaths["proposed_features"]
    updated_variables_filepath =testcases_result_filepaths["updated_variables"]
    updated_world_model_filepath = testcases_result_filepaths["updated_world_model"]
    updated_goal_state_filepath = testcases_result_filepaths["updated_goal_state"]

    
    define_variables(gpt_model_type,action_option_filepath, user_manual_filepath, control_panel_label_details_filepath, prompt_filepaths["define_variables"], template_code_filepaths[1], proposed_variables_filepath, command_string, use_history = True)
    
    define_feature_list(gpt_model_type,action_option_filepath, proposed_variables_filepath, user_manual_filepath, prompt_filepaths["define_feature_list"], proposed_features_filepath, template_code_filepaths[2], prompt_filepaths["verify_feature_list"], prompt_filepaths["verify_meta_actions"], command_string,verbose, use_history = True)
    #exit()
    # define world model agnostic to the command. 
    define_world_model(gpt_model_type,action_option_filepath, proposed_variables_filepath, proposed_features_filepath, user_manual_filepath, prompt_filepaths["define_world_model"], testcases_result_filepaths["proposed_world_model"], template_code_filepaths[1], template_code_filepaths[2], template_code_filepaths[3], command_string, use_history = True)
    #exit()

    log_record_filepath = testcases_result_filepaths["log_record"]
    raw_output_filepath = testcases_result_filepaths["raw_output"]

    log_record = {}
    log_record["command_id"] = testcase_info["id"]
    log_record["command_string"] = command_string
    log_record["ground_truth_goal_state"] = testcase_info["important_target_states"] 
    execution_history = []

    # if the given file does not exists, directly return zero. 
    generated_code_filepaths = [testcases_result_filepaths["proposed_variables"], testcases_result_filepaths["proposed_features"], testcases_result_filepaths["proposed_world_model"]]
    if not check_reasoning_file_existance(generated_code_filepaths, log_record, log_record_filepath):
        return
    
    #generate_world_model_specific_to_command(gpt_model_type,prompt_filepaths,action_option_filepath, reasoning_filepaths, template_code_filepaths[1:], testcases_result_filepaths, user_manual_filepath, command_string, use_history = True)

    
    #if not check_reasoning_file_existance([testcases_result_filepaths["world_model_specific_to_command"]], log_record, log_record_filepath):
        return 
    
    # if the world model file does not exists, return zero.
    generate_goal_state(gpt_model_type,prompt_filepaths["generate_goal_state"], testcases_result_filepaths["goal_state"], template_code_filepaths[1:], generated_code_filepaths, command_string, user_manual_filepath, "", use_history = True) 
    
    if not check_reasoning_file_existance([testcases_result_filepaths["goal_state"]], log_record, log_record_filepath):
        return 
    
    oracle_appliance_code = prepare_oracle_simulator(template_code_filepaths[1:], oracle_appliance_code_filepath)
    
    generated_appliance_code, generated_files = prepare_generated_simulator(template_code_filepaths[0], generated_code_filepaths, testcases_result_filepaths, setting = "specific") 
    
    appliance_simulator, current_state_simulator, goal_state_simulator, feature_sequence, AStarSearch = load_oracle_generated_and_goal_simulator(oracle_appliance_code, generated_appliance_code, setting = "specific")


    initial_state_string = str(appliance_simulator)
    print("initial appliance state: ", initial_state_string)
    print(f"\ncurrent_state_simulator when it is just created: \n\n {current_state_simulator}")
    print("\ngoal state: ", goal_state_simulator)

    actions = [action for action in dir(current_state_simulator) if action.startswith(('press_', 'turn_')) and callable(getattr(current_state_simulator, action))]
    feature_list = current_state_simulator.feature.feature_list 

    step_index = 0 
    past_actions = []
    reached_goal = None 
    has_error = False  

    ############################
    # required outputs:      
    # log record: 
    #       index, proposed action, reasoning, grounded action, current observation, mismatch? if mismatch.
    # 
    # > < 
    # 
    #  
    for feature_progress_index in range(len(feature_sequence)):
        if has_error == True:
            break 
        current_feature = feature_sequence[feature_progress_index]
        print("current feature: ", current_feature)
        current_feature_info = feature_list[current_feature]

        subgoal_simulator = copy.deepcopy(current_state_simulator)
        feedbacks = []
        
        for step_info in current_feature_info:
            if has_error:
                break 
            print("step_info: ", step_info)
            current_action = step_info["actions"][0]
            current_action = (current_action, 1)
            # if it is a number action, skip this step 
            if (not hasattr(current_state_simulator, "meta_actions_dict")) or (current_action[0] not in current_state_simulator.meta_actions_dict.values()):
                print(f"executing action: {current_action}")

                step_index, appliance_simulator, current_state_simulator, has_error, execution_history, feedbacks = execute_action(current_action, appliance_simulator, current_state_simulator, grounding_mapping_filepath, step_index, execution_history, feedbacks, verbose) 
                past_actions.append(current_action)

                if has_error:
                    print("has error")
                    break
                
                
            # if at the step the goal is already fulfilled, then should still execute the action because the step is not skippable. 
            if "variable" not in step_info:
                continue 

            modified_code_attempt = 0 
            reached_goal = False 
            allowed_modification_trials = 2
            while not reached_goal:
                
                if has_error:
                    break

                variable_name = step_info["variable"]
                subgoal_variable = goal_state_simulator.get_variable_by_name(variable_name)
                subgoal_variable_value = goal_state_simulator.get_variable_value(variable_name)
                goal_state_string = f"We want to have the variable: {variable_name} to have a value of {subgoal_variable_value}. "
                setattr(subgoal_simulator, variable_name, subgoal_variable)

                if subgoal_variable is None:
                    print(f"variable {variable_name} is not in the simulator attributes, this should not happen, code has bug, return error")
                    break

                actions = step_info["actions"]

                # here check for mismatch. other places do not need to check for mismatch.
                reached_goal = None 

                print(f"goal_state_simulator: {subgoal_simulator}")
                print(f"current_state_simulator: {current_state_simulator}")
                print(f"variable_name: {variable_name}")
                print(f"actions: {actions}")
                print(f"astarsearch: {AStarSearch}")
                astar = AStarSearch(current_state_simulator, subgoal_simulator, actions, [variable_name], current_feature, verbose=False)
                planning_result = astar.search()
                planning_result = compress_planning_result(planning_result)
                print("planning_result: ", planning_result)

                if planning_result is None:
                    reached_goal = False
                    has_error = True 
                    print(f"planning failed, generated flawed transition dynamics")
                    current_step_record = {}
                    current_step_record["step_index"] = step_index
                    current_step_record["error_message"] = "planning failed, generated model has flawed transition dynamics"
                    execution_history.append(current_step_record)
                    break
                    

                before_action_state = str(current_state_simulator)
                
                if len(planning_result) > 0:
                    for current_action in planning_result: 
                        step_index, appliance_simulator, current_state_simulator, has_error, execution_history, feedbacks = execute_action(current_action, appliance_simulator, current_state_simulator, grounding_mapping_filepath, step_index, execution_history, feedbacks, verbose)

                        if has_error:
                            continue                   
                    
                if len(feedbacks) > 3:
                    feedbacks = feedbacks[-3:]
                print("feedbacks: ", feedbacks)
                #print("current actual appliance state: ", str(appliance_simulator))
                reached_goal, reached_goal_details = check_state_reached(gpt_model_type,prompt_filepaths["decide_mismatch"], template_code_filepaths[1:] + generated_files, prompt_filepaths["distill_feedback"], goal_state_string, feedbacks[-1], command_string, verbose = False) # verbose
                #print("state reached: ", reached_goal)
                
                #exit()
                if reached_goal:
                    if len(planning_result) > 0:
                        past_actions += planning_result
                if not reached_goal:
                    print("detecting mismatch!!")
                    execution_history[-1]["mismatch"] = reached_goal_details

                    if modified_code_attempt > allowed_modification_trials:
                        print(f"modify code more than {allowed_modification_trials} times, return error")
                        break
                    generated_appliance_code = load_generated_code(generated_files, setting = "specific")
                    appliance_simulator, current_state_simulator, goal_state_simulator, debug_record, _, _, = revert_to_previous_state(past_actions, oracle_appliance_code, generated_appliance_code, 0, grounding_mapping_filepath, [], setting="specific")
                    print("currently, here are the past actions taken: ", past_actions, flush=True)   
                    debug_record_last_step, _, _, = obtain_debug_record(current_action, appliance_simulator, current_state_simulator, grounding_mapping_filepath, 0, [], verbose = False)
                    
                    if len(debug_record) > 1:
                        debug_record = [debug_record[-1]]
                    debug_record += debug_record_last_step
                    
                    calibration_successful = calibrate_current_value(gpt_model_type,prompt_filepaths["calibrate_current_value"], variable_name, debug_record, prompt_filepaths["define_variables"], template_code_filepaths[1:], generated_files[:3], str(current_action), before_action_state, goal_state_string, execution_history[-1]["current_observation"],prompt_filepaths["generate_record_sequence"], prompt_filepaths["correct_world_model"], "temp_generated_variable.py", "temp_generated_world_model.py", verbose = False)
                    
                    if calibration_successful: 
                         
                        # update goal 

                        original_goal_code = load_string_from_file("temp_goal.py")
                        
                        
                        updated_goal = generate_updated_goal(gpt_model_type,template_code_filepaths[1:] + generated_files[:3], [template_code_filepaths[0]]+ generated_files[:2], original_goal_code, variable_name,prompt_filepaths["update_goal_state"],  prompt_filepaths["generate_goal_state"], "temp_goal.py", verbose = False)
                        if updated_goal is None:
                            print("Fail to update the goal given calibrated code, calibration failed.")
                            has_error = True
                            execution_history[-1]["error_message"] = "detect mismatch, but calibration failed, goal state can not be updated."
                            break
                        #exit()
                        # load updated simulator 
                        generated_appliance_code = load_generated_code(generated_files, setting="specific")
                        appliance_simulator, current_state_simulator, goal_state_simulator, feedbacks, _, _ = revert_to_previous_state(past_actions, oracle_appliance_code, generated_appliance_code, 0, grounding_mapping_filepath, [], setting="specific",verbose=True)

                        print("past actions: ", past_actions)
                        print(f"#### after updating goal and var, reverting to previous state, \n appliance simulator: {appliance_simulator} \n current state simulator: {current_state_simulator} \n goal state simulator: {goal_state_simulator}")

                        modified_code_attempt += 1
                    
                    else:
                        print("There is a mismatch between simulation and real world, but calibration of variable definition failed.")
                        has_error = True
                        execution_history[-1]["error_message"] = "mismatch detected, but variable definition calibration failed."
                        break
                
                    
                print("goal state reached:", reached_goal)
                
            if has_error or reached_goal != True or modified_code_attempt > allowed_modification_trials:
                    # rely on llm planner to complete this subgoal.
                if modified_code_attempt >= 3:
                    execution_history[-1]["error_message"] = "mismatch detected, but 3 trials of calibration still cannot achieve the goal."
                print("resolution failed or goal not reached or modify code more than 3 times.")
                break
           # If you want to exit the outer loop

        # consider change to only has error, still try complete other features. 
        #if has_error:
        #    break
        if has_error or reached_goal != True or modified_code_attempt > allowed_modification_trials:
            break


    # here resolve to llm agents. 
    if reached_goal != True or modified_code_attempt > allowed_modification_trials:
        print("previous attempt fails, using default llm agents to complete the task. ")
    
    appliance_current_state = appliance_simulator.get_state()
    log_record["executed_goal_state"] = appliance_current_state
    log_record["execution_history"] = execution_history
    score, score_comments = generate_score(appliance_current_state, testcase_info)
    log_record["score"] = score
    log_record["score_comments"] = score_comments

    # write the log record as a json file 
    create_or_replace_path(log_record_filepath)
    with open(log_record_filepath, 'w') as f:
        json.dump(log_record, f, indent = 4)

    shutil.copyfile("log.out", raw_output_filepath)

if __name__ == "__main__":
    pass

    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 
    
    # This File evaluates: VLM with no user manual, no intermediate reasoning. 
    
    # test param 
    trial_rounds_per_testcase = 1
    gpt_model_type = "gpt-4o-2024-11-20"
    machine_type = '_1_microwave'
    machine_id = "1"
    testcase_difficulty = "easy"
    question_id = "2"

    #######################
    # Available Info 
    #######################
    # appliance observations 
    observations_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_2_control_panel_images/_1_selected/xxxxx/")
    # control panel element names 
    control_panel_element_names_filepath = os.path.expanduser(f'~/TextToActions/dataset/simulated/_1_user_manual/_3_extracted_control_panel_element_names/{gpt_model_type}/xxxxx/_yyyyy.py')

    # user manual text 
    user_manual_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_1_user_manual/_2_text/xxxxx/_yyyyy.txt")

    # appliance simulator 
    template_code_root = os.path.expanduser("~/TextToActions/code/simulated/samples")
    template_code_filepaths = [os.path.join(template_code_root, f) for f in ["_0_search.py", "_1_variables.py", "_2_features.py", "_3_actions.py"]]
    oracle_appliance_code_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_4_simulators_with_states_and_display/xxxxx/_yyyyy.py")

    # proposed_actions  
    grounding_mapping_filepath = os.path.expanduser(f"~/TextToActions/dataset/simulated/_4_visual_grounding/{gpt_model_type}/_1_action_names/_3_proposed_to_oracle_action_mapping/xxxxx/yyyyy.json")
    action_option_filepath= os.path.expanduser(f'~/TextToActions/dataset/simulated/_4_visual_grounding/{gpt_model_type}/_1_action_names/_1_proposed_action_names/xxxxx/_yyyyy.txt')

    instance_info_filepaths = {
        "observations_dir": observations_dir,
        "control_panel_element_names_filepath": control_panel_element_names_filepath,
        "user_manual_filepath": user_manual_filepath,
        "oracle_appliance_code_filepath": oracle_appliance_code_filepath,
        "grounding_mapping_filepath": grounding_mapping_filepath,
        "action_option_filepath": action_option_filepath
    }

    # testcase input data
    testcase_input_root_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/hhhhh/xxxxx/_yyyyy.py")
    testcase_input_filepaths = {
        "easy_testcase_input_filepath": testcase_input_root_dir.replace("hhhhh", "_6_testcases_specific_formatted"),
        "hard_testcase_input_filepath": testcase_input_root_dir.replace("hhhhh", "_9_testcases_compound_formatted"),
        "ambiguous_testcase_input_filepath": testcase_input_root_dir.replace("hhhhh", "_8_testcases_unified_formatted"),
    }

    # prompt
    prompt_root_dir = os.path.expanduser("~/TextToActions/code/simulated/prompts/paper_exp/baselines_v1/_3_HV_M_SR_MA_specific")
    prompt_filepaths = {
    "define_variables": os.path.join(prompt_root_dir, "_0_define_variables.txt"),
    "define_feature_list": os.path.join(prompt_root_dir, "_1_define_feature_list.txt"),
    "verify_feature_list": os.path.join(prompt_root_dir, "_2_verify_feature_list.txt"),
    "verify_meta_actions": os.path.join(prompt_root_dir, "_3_verify_meta_actions.txt"),
    "define_world_model": os.path.join(prompt_root_dir, "_4_define_world_model.txt"),
    "make_world_model_specific_to_command": os.path.join(prompt_root_dir, "_5_regenerate_model.txt"),
    "generate_goal_state": os.path.join(prompt_root_dir, "_6_generate_goal_state.txt"),
    "decide_mismatch": os.path.join(prompt_root_dir, "_7_decide_mismatch.txt"),
    "distill_feedback": os.path.join(prompt_root_dir, "_8_distill_feedback.txt"),
    "generate_record_sequence": os.path.join(prompt_root_dir, "_9_generate_record_sequence.txt"),
    "calibrate_current_value": os.path.join(prompt_root_dir, "_10_calibrate_current_value.txt"),
    "update_goal_state": os.path.join(prompt_root_dir, "_11_update_goal_state.txt"),
    "correct_world_model": os.path.join(prompt_root_dir, "_12_correct_world_model.txt"),
    }

    ######################
    # Generated Info
    ######################

    reasoning_root_dir = os.path.expanduser(
    f"~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselinesv1/_3_HV_M_SR_MA_specific/{gpt_model_type}/xxxxx/yyyyy/_0_reasoning"
    )

    reasoning_filepaths = {
        "control_panel_label_details": os.path.join(reasoning_root_dir, "_1_control_panel_label_details.txt"),
        #"proposed_variables": os.path.join(reasoning_root_dir, "_2_proposed_variables.py"),
        #"proposed_features": os.path.join(reasoning_root_dir, "_3_proposed_feature_list.py"),
        #"proposed_world_model": os.path.join(reasoning_root_dir, "_4_proposed_world_model.py"),
    }
    # "make_world_model_specific_to_command": os.path.join(reasoning_root_dir, "_5_make_world_model_specific_to_command.py"

    # testcase output result 
    output_root_dir = os.path.expanduser(f"~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselinesv1/_3_HV_M_SR_MA_specific/{gpt_model_type}/xxxxx/yyyyy/hhhhh/zzzzz/wwwww")
    output_filepaths = {
        "proposed_variables": os.path.join(output_root_dir, "_1_proposed_variables.py"),
        "proposed_features": os.path.join(output_root_dir, "_2_proposed_features.py"),
        "proposed_world_model": os.path.join(output_root_dir, "_3_proposed_world_model.py"),
        "world_model_specific_to_command": os.path.join(output_root_dir, "_9_world_model_specific_to_command.py"),
        "goal_state": os.path.join(output_root_dir, "_4_goal_state.py"),
        "log_record": os.path.join(output_root_dir, "_0_log_record.json"),
        "updated_variables": os.path.join(output_root_dir, "_5_updated_variables.py"),
        "updated_world_model": os.path.join(output_root_dir, "_6_updated_world_model.py"),
        "updated_goal_state": os.path.join(output_root_dir, "_7_updated_goal_state.py"),
        "raw_output": os.path.join(output_root_dir, "_8_raw_output.txt"),
    }
    
    test_all_appliance_types(gpt_model_type,
        instance_info_filepaths, reasoning_filepaths, # get variables
        template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, selected_machine_type = machine_type, selected_machine_id = machine_id, selected_testcase_difficulty = testcase_difficulty, selected_question_id = question_id,verbose = False, mode= "batch")
    # mode can be test or batch


    
