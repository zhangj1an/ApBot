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
from simulated.utils.task.interact_with_simulator import interact_with_appliance_simulator, compress_planning_result, execute_action, revert_to_previous_state_for_oracle_simulator, obtain_debug_record_for_oracle_simulator
from simulated.utils.task.matches_run_action_format import matches_run_action_format
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.task.propose_actions import propose_action, generate_action_effects
from simulated.utils.task.propose_variables import extract_control_panel_labels, define_variables
from simulated.utils.task.replace_placeholder_in_filepaths import replace_placeholder_in_filepaths
from simulated.utils.task.propose_goal_state import generate_goal_state
from simulated.utils.task.prepare_simulator import prepare_oracle_simulator, prepare_generated_simulator, load_oracle_generated_and_goal_simulator, load_generated_code
from simulated.utils.task.check_state_reached import check_state_reached
from simulated.utils.task.calibrate_current_value import calibrate_current_value, calibrate_current_value_for_variables
from simulated.utils.task.generate_updated_goal import generate_updated_goal
from simulated.utils.task.check_reasoning_file_existance import check_reasoning_file_existance
from simulated.utils.task.save_prints_to_file import save_prints_to_file
# assume the perception is done first, merge later 
# in one go, propose variable, feature list and world model, and task-specific model, goal state, and run. 

# here already have code. 

# 
# firstly generate variables, features and action effects. 

def test_one_appliance_type(gpt_model_type, appliance_type, instance_info_filepaths, reasoning_filepaths,  template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, verbose = False):

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
            gpt_model_type, 
            appliance_type, 
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
        if not (appliance_type == "_3_rice_cooker" and appliance_id == "5" and question_id in ["4"]):
            continue
        
        print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
        testcases_result_filepaths_specific = replace_placeholder_in_filepaths(testcases_result_filepaths, "zzzzz", question_id)
        test_one_single_testcase_multiple_trials(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths, user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepaths_specific,prompt_filepaths, grounding_mapping_filepath,  trial_rounds_per_testcase, verbose = verbose)
        
def test_one_single_testcase_multiple_trials(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepaths,prompt_filepaths, grounding_mapping_filepath, trial_rounds_per_testcase, verbose = False):

    print("processing: ", appliance_type, appliance_id, question_id)
    for i in range(trial_rounds_per_testcase):
        print("trial: ", i+1)
        updated_testcases_result_filepaths = replace_placeholder_in_filepaths(testcases_result_filepaths, "wwwww", str(i+1))
        test_one_single_testcase_single_trial(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, updated_testcases_result_filepaths, prompt_filepaths, grounding_mapping_filepath, verbose = verbose)
        




def test_one_appliance_instance(gpt_model_type,appliance_type, appliance_id, instance_info_filepaths, reasoning_filepaths, template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, verbose = False):

    # for one appliance instance, extract its labels, variables, actions, world model. 
    control_panel_label_details_filepath = reasoning_filepaths["control_panel_label_details"]
    proposed_variables_filepath = reasoning_filepaths["proposed_variables"]
    
    user_manual_filepath = instance_info_filepaths["user_manual_filepath"]
    action_option_filepath = instance_info_filepaths["action_option_filepath"]
    oracle_appliance_code_filepath = instance_info_filepaths["oracle_appliance_code_filepath"]
    grounding_mapping_filepath = instance_info_filepaths["grounding_mapping_filepath"]

    extract_control_panel_labels(gpt_model_type,instance_info_filepaths["observations_dir"], appliance_type, appliance_id, control_panel_label_details_filepath,instance_info_filepaths["control_panel_element_names_filepath"],  use_history = True )

    define_variables(gpt_model_type,action_option_filepath, user_manual_filepath, control_panel_label_details_filepath, prompt_filepaths["define_variables"], template_code_filepaths[1], proposed_variables_filepath, "", use_history = True)

    var_testcase_output_filepaths = replace_placeholder_in_filepaths(output_filepaths, "hhhhh", "_1_var_testcases")

    test_one_appliance_instance_multiple_testcases(gpt_model_type,appliance_type, appliance_id, "var", reasoning_filepaths, user_manual_filepath,  action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_input_filepaths["var_testcase_input_filepath"], var_testcase_output_filepaths, prompt_filepaths, grounding_mapping_filepath, trial_rounds_per_testcase, verbose =verbose)
    





def test_one_single_testcase_single_trial(gpt_model_type,appliance_type, appliance_id, question_id, reasoning_filepaths,user_manual_filepath, action_option_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepaths, prompt_filepaths,grounding_mapping_filepath, verbose = False):


    command_string = testcase_info["command"]
    user_manual_text = load_string_from_file(user_manual_filepath)

    log_record_filepath = testcases_result_filepaths["log_record"]
    raw_output_filepath = testcases_result_filepaths["raw_output"]
    create_or_replace_path(raw_output_filepath)
    #save_prints_to_file(raw_output_filepath)

    log_record = {}
    log_record["command_id"] = testcase_info["id"]
    log_record["command_string"] = command_string
    log_record["ground_truth_goal_state"] = testcase_info["important_target_states"] 
    execution_history = []

    with open("temp_generated_variable.py", 'w') as f:
        f.write(load_string_from_file(reasoning_filepaths["proposed_variables"]))

    # sample var code + generated var code
    defined_variables_code = load_string_from_files([template_code_filepaths[1],  reasoning_filepaths["proposed_variables"]])
    
    oracle_appliance_code = prepare_oracle_simulator(template_code_filepaths, oracle_appliance_code_filepath)

    variable_search_code = load_string_from_file(template_code_filepaths[0])
    
    
    oracle_globals = {}
    exec(oracle_appliance_code, oracle_globals)
    ApplianceSimulator = oracle_globals.get('Oracle', None)
    appliance_simulator = ApplianceSimulator()
    exec(variable_search_code, oracle_globals)
    VariableSearch = oracle_globals.get('VariableSearch', None)

    action_option_text = load_string_from_file(action_option_filepath)

    replacement_dict = {
        "xxxxx": user_manual_text, 
        "hhhhh": action_option_text,
        "zzzzz": command_string,
        "yyyyy": defined_variables_code,
        "$$$$$gpt_model_type": gpt_model_type
    }

    prompt_execute_command_context_text = load_string_from_file(prompt_filepaths["execute_command_context"])
    prompt_execute_command_dialogue_text = load_string_from_file(prompt_filepaths["execute_command_dialogue"])
    
    appliance_simulator, termination_flag, current_observation, prompt_initialised_context, proposed_action, grounded_action, adjusting_variable_name, expected_feedback, reason = propose_action(
        appliance_simulator, 
        prompt_execute_command_context_text, 
        replacement_dict, 
        grounding_mapping_filepath, 
        setting = "UR_MA",
        initial_setup=True, 
        verbose=verbose
    )

    current_step_record = {}
    current_step_record["index"] = -1
    current_step_record["context_prompt"] = prompt_initialised_context
    execution_history.append(current_step_record)

    current_step_record = {}
    current_step_record["index"] = 0 
    current_step_record["proposed_action"] = proposed_action
    current_step_record["grounded_action"] = grounded_action
    current_step_record["current_observation"] = current_observation
    current_step_record["expected_feedback"] = expected_feedback
    current_step_record["adjusting_variable_name"] = adjusting_variable_name
    current_step_record["reason"] = reason
    execution_history.append(current_step_record)

    past_execution_records = [f"executing action: {proposed_action}, feedback: {current_observation}"]
    #past_actions = []
    #feedbacks = []
    has_error = False 
    allowed_modification_trials = 2
    modified_code_attempt = {}
    step_index = 0
    for i in range(25):

        print("################round ", i)
        print("currently, here are the past actions taken: ", "\n".join(past_execution_records), flush=True)
        if verbose:
            print(f"################round {i}")
        if termination_flag or has_error:
            print("repeated errors when updating variables, exiting loop")
            break 
        
        # check if works 
        reached_goal, reached_goal_details = check_state_reached(gpt_model_type, prompt_filepaths["decide_mismatch"], [template_code_filepaths[1], reasoning_filepaths["proposed_variables"]], prompt_filepaths["distill_feedback"], f"let {adjusting_variable_name} to satisfy the task of {command_string}", str(current_observation), command_string, verbose = False)

        reached_expectation, _ = check_state_reached(gpt_model_type, prompt_filepaths["decide_mismatch"], [template_code_filepaths[1] , reasoning_filepaths["proposed_variables"] ], prompt_filepaths["distill_feedback"], str(expected_feedback), str(current_observation), command_string, verbose = False)

        calibration_successful = False
        while adjusting_variable_name != "" and not reached_goal and not reached_expectation and "press_number" not in proposed_action:
            # if there is a modified_code_attempt["adjusting_variable_name"], and it is greater than allowed_modification_trials, then break.
            if adjusting_variable_name in modified_code_attempt and modified_code_attempt[adjusting_variable_name] >= allowed_modification_trials:
                has_error = True 
                print(f"repeated errors when updating variable {adjusting_variable_name}, exiting loop")
                break 
            print(f"detect mismatch when trying to set variable {adjusting_variable_name} to {expected_feedback}")
            
            
            print("now obtaining debug record for oracle simulator")
            
            debug_record, appliance_simulator = obtain_debug_record_for_oracle_simulator(proposed_action, appliance_simulator, grounding_mapping_filepath, verbose = False)
            execution_history[-1]["calibration_attempt"] = debug_record
            print("debug record: ", debug_record)
            #exit()
            #past_execution_records += debug_record

            # fix this function later, finish the pipeline first 
            calibration_successful, current_var, goal_var = calibrate_current_value_for_variables(gpt_model_type, prompt_filepaths["calibrate_current_value"], adjusting_variable_name, debug_record, prompt_filepaths["define_variables"], template_code_filepaths[1], "temp_generated_variable.py", str(proposed_action),  str(expected_feedback), prompt_filepaths["generate_record_sequence"], prompt_filepaths["update_goal"],command_string, revert_back_later= False, verbose = False)
            # if modified code attempt has a key called adjusting_variable_name, then increment it by 1. otherwise creat this key and assign it to be 1. 
            if adjusting_variable_name in modified_code_attempt:
                modified_code_attempt[adjusting_variable_name] += 1
            else:
                modified_code_attempt[adjusting_variable_name] = 1
            if calibration_successful:
                print("calibration successful")
                break

        if adjusting_variable_name != "" and not reached_goal and not has_error and calibration_successful:
            action_tuples = []
            action_tuples = generate_action_effects(load_string_from_file(prompt_filepaths["generate_action_effect"]), user_manual_text, defined_variables_code, action_option_text, command_string, adjusting_variable_name, expected_feedback, past_execution_records, debug_record)
            print("generated action tuples: ", action_tuples)
            # if press_number in action tuples, return [] also. 
            print("len of past_execution_records: ", len(past_execution_records))
            
            variablesearch = VariableSearch(current_var, goal_var, action_tuples, verbose= False)
            planning_result = variablesearch.search()
            print("planning_result: ", planning_result)
            planning_result = compress_planning_result(planning_result)
            print("compressed planning_result: ", planning_result)
            if planning_result is None: 
                #has_error = True 
                print(f"planning failed, generated flawed transition dynamics, using llm to generate actions")
                current_step_record = {}
                step_index += 1
                current_step_record["index"] = step_index
                current_step_record["error_message"] = "planning failed, generated model has flawed transition dynamics"
                execution_history.append(current_step_record)
                continue 

            else:
                for current_action in planning_result: 
                    
                    appliance_simulator, termination_flag, current_observation, grounded_action = interact_with_appliance_simulator(
                        appliance_simulator, current_action, grounding_mapping_filepath, verbose
                    )
                    current_step_record = {}
                    step_index += 1
                    current_step_record["index"] = step_index
                    current_step_record["proposed_action"] = current_action
                    current_step_record["grounded_action"] = grounded_action
                    current_step_record["current_observation"] = current_observation
                    execution_history.append(current_step_record) 
                    print("apply action: ", current_action, "observation: ", current_observation)
                    past_execution_records.append(f"executing action: {current_action}, feedback: {current_observation}")
                    print("len of past_execution_records: ", len(past_execution_records))
                    
                proposed_action = planning_result
                grounded_action = ""
                
        current_step_record = {}
        step_index += 1
        current_step_record["index"] = step_index
        current_step_record["proposed_action"] = proposed_action
        current_step_record["grounded_action"] = grounded_action
        current_step_record["current_observation"] = current_observation
        current_step_record["expected_feedback"] = expected_feedback
        current_step_record["adjusting_variable_name"] = adjusting_variable_name
        current_step_record["reached_goal_details"] = reached_goal_details
        current_step_record["reason"] = reason
        execution_history.append(current_step_record)

       
        # if reached goal, then record into records
        # updated replacement dict 
        replacement_dict = {
            "xxxxx": user_manual_text,
            "hhhhh": action_option_text,
            "zzzzz": command_string,
            "yyyyy": "\n".join(past_execution_records),
            "uuuuu": defined_variables_code,
            "$$$$$gpt_model_type": gpt_model_type
        }

        # otherwise use llm to execute actions. 
        appliance_simulator, termination_flag, current_observation, _, proposed_action, grounded_action, adjusting_variable_name, expected_feedback, reason = propose_action(
            appliance_simulator, 
            prompt_execute_command_dialogue_text, 
            replacement_dict, 
            grounding_mapping_filepath, 
            setting = "UR_MA",
            initial_setup=True, 
            verbose=verbose
        )
        if termination_flag:
            current_step_record = {}
            step_index += 1
            current_step_record["index"] = step_index
            current_step_record["proposed_action"] = proposed_action
            current_step_record["grounded_action"] = grounded_action
            current_step_record["current_observation"] = current_observation
            current_step_record["expected_feedback"] = expected_feedback
            current_step_record["adjusting_variable_name"] = adjusting_variable_name
            current_step_record["reached_goal_details"] = reached_goal_details
            current_step_record["reason"] = reason
            execution_history.append(current_step_record)
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

    shutil.copyfile("log.out", raw_output_filepath)

if __name__ == "__main__":
    pass

    # srun -u -o "testlog.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 
    
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
    prompt_root_dir = os.path.expanduser("~/TextToActions/code/simulated/prompts/paper_exp/baselines_v1/_7_HV_M_UR_MA")
    prompt_filepaths = {
    "define_variables": os.path.join(prompt_root_dir, "_0_define_variables.txt"),
    "execute_command_context": os.path.join(prompt_root_dir, "_1_execute_command_context.txt"),
    "execute_command_dialogue": os.path.join(prompt_root_dir, "_2_execute_command_dialogue.txt"),
    "generate_action_effect": os.path.join(prompt_root_dir, "_5_generate_action_effect.txt"),
    "decide_mismatch": os.path.join(prompt_root_dir, "_7_decide_mismatch.txt"),
    "distill_feedback": os.path.join(prompt_root_dir, "_3_distill_feedback.txt"),
    "generate_record_sequence": os.path.join(prompt_root_dir, "_4_generate_record_sequence.txt"),
    "calibrate_current_value": os.path.join(prompt_root_dir, "_6_calibrate_current_value.txt"),
    "update_goal": os.path.join(prompt_root_dir, "_8_update_goal.txt"),
    }

    ######################
    # Generated Info
    ######################

    reasoning_root_dir = os.path.expanduser(
    f"~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_7_HV_M_UR_MA/{gpt_model_type}/xxxxx/yyyyy/_0_reasoning"
    )

    reasoning_filepaths = {
        "control_panel_label_details": os.path.join(reasoning_root_dir, "_1_control_panel_label_details.txt"),
        "proposed_variables": os.path.join(reasoning_root_dir, "_2_proposed_variables.py"),
    }
    # "make_world_model_specific_to_command": os.path.join(reasoning_root_dir, "_5_make_world_model_specific_to_command.py"

    # testcase output result 
    output_root_dir = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_7_HV_M_UR_MA/{gpt_model_type}/xxxxx/yyyyy/hhhhh/zzzzz/wwwww")
    output_filepaths = {
        "log_record": os.path.join(output_root_dir, "_1_log_record.json"),
        "raw_output": os.path.join(output_root_dir, "_2_raw_output.txt"),
    }

    # test param 
    trial_rounds_per_testcase = 1

    test_all_appliance_types(
        gpt_model_type, instance_info_filepaths, reasoning_filepaths, # get variables
        template_code_filepaths, testcase_input_filepaths, output_filepaths, prompt_filepaths, trial_rounds_per_testcase, verbose = False)


    
