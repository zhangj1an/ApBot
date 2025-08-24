# no visual grounding: input is image and labelled numbers. 
# compare the _4_ our method and _5_ its method on a few baselines: 
# x gpt-4.5 ($70)
# x gpt-4-0613 ($30)
# gpt-4-turbo-2024-04-09 ($10) gpt-4-turbo-2024-04-09
# Gpt-4o-20240513 ($2.5)
# o1-mini ($1.1) - text only 

# firstly try it on gpt-4o-2024-11-20
# then try it on gpt-4o-2024-05-13

import os
import sys
import json
import textwrap
import re
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.load_string_from_file import load_string_from_file, load_string_from_files
from simulated.utils.extract_python_code import extract_python_code
from simulated.utils.extract_list_from_file import extract_list_from_file
from simulated.utils.create_or_replace_path import create_or_replace_path
from simulated.utils.task.derive_variable_definition import analyze_continuous_sequence, analyze_discrete_sequence
from simulated.utils.task.generate_score import generate_score
from simulated.utils.task.interact_with_simulator import interact_with_appliance_simulator
from simulated.utils.task.matches_run_action_format import matches_run_action_format
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.task.propose_actions import propose_action
from simulated.utils.task.replace_placeholder_in_filepaths import replace_placeholder_in_filepaths
from simulated.utils.task.prepare_simulator import prepare_oracle_simulator
# logic:

# firsly loop through all appliance type, instance index, testcase type, intruction index, number of trials. 

# for each single trial, log a success or fail score. 

# at the end, use a score function to calculate the score for each category, and generate a excel file that has all the execution history. (here no intermediate reasoning needed, so just score and execution history will do.)

def test_one_appliance_instance_multiple_testcases(appliance_type, appliance_id, testcase_difficulty, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_input_filepath, testcases_result_filepath, prompt_filepaths,grounding_mapping_dir, button_index_image_dir, trial_rounds_per_testcase, gpt_model_type, verbose = False):
    print(f"processing: {appliance_type}/{appliance_id}")
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
        #if not (testcase_difficulty == "easy" and appliance_type == "_1_microwave" and appliance_id == "1" and question_id in ["1"]): #["2", "3", "4", "5"]): # ["1"]):
            #print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
        #    continue
        print(f"processing: {appliance_type}/{appliance_id}/{question_id}")
        if not (appliance_type == "_5_induction_cooker" and appliance_id == "1" and question_id not in ["1", "2", "4", "5"]):
            continue
        print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
        testcases_result_filepath_specific = testcases_result_filepath.replace("zzzzz", question_id) 
        test_one_single_testcase_multiple_trials(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepath_specific,prompt_filepaths, grounding_mapping_dir, button_index_image_dir,  trial_rounds_per_testcase, gpt_model_type, verbose = verbose)
        



def test_one_appliance_instance(appliance_type, appliance_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths, grounding_mapping_dir, button_index_image_dir,trial_rounds_per_testcase, gpt_model_type, verbose = False):

    var_testcase_result_filepath = output_result_filepath_placeholder.replace("hhhhh", "_4_testcases_var_formatted")

    test_one_appliance_instance_multiple_testcases(appliance_type, appliance_id, "var", user_manual_filepath,  oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, var_testcase_result_filepath, prompt_filepaths, grounding_mapping_dir, button_index_image_dir,  trial_rounds_per_testcase, gpt_model_type, verbose =verbose)
    

def test_one_appliance_type(appliance_type, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths, grounding_mapping_dir, button_index_image_dir,  trial_rounds_per_testcase, gpt_model_type, verbose = False):

    appliance_ids = os.listdir(os.path.dirname(oracle_appliance_code_filepath))
    appliance_ids = sorted([f[:-3].split("_")[-1] for f in appliance_ids if re.fullmatch(r'_\d\.py', f)])
    
    filepaths = {
        "user_manual_filepath": user_manual_filepath,
        "oracle_appliance_code_filepath": oracle_appliance_code_filepath,
        "var_testcase_input_filepath": var_testcase_input_filepath,
        "output_result_filepath_placeholder": output_result_filepath_placeholder,
        "grounding_mapping_dir": grounding_mapping_dir,
        "button_index_image_dir": button_index_image_dir,
    }

    for appliance_id in appliance_ids:
        updated_filepaths = replace_placeholder_in_filepaths(filepaths, "yyyyy", appliance_id)

        test_one_appliance_instance(
            appliance_type, appliance_id, updated_filepaths["user_manual_filepath"], updated_filepaths["oracle_appliance_code_filepath"], template_code_filepaths,
            updated_filepaths["var_testcase_input_filepath"], updated_filepaths["output_result_filepath_placeholder"],
            prompt_filepaths,
            updated_filepaths["grounding_mapping_dir"], updated_filepaths["button_index_image_dir"],trial_rounds_per_testcase, gpt_model_type, verbose=verbose
        ) 

def test_all_appliance_types(user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths, grounding_mapping_dir, button_index_image_dir, trial_rounds_per_testcase, gpt_model_type, verbose = False):

    parent_dir = os.path.dirname(os.path.dirname(oracle_appliance_code_filepath))
    appliance_types = os.listdir(parent_dir)
    
    filepaths = {
        "user_manual_filepath": user_manual_filepath,
        "oracle_appliance_code_filepath": oracle_appliance_code_filepath,
        "var_testcase_input_filepath": var_testcase_input_filepath,
        "output_result_filepath_placeholder": output_result_filepath_placeholder,
        "grounding_mapping_dir": grounding_mapping_dir,
        "button_index_image_dir": button_index_image_dir,
    }

    for appliance_type in appliance_types:
        updated_filepaths = replace_placeholder_in_filepaths(filepaths, "xxxxx", appliance_type)
        
        test_one_appliance_type(
            appliance_type, updated_filepaths["user_manual_filepath"], updated_filepaths["oracle_appliance_code_filepath"], template_code_filepaths,
            updated_filepaths["var_testcase_input_filepath"], updated_filepaths["output_result_filepath_placeholder"],
            prompt_filepaths,
            updated_filepaths["grounding_mapping_dir"], updated_filepaths["button_index_image_dir"],trial_rounds_per_testcase, gpt_model_type,verbose=verbose
        )

def test_one_single_testcase_multiple_trials(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepath,prompt_filepaths, grounding_mapping_dir, button_index_image_dir, trial_rounds_per_testcase, gpt_model_type, verbose = False):

    log_record = {}
    log_record["command_id"] = testcase_info["id"]
    log_record["command_string"] = testcase_info["command"]
    log_record["ground_truth_goal_state"] = testcase_info["important_target_states"] 
    log_record["execution_results"] = []
    print(f"command: {appliance_type}/{appliance_id}/{question_id}: {testcase_info['command']}")
    for i in range(trial_rounds_per_testcase):
        log_record_per_round = test_one_single_testcase_single_trial(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, prompt_filepaths, grounding_mapping_dir, button_index_image_dir, gpt_model_type, verbose = verbose)
        log_record_per_round["execution_round_index"] = i + 1 
        log_record["execution_results"].append(log_record_per_round)
        pass
    
    create_or_replace_path(testcases_result_filepath)
    with open(testcases_result_filepath, "w") as f:
        json.dump(log_record, f, indent = 4)

def test_one_single_testcase_single_trial(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, prompt_filepaths,grounding_mapping_dir, button_index_image_dir, gpt_model_type, verbose = False):

    log_record_per_round = {}
    execution_history = []

    user_manual_text = load_string_from_file(user_manual_filepath)
    command_string = testcase_info["command"]

    prompt_extract_relevant_user_manual_text = load_string_from_file(prompt_filepaths["extract_relevant_user_manual"])
    prompt_execute_command_context_text = load_string_from_file(prompt_filepaths["execute_command_context"]) 
    prompt_execute_command_dialogue_text = load_string_from_file(prompt_filepaths["execute_command_dialogue"])  

    user_manual_relevant_text = ""
    gpt_model = GPT4O()
    prompt = prompt_extract_relevant_user_manual_text
    prompt = prompt.replace("xxxxx", command_string)
    prompt = prompt.replace("yyyyy", user_manual_text)
    user_manual_relevant_text = gpt_model.chat_with_text(prompt, gpt_model_type=gpt_model_type)

    oracle_appliance_code = prepare_oracle_simulator(template_code_filepaths, oracle_appliance_code_filepath)

    oracle_globals = {}
    exec(oracle_appliance_code, oracle_globals)
    ApplianceSimulator = oracle_globals.get('Oracle', None)
    appliance_simulator = ApplianceSimulator()

    # list button_index_image_dir, the file with name "original" is the original image; the other one is label image 
    original_image_filepath = os.path.join(button_index_image_dir, "original.jpg")
    label_image_filepath = None
    for file in os.listdir(button_index_image_dir):
        if file != "original.jpg" and file.endswith((".jpg", ".png")):  # Adjust extensions as needed
            label_image_filepath = os.path.join(button_index_image_dir, file)
            break 
    grounding_mapping_filepath = None 
    for file in os.listdir(grounding_mapping_dir):
        if file.endswith(".json"):
            grounding_mapping_filepath = os.path.join(grounding_mapping_dir, file)
            break
    replacement_dict = {
    "zzzzz": command_string,
    "xxxxx": user_manual_relevant_text,
    "$$$$$original": original_image_filepath,
    "$$$$$label": label_image_filepath,
    "$$$$$gpt_model_type": gpt_model_type
    }
    appliance_simulator, conversation_history, termination_flag, current_observation, prompt_initialised_context, proposed_action, reasoning, grounded_action = propose_action(
        appliance_simulator, 
        prompt_execute_command_context_text, 
        replacement_dict, 
        grounding_mapping_filepath, 
        setting = "NV_UR_LP",
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
    current_step_record["reasoning"] = reasoning
    current_step_record["grounded_action"] = grounded_action
    current_step_record["current_observation"] = current_observation
    execution_history.append(current_step_record)

    for i in range(25):
        if verbose:
            print(f"################round {i}")
        if termination_flag:
            break 

        replacement_dict = {
            "xxxxx": current_observation,
            "$$$$$original": original_image_filepath,
            "$$$$$label": label_image_filepath,
            "$$$$$gpt_model_type": gpt_model_type
        }

        print("current_observation in dialogue: ", current_observation)
        appliance_simulator, conversation_history, termination_flag, current_observation, _, proposed_action, reasoning, grounded_action = propose_action(
            appliance_simulator, 
            prompt_execute_command_dialogue_text, 
            replacement_dict, 
            grounding_mapping_filepath, 
            setting = "NV_UR_LP",
            initial_setup=False, 
            prompt_initialised_context=prompt_initialised_context, 
            conversation_history=conversation_history, 
            # ,
            verbose=verbose
        )

        current_step_record = {}
        current_step_record["index"] = i+1 
        current_step_record["proposed_action"] = proposed_action
        current_step_record["reasoning"] = reasoning
        current_step_record["grounded_action"] = grounded_action
        current_step_record["current_observation"] = current_observation
        execution_history.append(current_step_record)
    
    appliance_current_state = appliance_simulator.get_state()
    score, error_msg = generate_score(appliance_current_state, testcase_info)
    log_record_per_round["execution_history"] = execution_history
    log_record_per_round["score"] = score
    log_record_per_round["score_comments"] = error_msg
    log_record_per_round["executed_goal_state"] = appliance_current_state

    print(f"command: {appliance_type}/{appliance_id}/{question_id}: {command_string}, score: {score}, comments: {error_msg}")

    return log_record_per_round


if __name__ == "__main__":
    pass

    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 
    
    # This File evaluates: VLM with no user manual, no intermediate reasoning. 
    
    # user manual text 
    user_manual_filepath = os.path.expanduser("~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text/xxxxx/_yyyyy.txt")

    # appliance simulator 
    template_code_root = os.path.expanduser("~/TextToActions/code/simulated/samples_real_world")
    template_code_filepaths = [os.path.join(template_code_root, f) for f in ["_1_variables.py", "_2_features.py", "_3_actions.py"]]
    oracle_appliance_code_filepath = os.path.expanduser("~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display/xxxxx/_yyyyy.py")

    # testcase input data
    testcase_filepath_placeholder = os.path.expanduser("~/TextToActions/datasetv2/real_world/_3_simulators/_5_testcases/hhhhh/xxxxx/_yyyyy.py")

    var_testcase_input_filepath = testcase_filepath_placeholder.replace("hhhhh", "_4_testcases_var_formatted")

    # gpt-4o-2024-11-20
    gpt_model_type = "gpt-4o-2024-11-20" 

    # testcase output result 
    output_result_filepath_placeholder = os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_6_results/_6_paper_exp/baselinesv1/_1_NV_M_UR_LP/{gpt_model_type}/xxxxx/yyyyy/hhhhh/zzzzz/_0_log_record.json")
   

    # prompt
    prompt_root_dir = os.path.expanduser("~/TextToActions/code/simulated/prompts/paper_exp/real_world/_1_NV_M_UR_LP")
    prompt_filepaths = {
    "execute_command_context": os.path.join(prompt_root_dir, "_1_execute_command_context.txt"),
    "execute_command_dialogue": os.path.join(prompt_root_dir, "_2_execute_command_dialogue.txt"),
    "extract_relevant_user_manual": os.path.join(prompt_root_dir, "_0_extract_relevant_user_manual.txt"),
    }

    # press_button, press_and_hold_button, turn_dial_clockwise, turn_dial_anti_clockwise 
    button_index_image_dir = os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_5_visualised_localised_buttons_no_label/xxxxx/yyyyy")

    # grounded buttons  
    grounding_mapping_dir = os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_7_proposed_buttons_to_oracle_action_mapping/xxxxx/yyyyy") 

    # test param 
    trial_rounds_per_testcase = 1


    test_all_appliance_types(user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths, grounding_mapping_dir, button_index_image_dir, trial_rounds_per_testcase, gpt_model_type, verbose = False)


    

