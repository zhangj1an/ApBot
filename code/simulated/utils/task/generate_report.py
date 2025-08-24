import os
import json
import sys
import numpy as np
from statistics import stdev
import pprint
import ast
import re
# Add the desired path
sys.path.append(os.path.expanduser("~/TextToActions/code/simulated"))
from utils.extract_list_from_file import extract_list_from_file
def batch_generate_report_for_one_gpt_model_type_for_var_size(testcase_optimal_step_length_dir, input_dir, output_filepath):
    machine_types = os.listdir(input_dir) 
    overall_report = {
        "results_by_appliance_type": {},
        "steps_by_appliance_type": {},
        "s_nipl_by_appliance_type": {},
        "results": {},
        "steps": {},
        "s_nipl": {},
        "results_details": {},
        "steps_details": {},
        "s_nipl_details": {}
    }

    all_results, all_steps, all_s_nipl = [], [], []

    appliance_results = {}
    appliance_steps = {}
    appliance_s_nipl = {}

    #for appliance in ["dehumidifier", "bottle_washer", "rice_cooker", "microwave_oven", "bread_maker", "washing_machine"]:
    for appliance in ["blender", "water_dispenser", "induction_cooker"]:
        overall_report["results_by_appliance_type"][appliance] = 0
        overall_report["steps_by_appliance_type"][appliance] = 0
        overall_report["s_nipl_by_appliance_type"][appliance] = 0
        overall_report["results_details"][appliance] = {}
        overall_report["steps_details"][appliance] = {}
        overall_report["s_nipl_details"][appliance] = {}
        appliance_results[appliance] = []
        appliance_steps[appliance] = []
        appliance_s_nipl[appliance] = []

    for machine_type in machine_types:
        machine_type_dir = os.path.join(input_dir, machine_type) 
        testcase_machine_type_dir = os.path.join(testcase_optimal_step_length_dir, machine_type)
        machine_ids = os.listdir(machine_type_dir)
        for machine_id in machine_ids:
            print(f"summarising results for {machine_type}, id {machine_id}")
            machine_id_dir = os.path.join(machine_type_dir, machine_id)
            testcase_machine_id_filepath = os.path.join(testcase_machine_type_dir, "_" + machine_id + ".py")
            score, steps_taken, s_nipl = generate_report_for_one_appliance_for_var_size(testcase_machine_id_filepath, machine_id_dir)
            print(f"score: {score}, steps_taken: {steps_taken}, s_nipl: {s_nipl}")
            selected_dict_key = next((key for key in overall_report["results_by_appliance_type"] if key in machine_type_dir), None)
            if selected_dict_key is not None: 
                scores = list(score.values())
                steps = list(steps_taken.values())
                s_nipls = list(s_nipl.values())

                overall_report["results_by_appliance_type"][selected_dict_key] += np.mean(scores)
                overall_report["steps_by_appliance_type"][selected_dict_key] += np.mean(steps)
                overall_report["s_nipl_by_appliance_type"][selected_dict_key] += np.mean(s_nipls)

                appliance_results[selected_dict_key].extend(scores)
                appliance_steps[selected_dict_key].extend(steps)
                appliance_s_nipl[selected_dict_key].extend(s_nipls)

                
                overall_report["results_details"][selected_dict_key][machine_id] = {"detail": score, "avg": round(np.mean(scores), 2), "std": round(stdev(scores), 2)}
                overall_report["steps_details"][selected_dict_key][machine_id] = {"detail": steps_taken, "avg": round(np.mean(steps), 2), "std": round(stdev(steps), 2)}
                overall_report["s_nipl_details"][selected_dict_key][machine_id] = {"detail": s_nipl, "avg": round(np.mean(s_nipls), 2), "std": round(stdev(s_nipls), 2)}

                all_results.extend(scores)
                all_steps.extend(steps)
                all_s_nipl.extend(s_nipls)

    for appliance in appliance_results:
        overall_report["results_by_appliance_type"][appliance] = {
            "avg": round(np.mean(appliance_results[appliance]), 3),
            "std": round(stdev(appliance_results[appliance]), 3)
        }
        overall_report["steps_by_appliance_type"][appliance] = {
            "avg": round(np.mean(appliance_steps[appliance]), 3),
            "std": round(stdev(appliance_steps[appliance]), 3)
        }
        overall_report["s_nipl_by_appliance_type"][appliance] = {
            "avg": round(np.mean(appliance_s_nipl[appliance]), 3),
            "std": round(stdev(appliance_s_nipl[appliance]), 3)
        }

    overall_report["results"]["avg"] = round(np.mean(all_results), 3)
    overall_report["steps"]["avg"] = round(np.mean(all_steps), 3)
    overall_report["s_nipl"]["avg"] = round(np.mean(all_s_nipl), 3)
    overall_report["results"]["std"] = round(stdev(all_results), 3)
    overall_report["steps"]["std"] = round(stdev(all_steps), 3)
    overall_report["s_nipl"]["std"] = round(stdev(all_s_nipl), 3)

    with open(output_filepath, "w") as f:
        json.dump(overall_report, f, indent=2)

    return overall_report


def batch_generate_report_for_one_gpt_model_type_for_easy_hard_ambi(input_dir, output_filepath):
    machine_types = os.listdir(input_dir) 
    overall_report = {}
    overall_report["results_by_appliance_type"] = {"microwave": 0, "washing_machine": 0, "rice_cooker": 0, "air_purifier": 0, "avg": 0}
    overall_report["steps_by_appliance_type"] = {"microwave": 0, "washing_machine": 0, "rice_cooker": 0, "air_purifier": 0, "avg": 0}
    overall_report["results_by_testcase_difficulty"] = {"easy": 0, "hard": 0, "ambiguous": 0, "avg": 0}
    overall_report["steps_by_testcase_difficulty"] = {"easy": 0, "hard": 0, "ambiguous": 0, "avg": 0}
    overall_report["results_details"] = {"microwave": {}, "washing_machine": {}, "rice_cooker": {}, "air_purifier": {}}
    overall_report["steps_details"] = {"microwave": {}, "washing_machine": {}, "rice_cooker": {}, "air_purifier": {}}
    for machine_type in machine_types:
        machine_type_dir = os.path.join(input_dir, machine_type) 
        machine_ids = os.listdir(machine_type_dir)
        for machine_id in machine_ids:
            print(f"summarising results for {machine_type}, id {machine_id}")
            machine_id_dir = os.path.join(machine_type_dir, machine_id)
            easy_score, hard_score, ambi_score, easy_steps_taken, hard_steps_taken, ambi_steps_taken = generate_report_for_one_appliance(machine_id_dir)
            selected_dict_key = next((key for key in overall_report["results_by_appliance_type"] if key in machine_type_dir), None)
            if selected_dict_key is not None: 
                overall_report["results_by_appliance_type"][selected_dict_key] += (sum(easy_score.values()) + sum(hard_score.values()) + sum(ambi_score.values()))/15/5 # needs to divide by 3 then divide by 5 then divide by 5; 3 testcase difficulties and 5 instances of this type, divide by 5 commands to get percentage
                overall_report["steps_by_appliance_type"][selected_dict_key] += (sum(easy_steps_taken.values()) + sum(hard_steps_taken.values()) + sum(ambi_steps_taken.values()))/15/5
                
                overall_report["results_by_testcase_difficulty"]["easy"] += (sum(easy_score.values()))/20/5 # needs to divide by 5 then divide by 4 then divide by 5; 5 appliance type and each type has 4 instances; 5 commands to get percentage
                overall_report["results_by_testcase_difficulty"]["hard"] += (sum(hard_score.values()))/20/5
                overall_report["results_by_testcase_difficulty"]["ambiguous"] += (sum(ambi_score.values()))/20/5
                overall_report["steps_by_testcase_difficulty"]["easy"] += (sum(easy_steps_taken.values()))/20/5
                overall_report["steps_by_testcase_difficulty"]["hard"] += (sum(hard_steps_taken.values()))/20/5
                overall_report["steps_by_testcase_difficulty"]["ambiguous"] += (sum(ambi_steps_taken.values()))/20/5

                overall_report["results_details"][selected_dict_key][machine_id] = {}
                overall_report["results_details"][selected_dict_key][machine_id]["easy"] = easy_score
                overall_report["results_details"][selected_dict_key][machine_id]["hard"] = hard_score
                overall_report["results_details"][selected_dict_key][machine_id]["ambiguous"] = ambi_score
                overall_report["results_details"][selected_dict_key][machine_id]["avg"] = round((sum(easy_score.values()) + sum(hard_score.values()) + sum(ambi_score.values()))/15, 2)
                
                overall_report["steps_details"][selected_dict_key][machine_id] = {}
                overall_report["steps_details"][selected_dict_key][machine_id]["easy"] = easy_steps_taken
                overall_report["steps_details"][selected_dict_key][machine_id]["hard"] = hard_steps_taken
                overall_report["steps_details"][selected_dict_key][machine_id]["ambiguous"] = ambi_steps_taken
                overall_report["steps_details"][selected_dict_key][machine_id]["avg"] = round((sum(easy_steps_taken.values()) + sum(hard_steps_taken.values()) + sum(ambi_steps_taken.values()))/15, 2)
               
                
                
    overall_report["results_by_appliance_type"]["avg"] = (overall_report["results_by_appliance_type"]["microwave"] + overall_report["results_by_appliance_type"]["washing_machine"] + overall_report["results_by_appliance_type"]["rice_cooker"] + overall_report["results_by_appliance_type"]["air_purifier"]) / 4
    overall_report["results_by_testcase_difficulty"]["avg"] = (overall_report["results_by_testcase_difficulty"]["easy"] + overall_report["results_by_testcase_difficulty"]["hard"] + overall_report["results_by_testcase_difficulty"]["ambiguous"]) / 3
    overall_report["steps_by_appliance_type"]["avg"] = (overall_report["steps_by_appliance_type"]["microwave"] + overall_report["steps_by_appliance_type"]["washing_machine"] + overall_report["steps_by_appliance_type"]["rice_cooker"] + overall_report["steps_by_appliance_type"]["air_purifier"]) / 4 
    overall_report["steps_by_testcase_difficulty"]["avg"] = (overall_report["steps_by_testcase_difficulty"]["easy"] + overall_report["steps_by_testcase_difficulty"]["hard"] + overall_report["steps_by_testcase_difficulty"]["ambiguous"]) / 3

    # Explicitly modify only the four specified keys
    keys_to_modify = [
        "results_by_appliance_type",
        "steps_by_appliance_type",
        "results_by_testcase_difficulty",
        "steps_by_testcase_difficulty"
    ]

    for key in keys_to_modify:
        if key in overall_report:
            overall_report[key] = {sub_key: round(value, 2) for sub_key, value in overall_report[key].items()}

    with open(output_filepath, "w") as f:
        json.dump(overall_report, f, indent=4)
    return overall_report


    
    #[os.path.join(input_dir, machine_type) for machine_type in  if os.path.isdir(os.path.join(input_dir, machine_type))]

    pass 

def generate_report_for_one_appliance_for_var_size(testcase_machine_id_filepath, input_dir):
    testcase_info = extract_list_from_file(testcase_machine_id_filepath)
    testcase_types = [testcase_type for testcase_type in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, testcase_type))] 
    score = {}
    steps_taken = {}
    s_nipl_dict = {}
    for testcase_type in testcase_types:
        testcase_type_dir = os.path.join(input_dir, testcase_type) 
        testcase_ids = [testcase_id for testcase_id in os.listdir(testcase_type_dir) if os.path.isdir(os.path.join(testcase_type_dir, testcase_id))]
        for testcase_id in testcase_ids:
            testcase_id_dir = os.path.join(testcase_type_dir, testcase_id)
            if any(s in testcase_id_dir for s in ["_10_oracle_V_proposed_M", "_9_oracle_V_oracle_M", "_5_HV_M_SR_LP_CL", "_4_M_SR_MA", "_8_HV_M_SR_MA_OL"]):
                log_record_filepath = os.path.join(testcase_id_dir, "1/_3_log_record.json") 
            elif any(s in testcase_id_dir for s in ["_7_HV_M_UR_MA"]):
                log_record_filepath = os.path.join(testcase_id_dir, "1/_1_log_record.json")
            elif any(s in testcase_id_dir for s in ["_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]):
                log_record_filepath = os.path.join(testcase_id_dir, "_0_log_record.json")
            print("processing testcase id: ", testcase_id)
            with open(log_record_filepath, "r") as f: 
                log_record = json.load(f)
                steps = 0 
                if any(s in testcase_id_dir for s in ["_10_oracle_V_proposed_M", "_9_oracle_V_oracle_M", "_5_HV_M_SR_LP_CL", "_4_M_SR_MA", "_7_HV_M_UR_MA", "_8_HV_M_SR_MA_OL"]):
                    if "execution_history" in log_record:
                        #steps = len(log_record["execution_history"])
                        steps = log_record["step_size"]
                elif any(s in testcase_id_dir for s in ["_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]):
                    steps = log_record["step_size"]
                    #steps = len(log_record["execution_results"][0]["execution_history"])

                if any(s in testcase_id_dir for s in ["_10_oracle_V_proposed_M", "_9_oracle_V_oracle_M", "_5_HV_M_SR_LP_CL", "_4_M_SR_MA", "_7_HV_M_UR_MA", "_8_HV_M_SR_MA_OL"]):
                    score_digit = log_record["score"]
                elif any(s in testcase_id_dir for s in ["_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]):
                    score_digit = log_record["execution_results"][0]["score"]

                score[testcase_id] = score_digit
                steps_taken[testcase_id] = steps
                if steps == 0:
                    s_nipl = score_digit
                else:
                    s_nipl = score_digit * min(1, testcase_info[int(testcase_id)-1]["optimal_step_size"] / steps)
                s_nipl_dict[testcase_id] = s_nipl

    return score, steps_taken, s_nipl_dict 

def generate_report_for_one_appliance(input_dir):
    # a single appliance will have easy, hard, ambiguous testcases. 
    # for setting of NV_M_UR_LP, output is just _0_log_record.json.
    # just get: "execution results avg step (len of execution history)","score"
    # list easy, hard, ambiguous testcases 
    testcase_types = [testcase_type for testcase_type in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, testcase_type))] 
    easy_score = {}
    hard_score = {}
    ambi_score = {} 
    easy_steps_taken = {}
    hard_steps_taken = {}
    ambi_steps_taken = {}
    for testcase_type in testcase_types:
        testcase_type_dir = os.path.join(input_dir, testcase_type) 
        testcase_ids = [testcase_id for testcase_id in os.listdir(testcase_type_dir) if os.path.isdir(os.path.join(testcase_type_dir, testcase_id))]
        for testcase_id in testcase_ids:
            testcase_id_dir = os.path.join(testcase_type_dir, testcase_id)
            log_record_filepath = os.path.join(testcase_id_dir, "1/_3_log_record.json") # "1/_3_log_record.json"
            with open(log_record_filepath, "r") as f: 
                log_record = json.load(f)
                #log_record = log_record["execution_results"][0]
                steps = 0 
                if "execution_history" in log_record:
                    steps = len(log_record["execution_history"])
                #steps = len(log_record["execution_results"][0]["execution_history"])
                
                #score = log_record["execution_results"][0]["score"]
                score = log_record["score"]
                if "easy" in testcase_type:
                    easy_score[testcase_id] = score
                    easy_steps_taken[testcase_id] = steps
                elif "hard" in testcase_type:
                    hard_score[testcase_id] = score
                    hard_steps_taken[testcase_id] = steps
                elif "ambiguous" in testcase_type:
                    ambi_score[testcase_id] = score
                    ambi_steps_taken[testcase_id] = steps
                
        #testcase_id_dirs = 
    print(f"easy_score: {easy_score}, steps: {easy_steps_taken}\n hard_score: {hard_score}, steps: {hard_steps_taken}\n ambi_score: {ambi_score}, steps: {ambi_steps_taken}")
    return (easy_score, hard_score, ambi_score, easy_steps_taken, hard_steps_taken, ambi_steps_taken)
    pass 


def extract_execution_times(action):
    match = re.search(r"(execution_times\s*=\s*(\d+))|(execution times\s*:\s*(\d+))", action)
    if match:
        # Depending on which pattern matched, group(2) or group(4) will have the number
        return int(match.group(2) or match.group(4))
    else:
        return 1

def get_step_size_from_file(file_path, feature_name, step_index):
    with open(file_path, 'r') as f:
        file_content = f.read()

    # Step 1: Extract from feature_list= { up to 'simulator_feature' (but not including it)
    match = re.search(r'(feature_list\s*=.*?)(?=\n\s*simulator_feature)', file_content, re.DOTALL)
    if not match:
        raise ValueError("feature_list block not found in the file.")
    
    feature_list_code = match.group(1)
    # Step 2: Add the extra line BEFORE
    complete_code = "meta_actions_on_number = 'empty'\n" + feature_list_code
    # Step 2: Execute this safely
    local_vars = {}
    exec(complete_code, {}, local_vars)

    feature_list = local_vars.get('feature_list', {})

    # Step 3: Now lookup
    feature_steps = feature_list.get(feature_name, [])
    for step_info in feature_steps:
        if step_info.get("step") == step_index:
            return step_info.get("step_size", 1)
    return 1  # fallback if not found

def obtain_step_size_for_one_testcase(method_name, filepath, oracle_model_filepath):

    if method_name in ["_9_oracle_V_oracle_M", "_8_HV_M_SR_MA_OL", "_7_HV_M_UR_MA", "_5_HV_M_SR_LP_CL", "_4_M_SR_MA", "_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]:
        with open(filepath, 'r') as f:
            data = json.load(f)

        total_steps = 0
        execution_history = data.get('execution_history', [])
        if len(execution_history) == 0:
            execution_history = data.get('execution_results', [{}])[0].get('execution_history', [])

        for step in execution_history:
            proposed_action = step.get('proposed_action', [])
            
            if isinstance(proposed_action, str):
                total_steps += extract_execution_times(proposed_action)
            elif isinstance(proposed_action, list) and len(proposed_action) >= 2 and isinstance(proposed_action[1], (int, float)):
                total_steps += proposed_action[1]
            else:
                total_steps += 1  # fallback if unexpected
            
            calibration_attempt = step.get('calibration_attempt', [])
            total_steps += len(calibration_attempt)
            mismatch_detection = step.get('mismatch', "")
            if mismatch_detection != "":
                #feature_name, step_index = step["current_observation"]["feature"]
                #added_step = get_step_size_from_file(oracle_model_filepath, feature_name, step_index)
                added_step = 0
                if "debug_record" in step:
                    added_step = len(step["debug_record"])
                total_steps += added_step

        return total_steps
    pass 
def save_python_list_full_indent(data, filename):
    # Dump as JSON pretty string with indent=4
    json_text = json.dumps(data, indent=4)
    # Replace JSON style (true, false, null) to Python style (True, False, None)
    python_text = (
        json_text
        .replace('true', 'True')
        .replace('false', 'False')
        .replace('null', 'None')
    )
    with open(filename, 'w') as f:
        f.write(python_text)
        f.write('\n')  # optional: add newline at end

def generate_optimal_step_size(testcase_optimal_step_length_dir=os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_5_testcases/_4_testcases_var_formatted"), input_dir=os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_6_results/_6_paper_exp/baselinesv1/_9_oracle_V_oracle_M/gpt-4o-2024-11-20")):
    # step size is calculated from perfect model, perfect perception baseline.
    machine_types = os.listdir(input_dir) 
    for machine_type in machine_types:
        machine_type_dir = os.path.join(input_dir, machine_type) 
        testcase_machine_type_dir = os.path.join(testcase_optimal_step_length_dir, machine_type)
        machine_ids = os.listdir(machine_type_dir)
        for machine_id in machine_ids:
            print(f"computing optimal step size for {machine_type}, id {machine_id}")
            # baseline result filepath
            machine_id_dir = os.path.join(machine_type_dir, machine_id)
            testcase_machine_id_filepath = os.path.join(testcase_machine_type_dir, "_" + machine_id + ".py")
            testcase_info = extract_list_from_file(testcase_machine_id_filepath)
            testcase_types = [testcase_type for testcase_type in os.listdir(machine_id_dir) if os.path.isdir(os.path.join(machine_id_dir, testcase_type))] 
            print("testcase types: ", testcase_types)
            for testcase_type in testcase_types:
                testcase_type_dir = os.path.join(machine_id_dir, testcase_type) 
                testcase_ids = [testcase_id for testcase_id in os.listdir(testcase_type_dir) if os.path.isdir(os.path.join(testcase_type_dir, testcase_id))]
                for testcase_id in testcase_ids:
                    testcase_id_dir = os.path.join(testcase_type_dir, testcase_id)
                    log_record_filepath = os.path.join(testcase_id_dir, "1/_3_log_record.json") 
                    print("log record filepath: ", log_record_filepath)
                    with open(log_record_filepath, "r") as f: 
                        log_record = json.load(f)
                        steps = 0 
                        if "execution_history" in log_record:
                            steps = obtain_step_size_for_one_testcase("_9_oracle_V_oracle_M",log_record_filepath)
                            for testcase_data in testcase_info:
                                if str(testcase_data["id"]) == str(testcase_id):
                                    testcase_data["optimal_step_size"] = steps 
                                    del testcase_data["number_of_steps"]
            save_python_list_full_indent(testcase_info, testcase_machine_id_filepath)
    pass 

def batch_obtain_step_size_for_one_method(method_name, oracle_model_dir, baseline_result_dir):

    # step size is calculated from perfect model, perfect perception baseline.
    machine_types = os.listdir(input_dir) 
    for machine_type in machine_types:
        machine_type_dir = os.path.join(input_dir, machine_type) 
        testcase_machine_type_dir = os.path.join(baseline_result_dir, machine_type)
        machine_ids = os.listdir(machine_type_dir)
        for machine_id in machine_ids:
            print(f"computing optimal step size for {machine_type}, id {machine_id}")
            # baseline result filepath
            machine_id_dir = os.path.join(machine_type_dir, machine_id)
            testcase_machine_id_filepath = os.path.join(testcase_machine_type_dir, "_" + machine_id + ".py")
            
            testcase_types = [testcase_type for testcase_type in os.listdir(machine_id_dir) if os.path.isdir(os.path.join(machine_id_dir, testcase_type))] 
            print("testcase types: ", testcase_types)
            for testcase_type in testcase_types:
                testcase_type_dir = os.path.join(machine_id_dir, testcase_type) 
                testcase_ids = [testcase_id for testcase_id in os.listdir(testcase_type_dir) if os.path.isdir(os.path.join(testcase_type_dir, testcase_id))]
                oracle_model_filepath = os.path.join(oracle_model_dir, machine_type, f"_{machine_id}.py")
                for testcase_id in testcase_ids:
                    testcase_id_dir = os.path.join(testcase_type_dir, testcase_id)

                    if any(s in testcase_id_dir for s in ["_8_HV_M_SR_MA_OL", "_5_HV_M_SR_LP_CL", "_4_M_SR_MA", ]): 
                        log_record_filepath = os.path.join(testcase_id_dir, "1/_3_log_record.json") 
                    elif any(s in testcase_id_dir for s in ["_7_HV_M_UR_MA"]):
                        log_record_filepath = os.path.join(testcase_id_dir, "1/_1_log_record.json")
                    elif any(s in testcase_id_dir for s in ["_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]):
                        log_record_filepath = os.path.join(testcase_id_dir, "_0_log_record.json")
                        pass 

                    step_size = obtain_step_size_for_one_testcase(method_name,log_record_filepath, oracle_model_filepath)
                    with open(log_record_filepath, 'r') as f:
                        data = json.load(f)
                        data["step_size"] = step_size 
                    # write the data into log record file as json 
                    with open(log_record_filepath, 'w') as f:
                        json.dump(data, f, indent=4)

                        pass 

                    ########
                    """
                    if any(s in testcase_id_dir for s in ["_5_HV_M_SR_LP_CL", "_4_M_SR_MA", "_8_HV_M_SR_MA_OL"]):
                        log_record_filepath = os.path.join(testcase_id_dir, "1/_3_log_record.json") 
                    elif any(s in testcase_id_dir for s in ["_7_HV_M_UR_MA"]):
                        log_record_filepath = os.path.join(testcase_id_dir, "1/_1_log_record.json")
                    elif any(s in testcase_id_dir for s in ["_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]):
                        log_record_filepath = os.path.join(testcase_id_dir, "_0_log_record.json")

                    print("log record filepath: ", log_record_filepath)
                    obtain_step_size_for_one_testcase(method_name,log_record_filepath)
                    """


if __name__ == "__main__":
    
    #srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 

    gpt_model_type = "gpt-4o-2024-11-20"
    baseline_value_options = [ "_1_NV_M_UR_LP", "_4_M_SR_MA", ]#["_1_NV_M_UR_LP", "_2_HV_M_UR_LP", "_4_M_SR_MA", "_5_HV_M_SR_LP_CL", "_7_HV_M_UR_MA", "_8_HV_M_SR_MA_OL"] # , "_9_oracle_V_oracle_M", "_10_oracle_V_proposed_M"
 
    #generate_optimal_step_size()
    testcase_dir = os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_5_testcases/_4_testcases_var_formatted")
    oracle_model_dir = os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display")

    for baseline_value in baseline_value_options:
        print("##processing method: ", baseline_value)
        baseline_name = baseline_value
        #input_dir = os.path.expanduser(f"~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselinesv1/{baseline_name}/gpt-4o-2024-11-20/_2_washing_machine/0")
        output_filepath = os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_6_results/_6_paper_exp/baselinesv1/{baseline_name}/{gpt_model_type}_report.json")
        #generate_report_for_one_appliance(input_dir) 
        input_dir = os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_6_results/_6_paper_exp/baselinesv1/{baseline_name}/{gpt_model_type}")
        #if baseline_name == "_1_NV_M_UR_LP":
        #    batch_obtain_step_size_for_one_method(baseline_name, oracle_model_dir, input_dir)
        #batch_obtain_step_size_for_one_method(baseline_name, oracle_model_dir, input_dir)

        # compute 
        batch_generate_report_for_one_gpt_model_type_for_var_size(testcase_dir, input_dir, output_filepath)
    
    # calculate s-nipl: success * min (1, optimal step / actual step)