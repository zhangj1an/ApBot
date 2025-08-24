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
from simulated.utils.task.interact_with_simulator import revert_to_previous_state, obtain_debug_record, obtain_debug_record_for_oracle_simulator, revert_to_previous_state_for_oracle_simulator
from simulated.utils.task.calibrate_current_value import calibrate_current_value
from simulated.utils.task.generate_updated_goal import generate_updated_goal
from simulated.utils.task.check_reasoning_file_existance import check_reasoning_file_existance
from simulated.utils.task.save_prints_to_file import save_prints_to_file
# assume the perception is done first, merge later 
# in one go, propose variable, feature list and world model, and task-specific model, goal state, and run. 

# here already have code. 

# 
# firstly generate variables, features and action effects. 

def test_one_appliance_type(gpt_model_type,appliance_type, instance_info_filepaths, reasoning_filepaths,  template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, verbose = False):

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

        test_one_appliance_instance(
            gpt_model_type, appliance_type, appliance_id, updated_filepaths["instance_info_filepaths"], updated_filepaths["reasoning_filepaths"], template_code_filepaths,
            updated_filepaths["testcase_input_filepaths"], updated_filepaths["output_filepaths"],
            prompt_filepaths,
            trial_rounds_per_testcase, verbose=verbose
        ) 

def test_all_appliance_types(
gpt_model_type, instance_info_filepaths, reasoning_filepaths, template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, verbose = False):

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
        
        test_one_appliance_type(
            gpt_model_type, appliance_type, 
            updated_filepaths["instance_info_filepaths"], updated_filepaths["reasoning_filepaths"], template_code_filepaths,
            updated_filepaths["testcase_input_filepaths"], updated_filepaths["output_filepaths"],
            prompt_filepaths,
            trial_rounds_per_testcase, verbose=verbose
        )

def test_one_appliance_instance_multiple_testcases(gpt_model_type, appliance_type, appliance_id, testcase_difficulty, reasoning_filepaths,  user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_input_filepath, testcases_result_filepaths, prompt_filepaths,grounding_mapping_filepath, trial_rounds_per_testcase, verbose = False):

    # update world model specific to command.
    # update goal state. 
    # then propose   

    testcase_info_list = extract_list_from_file(testcase_input_filepath) 
    testcases_info = sorted(testcase_info_list, key=lambda x: x['id']) 
    for testcase_info in testcases_info:
        question_id = str(testcase_info["id"])
        # testcase_difficulty : ["easy", "hard", "ambi"]:
        # appliance_type: ["_1_microwave", "_2_washing_machine", "_3_rice_cooker", "_4_air_purifier"]
        # appliance_id : ["1", "2", "3", "4", "5"]
        # question_id : ["1", "2", "3", "4", "5"]

        # Microwave: 1, 2, 3 || 0, 4
        # Washing machine: 0, 2, 3 || 
        # Rice cooker: 0, 2, 4 || 0, 2
        # Air purifier: 1, 2, 3 || 0, 4
        #if not (appliance_type in ["_5_bread_maker"] and appliance_id in ["5"] and question_id in ["6", "7", "8", "9", "10"]):
        if not (appliance_type == "_3_rice_cooker" and appliance_id == "5" and question_id in ["4"]):
            continue 
 
       
        print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
        testcases_result_filepaths_specific = replace_placeholder_in_filepaths(testcases_result_filepaths, "zzzzz", question_id)
        test_one_single_testcase_multiple_trials(gpt_model_type, appliance_type, appliance_id, question_id, reasoning_filepaths, user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepaths_specific,prompt_filepaths, grounding_mapping_filepath,  trial_rounds_per_testcase, verbose = verbose)
        
def test_one_single_testcase_multiple_trials(gpt_model_type, appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepaths,prompt_filepaths, grounding_mapping_filepath, trial_rounds_per_testcase, verbose = False):

    print("processing: ", appliance_type, appliance_id, question_id)
    for i in range(trial_rounds_per_testcase):
        print("trial: ", i+1)
        updated_testcases_result_filepaths = replace_placeholder_in_filepaths(testcases_result_filepaths, "wwwww", str(i+1))
        test_one_single_testcase_single_trial(gpt_model_type, appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, updated_testcases_result_filepaths, prompt_filepaths, grounding_mapping_filepath, verbose = verbose)
        




def test_one_appliance_instance(gpt_model_type, appliance_type, appliance_id, instance_info_filepaths, reasoning_filepaths, template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, verbose = False):

    # for one appliance instance, extract its labels, variables, actions, world model. 
    control_panel_label_details_filepath = reasoning_filepaths["control_panel_label_details"]
    proposed_variables_filepath = reasoning_filepaths["proposed_variables"]
    proposed_features_filepath = reasoning_filepaths["proposed_features"]
    user_manual_filepath = instance_info_filepaths["user_manual_filepath"]
    action_option_filepath = instance_info_filepaths["action_option_filepath"]
    oracle_appliance_code_filepath = instance_info_filepaths["oracle_appliance_code_filepath"]
    grounding_mapping_filepath = instance_info_filepaths["grounding_mapping_filepath"]

    extract_control_panel_labels(gpt_model_type, instance_info_filepaths["observations_dir"], appliance_type, appliance_id, control_panel_label_details_filepath,instance_info_filepaths["control_panel_element_names_filepath"],  use_history = True )

    define_variables(gpt_model_type,action_option_filepath, user_manual_filepath, control_panel_label_details_filepath, prompt_filepaths["define_variables"], template_code_filepaths[1], proposed_variables_filepath,"", use_history = True)

    define_feature_list(gpt_model_type,action_option_filepath, proposed_variables_filepath, user_manual_filepath, prompt_filepaths["define_feature_list"], proposed_features_filepath, template_code_filepaths[2], prompt_filepaths["verify_feature_list"], prompt_filepaths["verify_meta_actions"],"", verbose, use_history = True)
    
    # define world model agnostic to the command. 
    define_world_model(gpt_model_type,action_option_filepath, proposed_variables_filepath, proposed_features_filepath, user_manual_filepath, prompt_filepaths["define_world_model"], reasoning_filepaths["proposed_world_model"], template_code_filepaths[1], template_code_filepaths[2], template_code_filepaths[3], "", use_history = True)

    var_testcase_output_filepaths = replace_placeholder_in_filepaths(output_filepaths, "hhhhh", "_1_var_testcases")

    test_one_appliance_instance_multiple_testcases(gpt_model_type,appliance_type, appliance_id, "var", reasoning_filepaths, user_manual_filepath,  action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_input_filepaths["var_testcase_input_filepath"], var_testcase_output_filepaths, prompt_filepaths, grounding_mapping_filepath, trial_rounds_per_testcase, verbose =verbose)





def test_one_single_testcase_single_trial(gpt_model_type, appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepaths, prompt_filepaths,grounding_mapping_filepath, verbose = False):

    
    command_string = testcase_info["command"]

    log_record_filepath = testcases_result_filepaths["log_record"]
    raw_output_filepath = testcases_result_filepaths["raw_output"]
    create_or_replace_path(raw_output_filepath)
    save_prints_to_file(raw_output_filepath)
    log_record = {}
    log_record["command_id"] = testcase_info["id"]
    log_record["command_string"] = command_string
    log_record["ground_truth_goal_state"] = testcase_info["important_target_states"] 
   
    # if the given file does not exists, directly return zero. 
    generated_code_filepaths = [reasoning_filepaths["proposed_variables"], reasoning_filepaths["proposed_features"], reasoning_filepaths["proposed_world_model"]]

    with open("temp_generated_variable.py", "w") as f:
        f.write(load_string_from_file(reasoning_filepaths["proposed_variables"]))

    if not check_reasoning_file_existance(generated_code_filepaths, log_record, log_record_filepath):
        return
    
    generate_world_model_specific_to_command(gpt_model_type, prompt_filepaths,action_option_filepath, reasoning_filepaths, template_code_filepaths[1:], testcases_result_filepaths, user_manual_filepath, command_string, use_history = True)

    
    if not check_reasoning_file_existance([testcases_result_filepaths["world_model_specific_to_command"]], log_record, log_record_filepath):
        return 
    
    generate_goal_state(gpt_model_type, prompt_filepaths["generate_goal_state"], testcases_result_filepaths["goal_state"], template_code_filepaths[1:], generated_code_filepaths, command_string, user_manual_filepath, testcases_result_filepaths["world_model_specific_to_command"], use_history = True) 
    
    if not check_reasoning_file_existance([testcases_result_filepaths["goal_state"]], log_record, log_record_filepath):
        return 
    
    
    oracle_appliance_code = prepare_oracle_simulator(template_code_filepaths[1:], oracle_appliance_code_filepath)
    
    generated_appliance_code, generated_files = prepare_generated_simulator(template_code_filepaths[0], generated_code_filepaths, testcases_result_filepaths) 

    generated_goal_code = load_generated_code(generated_files)
    appliance_simulator, current_state_simulator, goal_state_simulator, feature_sequence, _ = load_oracle_generated_and_goal_simulator(oracle_appliance_code, generated_appliance_code, generated_goal_code)

    actions = [action for action in dir(current_state_simulator) if action.startswith(('press_', 'turn_')) and callable(getattr(current_state_simulator, action))]
    feature_list = current_state_simulator.feature.feature_list 

    step_index = 0 
    past_actions = []
    reached_goal = None   
    feedbacks = []
    termination_flag = False
    execution_history = []

    prompt_execute_command_context_filepath = prompt_filepaths["execute_command_dialogue"]
    prompt_execute_command_context_text = load_string_from_file(prompt_execute_command_context_filepath)
    
    for feature_progress_index in range(len(feature_sequence)):
        if termination_flag:
            break 
        current_feature = feature_sequence[feature_progress_index]
        print("current feature: ", current_feature)
        current_feature_info = feature_list[current_feature]

        subgoal_simulator = copy.deepcopy(current_state_simulator)
        #feedbacks = []
        
        for step_info in current_feature_info:
            if termination_flag:
                break
            print("step_info: ", step_info)
            actions = step_info["actions"]
            if len(actions) == 1 and "variable" not in step_info:
                step_index, appliance_simulator, current_state_simulator, termination_flag, execution_history, feedbacks = execute_action((actions[0], 1), appliance_simulator, current_state_simulator, grounding_mapping_filepath, step_index, execution_history, feedbacks, verbose = verbose) 
                print("len of execution history after automatic execution of action: ", len(execution_history))
                continue 
            variable_name = step_info["variable"]
            
            # each variable allows 5 trials, gpt can suggest the next action to adjust this variable. 
            reached_goal = False
            variable_trials = 0
            calibration_trials = 0
            #feedbacks = []
            max_calibration_attempts = 1
            while step_index < 25 and not termination_flag and variable_trials < 5: 
                replacement_dict = {
                            "ttttt": load_string_from_file(user_manual_filepath),
                            "xxxxx": generated_appliance_code,
                            "zzzzz": command_string,
                            "hhhhh": "\n".join(actions),
                            "iiiii": variable_name,
                            "kkkkk": current_feature,
                            "wwwww": "" if len(feedbacks)==0 else "\n".join(feedbacks),
                            "$$$$$gpt_model_type": gpt_model_type
                        }
                appliance_simulator, termination_flag, current_observation, _, proposed_action, grounded_action, expected_feedback, reason = propose_action(
                    appliance_simulator, 
                    prompt_execute_command_context_text, 
                    replacement_dict, 
                    grounding_mapping_filepath, 
                    setting = "SR",
                    initial_setup=True, 
                    verbose=verbose
                ) 
                print("proposed action: ", proposed_action)
                print("expected feedback: ", expected_feedback)
                step_index += 1
                variable_trials += 1
                
                if termination_flag:
                    print("termination flag is true")
                    if proposed_action != "end":
                        current_step_record = {}
                        current_step_record["step_index"] = step_index
                        current_step_record["error_message"] = f"cannot generate suitable action."
                        execution_history.append(current_step_record)
                    elif proposed_action == "end":
                        current_step_record = {}
                        current_step_record["index"] = step_index
                        current_step_record["proposed_action"] = proposed_action 
                        current_step_record["current_observation"] = current_observation     
                        current_step_record["expected_feedback"] = expected_feedback
                        current_step_record["reason"] = reason
                        execution_history.append(current_step_record)
                        past_actions += [proposed_action]
                        feedbacks += [f"executed action: {proposed_action}, feedback: {current_observation}"]
                        step_index += 1
                    print("len of execution history when terminates: ", len(execution_history))
                    break
                print("checking for mismatch")

                reached_goal, _ = check_state_reached(gpt_model_type,prompt_filepaths["decide_mismatch"], template_code_filepaths[1:] + generated_files, prompt_filepaths["distill_feedback"], f"We want to adjust the value of {variable_name} so it aligns with {command_string}", str(current_observation), command_string, verbose = False) # verbose 
                print("reached goal: ", reached_goal)
                reached_expectation, _ = check_state_reached(gpt_model_type,prompt_filepaths["decide_mismatch"], template_code_filepaths[1:] + generated_files, prompt_filepaths["distill_feedback"], str(expected_feedback), str(current_observation), command_string, verbose = False)
                print("reached expectation: ", reached_expectation)
                
                current_step_record = {}
                current_step_record["index"] = step_index
                current_step_record["proposed_action"] = proposed_action 
                current_step_record["grounded_action"] = grounded_action
                current_step_record["current_observation"] = current_observation     
                current_step_record["expected_feedback"] = expected_feedback
                current_step_record["reason"] = reason
                current_step_record["reached_goal"] = reached_goal
                execution_history.append(current_step_record)
                past_actions += [proposed_action]
                feedbacks += [f"executed action: {proposed_action}, feedback: {current_observation}"]
                #print(f"current feedbacks: {feedbacks}\n")
                if reached_goal:# and reached_expectation:
                    print("reached goal")
                    break
                if not reached_expectation and (
                    not hasattr(current_state_simulator, "meta_actions_dict") 
                    or actions[0] not in current_state_simulator.meta_actions_dict.values()
                ):
                    if calibration_trials  > max_calibration_attempts:
                        termination_flag = True
                        break
                    calibration_trials += 1
                    debug_record, appliance_simulator = obtain_debug_record_for_oracle_simulator(proposed_action, appliance_simulator, grounding_mapping_filepath, verbose = False)
                    print("current state of appliance simulator: ", appliance_simulator)
                    calibration_successful = calibrate_current_value(gpt_model_type, prompt_filepaths["calibrate_current_value"], expected_feedback, debug_record, prompt_filepaths["define_variables"], template_code_filepaths[1:], generated_files[:3], str(proposed_action), "\n".join(feedbacks), "", current_observation,prompt_filepaths["generate_record_sequence"], prompt_filepaths["correct_world_model"], "temp_generated_variable.py", "temp_generated_world_model.py", revert_back_later=False, verbose = False)
                    execution_history[-1]["calibration_attempt"] = debug_record
                    feedbacks += debug_record

            
                    if calibration_successful:
                        #original_goal_code = load_string_from_file("temp_goal.py")

                        #updated_goal = generate_updated_goal(gpt_model_type,template_code_filepaths[1:] + generated_files[:3], [template_code_filepaths[0]]+ generated_files[:2], original_goal_code, expected_feedback,command_string,prompt_filepaths["update_goal_state"],  prompt_filepaths["generate_goal_state"], "temp_goal.py",verbose = False)
                        #if updated_goal is None:
                            #print("Fail to update the goal given calibrated code, calibration failed.")
                            #termination_flag = True
                            #current_step_record = {}
                            #current_step_record["step_index"] = step_index
                            #current_step_record["error_message"] = "detect mismatch, but calibration failed, goal state can not be updated."
                            #execution_history.append(current_step_record)
                            #break

                        generated_appliance_code = load_generated_code(generated_files)
                        
                        print("past actions: ", past_actions)
                        print(f"#### after updating goal and var, reverting to previous state, \n appliance simulator: {appliance_simulator} \n")
                        #exit()
                        feedbacks = debug_record
            if not reached_goal:
                print(f"fail to set target value for{variable_name} within {max_calibration_attempts} model calibration trials and {5} value setting trials.")
                current_step_record = {}
                current_step_record["step_index"] = step_index
                current_step_record["error_message"] = f"we fail to adjust {variable_name} to its target value within 5 trials."
                execution_history.append(current_step_record)
                termination_flag = True
                break

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

    #shutil.copyfile("log.out", raw_output_filepath)

if __name__ == "__main__":
    pass

    # srun -u -o "log.out" -w crane2 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 

    # srun -u -o "no_btn_policy.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 _5_HV_M_SR_LP_CL.py
    
    # This File evaluates: VLM with no user manual, no intermediate reasoning. 
    
    gpt_model_type = "gpt-4o-2024-11-20"
    #######################
    # Available Info 
    #######################
    # appliance observations 
    observations_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_2_control_panel_images/_1_selected/xxxxx/")
    # control panel element names 
    control_panel_element_names_filepath = os.path.expanduser(f'~/TextToActions/datasetv2/simulated/_1_user_manual/_3_extracted_control_panel_element_names/{gpt_model_type}/xxxxx/_yyyyy.py')

    # user manual text 
    user_manual_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_1_user_manual/_2_text/xxxxx/_yyyyy.txt")

    # appliance simulator 
    template_code_root = os.path.expanduser("~/TextToActions/code/simulated/samples")
    template_code_filepaths = [os.path.join(template_code_root, f) for f in ["_0_search.py", "_1_variables.py", "_2_features.py", "_3_actions.py"]]
    oracle_appliance_code_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_3_simulators/_4_simulators_with_states_and_display/xxxxx/_yyyyy.py")

    # proposed_actions  
    grounding_mapping_filepath = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_4_visual_grounding/{gpt_model_type}/_1_action_names/_3_proposed_to_oracle_action_mapping/xxxxx/yyyyy.json")
    action_option_filepath= os.path.expanduser(f'~/TextToActions/datasetv2/simulated/_4_visual_grounding/{gpt_model_type}/_1_action_names/_1_proposed_action_names/xxxxx/_yyyyy.txt')

    instance_info_filepaths = {
        "observations_dir": observations_dir,
        "control_panel_element_names_filepath": control_panel_element_names_filepath,
        "user_manual_filepath": user_manual_filepath,
        "oracle_appliance_code_filepath": oracle_appliance_code_filepath,
        "grounding_mapping_filepath": grounding_mapping_filepath,
        "action_option_filepath": action_option_filepath
    }

    # testcase input data
    testcase_input_root_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_3_simulators/_5_testcases/hhhhh/xxxxx/_yyyyy.py")
    testcase_input_filepaths = {
        "var_testcase_input_filepath": testcase_input_root_dir.replace("hhhhh", "_4_testcases_var_formatted"),
    }

    # prompt
    prompt_root_dir = os.path.expanduser("~/TextToActions/code/simulated/prompts/paper_exp/baselines_v1/_5_HV_M_SR_LP")
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
    "execute_command_context": os.path.join(prompt_root_dir, "_13_execute_command_context.txt"),
    "execute_command_dialogue": os.path.join(prompt_root_dir, "_14_execute_command_dialogue.txt"),
    }

    ######################
    # Generated Info
    ######################

    reasoning_root_dir = os.path.expanduser(
    f"~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_5_HV_M_SR_LP_CL/{gpt_model_type}/xxxxx/yyyyy/_0_reasoning"
    )

    reasoning_filepaths = {
        "control_panel_label_details": os.path.join(reasoning_root_dir, "_1_control_panel_label_details.txt"),
        "proposed_variables": os.path.join(reasoning_root_dir, "_2_proposed_variables.py"),
        "proposed_features": os.path.join(reasoning_root_dir, "_3_proposed_feature_list.py"),
        "proposed_world_model": os.path.join(reasoning_root_dir, "_4_proposed_world_model.py"),
    }
    # "make_world_model_specific_to_command": os.path.join(reasoning_root_dir, "_5_make_world_model_specific_to_command.py"

    # testcase output result 
    output_root_dir = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_5_HV_M_SR_LP_CL/{gpt_model_type}/xxxxx/yyyyy/hhhhh/zzzzz/wwwww")
    output_filepaths = {
        "world_model_specific_to_command": os.path.join(output_root_dir, "_1_world_model_specific_to_command.py"),
        "goal_state": os.path.join(output_root_dir, "_2_goal_state.py"),
        "log_record": os.path.join(output_root_dir, "_3_log_record.json"),
        "raw_output": os.path.join(output_root_dir, "_4_raw_output.txt"),
    }

    # test param 
    trial_rounds_per_testcase = 1

    test_all_appliance_types(
        gpt_model_type, instance_info_filepaths, reasoning_filepaths, # get variables
        template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, verbose = False)


    
