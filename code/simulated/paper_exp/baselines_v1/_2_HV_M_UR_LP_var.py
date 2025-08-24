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

def test_one_appliance_instance_multiple_testcases(appliance_type, appliance_id, testcase_difficulty, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_input_filepath, testcases_result_filepath, prompt_filepaths,grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose = False):
    print("testcase_input_filepath: ", testcase_input_filepath)
    testcase_info_list = extract_list_from_file(testcase_input_filepath) 
    testcases_info = sorted(testcase_info_list, key=lambda x: x['id']) 
    for testcase_info in testcases_info:
        question_id = str(testcase_info["id"])
        # testcase_difficulty : ["easy", "hard", "ambi"]:
        # appliance_type: ["_1_microwave", "_2_washing_machine", "_4_rice_cooker", "_4_air_purifier"]
        # appliance_id : ["1", "2", "3", "4", "5"]
        # question_id : ["1", "2", "3", "4", "5"]

        # Microwave: 1, 2, 3 || 0, 4
        # Washing machine: 0, 2, 3 || 
        # Rice cooker: 0, 2, 4 || 0, 2
        # Air purifier: 1, 2, 3 || 0, 4
        if not (appliance_type == "_3_rice_cooker" and appliance_id == "5" and question_id in ["4"]):
             #["2", "3", "4", "5"]): # ["1"]):
            #print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
            continue
        print("processing: ", appliance_type, appliance_id, testcase_difficulty, question_id)
        testcases_result_filepath_specific = testcases_result_filepath.replace("zzzzz", question_id) 
        test_one_single_testcase_multiple_trials(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepath_specific,prompt_filepaths, grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose = verbose)
        



def test_one_appliance_instance(appliance_type, appliance_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths,grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose = False):

    var_testcases_result_filepath = output_result_filepath_placeholder.replace("hhhhh", "_1_var_testcases")

    test_one_appliance_instance_multiple_testcases(appliance_type, appliance_id, "var", user_manual_filepath,  oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, var_testcases_result_filepath, prompt_filepaths, grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose =verbose)

    

def test_one_appliance_type(appliance_type, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths, grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose = False):

    appliance_ids = os.listdir(os.path.dirname(oracle_appliance_code_filepath))
    appliance_ids = sorted([f[:-3].split("_")[-1] for f in appliance_ids if re.fullmatch(r'_\d\.py', f)])
    
    filepaths = {
        "user_manual_filepath": user_manual_filepath,
        "oracle_appliance_code_filepath": oracle_appliance_code_filepath,
        "var_testcase_input_filepath": var_testcase_input_filepath,
        "output_result_filepath_placeholder": output_result_filepath_placeholder,
        "grounding_mapping_filepath": grounding_mapping_filepath,
        "action_filepath": action_option_filepath
    }

    for appliance_id in appliance_ids:
        updated_filepaths = replace_placeholder_in_filepaths(filepaths, "yyyyy", appliance_id)
        print("appliance_id: ", appliance_id)
        if not any(s in appliance_id for s in ["5"]):
            continue

        test_one_appliance_instance(
            appliance_type, appliance_id, updated_filepaths["user_manual_filepath"], updated_filepaths["oracle_appliance_code_filepath"], template_code_filepaths,
            updated_filepaths["var_testcase_input_filepath"], updated_filepaths["output_result_filepath_placeholder"],
            prompt_filepaths,
            updated_filepaths["grounding_mapping_filepath"],updated_filepaths["action_filepath"], trial_rounds_per_testcase, gpt_model_type, verbose=verbose
        ) 

def test_all_appliance_types(user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths, grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose = False):

    

    parent_dir = os.path.dirname(os.path.dirname(oracle_appliance_code_filepath))
    appliance_types = os.listdir(parent_dir)
    
    filepaths = {
        "user_manual_filepath": user_manual_filepath,
        "oracle_appliance_code_filepath": oracle_appliance_code_filepath,
        "var_testcase_input_filepath": var_testcase_input_filepath,
        
        "output_result_filepath_placeholder": output_result_filepath_placeholder,
        "grounding_mapping_filepath": grounding_mapping_filepath,
        "action_option_filepath": action_option_filepath
    }

    for appliance_type in appliance_types:
        updated_filepaths = replace_placeholder_in_filepaths(filepaths, "xxxxx", appliance_type)
        
        test_one_appliance_type(
            appliance_type, updated_filepaths["user_manual_filepath"], updated_filepaths["oracle_appliance_code_filepath"], template_code_filepaths,
            updated_filepaths["var_testcase_input_filepath"], updated_filepaths["output_result_filepath_placeholder"],
            prompt_filepaths,
            updated_filepaths["grounding_mapping_filepath"], updated_filepaths["action_option_filepath"], trial_rounds_per_testcase, gpt_model_type, verbose=verbose
        )

def test_one_single_testcase_multiple_trials(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, testcases_result_filepath,prompt_filepaths, grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose = False):

    log_record = {}
    log_record["command_id"] = testcase_info["id"]
    log_record["command_string"] = testcase_info["command"]
    log_record["ground_truth_goal_state"] = testcase_info["important_target_states"] 
    log_record["execution_results"] = []
    print(f"command: {appliance_type}/{appliance_id}/{question_id}: {testcase_info['command']}")
    for i in range(trial_rounds_per_testcase):
        log_record_per_round = test_one_single_testcase_single_trial(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, prompt_filepaths, grounding_mapping_filepath, action_option_filepath, gpt_model_type, verbose = verbose)
        log_record_per_round["execution_round_index"] = i + 1 
        log_record["execution_results"].append(log_record_per_round)
        pass
    
    create_or_replace_path(testcases_result_filepath)
    with open(testcases_result_filepath, "w") as f:
        json.dump(log_record, f, indent = 4)

def test_one_single_testcase_single_trial(appliance_type, appliance_id, question_id, user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, testcase_info, prompt_filepaths,grounding_mapping_filepath, action_option_filepath, gpt_model_type, verbose = False):

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
    user_manual_relevant_text = gpt_model.chat_with_text(prompt, gpt_model_type = gpt_model_type)


    action_option_text = load_string_from_file(action_option_filepath) 
    
    oracle_appliance_code = prepare_oracle_simulator(template_code_filepaths, oracle_appliance_code_filepath)

    oracle_globals = {}
    exec(oracle_appliance_code, oracle_globals)
    ApplianceSimulator = oracle_globals.get('Oracle', None)
    appliance_simulator = ApplianceSimulator()

    replacement_dict = {
    "hhhhh": action_option_text,
    "zzzzz": command_string,
    "xxxxx": user_manual_relevant_text,
    "$$$$$gpt_model_type": gpt_model_type
    }
    appliance_simulator, conversation_history, termination_flag, current_observation, prompt_initialised_context, proposed_action, reasoning, grounded_action = propose_action(
        appliance_simulator, 
        prompt_execute_command_context_text, 
        replacement_dict, 
        grounding_mapping_filepath, 
        setting = "UR_LP",
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
            "$$$$$gpt_model_type": gpt_model_type
        }

        print("current_observation in dialogue: ", current_observation)
        appliance_simulator, conversation_history, termination_flag, current_observation, _, proposed_action, reasoning, grounded_action = propose_action(
            appliance_simulator, 
            prompt_execute_command_dialogue_text, 
            replacement_dict, 
            grounding_mapping_filepath, 
            setting = "UR_LP",
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

    gpt_model_type = "gpt-4o-2024-11-20"
    # srun -u -o "cot-action-log.out" -w crane2 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 
    
    # This File evaluates: VLM with no user manual, no intermediate reasoning. 
    
    # user manual text 
    user_manual_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_1_user_manual/_2_text/xxxxx/_yyyyy.txt")

    # appliance simulator 
    template_code_root = os.path.expanduser("~/TextToActions/code/simulated/samples")
    template_code_filepaths = [os.path.join(template_code_root, f) for f in ["_1_variables.py", "_2_features.py", "_3_actions.py"]]
    oracle_appliance_code_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_3_simulators/_4_simulators_with_states_and_display/xxxxx/_yyyyy.py")

    # testcase input data
    testcase_filepath_placeholder = os.path.expanduser("~/TextToActions/datasetv2/simulated/_3_simulators/_5_testcases/hhhhh/xxxxx/_yyyyy.py")
    var_testcase_input_filepath = testcase_filepath_placeholder.replace("hhhhh", "_4_testcases_var_formatted")

    # testcase output result 
    output_result_filepath_placeholder = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_2_HV_M_UR_LP/{gpt_model_type}/xxxxx/yyyyy/hhhhh/zzzzz/_0_log_record.json")
   

    # prompt
    prompt_root_dir = os.path.expanduser("~/TextToActions/code/simulated/prompts/paper_exp/baselines_v1/_2_HV_M_UR_LP")
    prompt_filepaths = {
    "execute_command_context": os.path.join(prompt_root_dir, "_1_execute_command_context.txt"),
    "execute_command_dialogue": os.path.join(prompt_root_dir, "_2_execute_command_dialogue.txt"),
    "extract_relevant_user_manual": os.path.join(prompt_root_dir, "_0_extract_relevant_user_manual.txt"),
    }

    # proposed_actions  
    grounding_mapping_filepath = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_4_visual_grounding/{gpt_model_type}/_1_action_names/_3_proposed_to_oracle_action_mapping/xxxxx/yyyyy.json")
    action_option_filepath= os.path.expanduser(f'~/TextToActions/datasetv2/simulated/_4_visual_grounding/{gpt_model_type}/_1_action_names/_1_proposed_action_names/xxxxx/_yyyyy.txt')

    # test param 
    trial_rounds_per_testcase = 1

    test_all_appliance_types(user_manual_filepath, oracle_appliance_code_filepath, template_code_filepaths, var_testcase_input_filepath, output_result_filepath_placeholder, prompt_filepaths, grounding_mapping_filepath, action_option_filepath, trial_rounds_per_testcase, gpt_model_type, verbose = False)


    
