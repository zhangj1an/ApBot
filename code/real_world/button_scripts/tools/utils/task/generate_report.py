import os
import json
import sys

# Add the desired path
sys.path.append(os.path.expanduser("~/TextToActions/code/simulated"))
from utils.extract_list_from_file import extract_list_from_file
def batch_generate_report_for_one_gpt_model_type_for_var_size(testcase_optimal_step_length_dir, input_dir, output_filepath):
    machine_types = os.listdir(input_dir) 
    overall_report = {}
    overall_report["results_by_appliance_type"] = {"dehumidifier": 0, "bottle_washer": 0, "rice_cooker": 0, "microwave_oven": 0, "bread_maker": 0, "washing_machine": 0, "avg": 0}
    overall_report["steps_by_appliance_type"] = {"dehumidifier": 0, "bottle_washer": 0, "rice_cooker": 0, "microwave_oven": 0, "bread_maker": 0, "washing_machine": 0, "avg": 0}
    overall_report["s_nipl_by_appliance_type"] = {"dehumidifier": 0, "bottle_washer": 0, "rice_cooker": 0, "microwave_oven": 0, "bread_maker": 0, "washing_machine": 0, "avg": 0}
    overall_report["results"] = {"avg": 0}
    overall_report["steps"] = {"avg": 0}
    overall_report["s_nipl"] = {"avg": 0}
    overall_report["results_details"] = {"dehumidifier": {}, "bottle_washer": {}, "rice_cooker": {}, "microwave_oven": {}, "bread_maker": {}, "washing_machine": {}}
    overall_report["steps_details"] = {"dehumidifier": {}, "bottle_washer": {}, "rice_cooker": {}, "microwave_oven": {}, "bread_maker": {}, "washing_machine": {}}
    overall_report["s_nipl_details"] = {"dehumidifier": {}, "bottle_washer": {}, "rice_cooker": {}, "microwave_oven": {}, "bread_maker": {}, "washing_machine": {}}
    for machine_type in machine_types:
        machine_type_dir = os.path.join(input_dir, machine_type) 
        testcase_machine_type_dir = os.path.join(testcase_optimal_step_length_dir, machine_type)
        machine_ids = os.listdir(machine_type_dir)
        for machine_id in machine_ids:
            print(f"summarising results for {machine_type}, id {machine_id}")
            machine_id_dir = os.path.join(machine_type_dir, machine_id)
            testcase_machine_id_filepath = os.path.join(testcase_machine_type_dir, "_" + machine_id + ".py")
            score, steps_taken, s_nipl = generate_report_for_one_appliance_for_var_size(testcase_machine_id_filepath, machine_id_dir)
            selected_dict_key = next((key for key in overall_report["results_by_appliance_type"] if key in machine_type_dir), None)
            if selected_dict_key is not None: 
                overall_report["results_by_appliance_type"][selected_dict_key] += sum(score.values())/10/5 # needs to divide by 10 then divide by 5; 5 instances of this type, divide by 10 commands to get percentage
                overall_report["steps_by_appliance_type"][selected_dict_key] += sum(steps_taken.values())/10/5

                if sum(score.values()) != 0:
                    overall_report["s_nipl_by_appliance_type"][selected_dict_key] += sum(s_nipl.values())/sum(score.values())/5
                else:
                    overall_report["s_nipl_by_appliance_type"][selected_dict_key] += 0
                
                overall_report["results"]["avg"] += (sum(score.values()))/50/6 # needs to divide by 5 then divide by 6 then divide by 10; 6 appliance type and each type has 5 instances; 10 commands to get percentage
                
                overall_report["steps"]["avg"] += (sum(steps_taken.values()))/50/6

                if sum(score.values()) != 0:
                    overall_report["s_nipl"]["avg"] += (sum(s_nipl.values()))/sum(score.values())/5/6
                else:
                    overall_report["s_nipl"]["avg"] += 0
                
                overall_report["results_details"][selected_dict_key][machine_id] = {}
                overall_report["results_details"][selected_dict_key][machine_id]["detail"] = score
                overall_report["results_details"][selected_dict_key][machine_id]["avg"] = round(sum(score.values())/10, 2)
                
                overall_report["steps_details"][selected_dict_key][machine_id] = {}
                overall_report["steps_details"][selected_dict_key][machine_id]["detail"] = steps_taken
                overall_report["steps_details"][selected_dict_key][machine_id]["avg"] = round(sum(steps_taken.values() )/10, 2)

                overall_report["s_nipl_details"][selected_dict_key][machine_id] = {}
                overall_report["s_nipl_details"][selected_dict_key][machine_id]["detail"] = s_nipl
                if sum(score.values()) != 0:
                    overall_report["s_nipl_details"][selected_dict_key][machine_id]["avg"] = round(sum(s_nipl.values())/sum(score.values()), 2)
                else:
                    overall_report["s_nipl_details"][selected_dict_key][machine_id]["avg"] = 0
                
               
                
    #{"dehumidifier": {}, "bottle_washer": {}, "rice_cooker": {}, "microwave_oven": {}, "bread_maker": {}, "washing_machine": {}}            
    overall_report["results_by_appliance_type"]["avg"] = (overall_report["results_by_appliance_type"]["dehumidifier"] + overall_report["results_by_appliance_type"]["bottle_washer"] + overall_report["results_by_appliance_type"]["rice_cooker"] + overall_report["results_by_appliance_type"]["microwave_oven"] + overall_report["results_by_appliance_type"]["bread_maker"] + overall_report["results_by_appliance_type"]["washing_machine"]) / 6
    overall_report["steps_by_appliance_type"]["avg"] = (overall_report["steps_by_appliance_type"]["dehumidifier"] + overall_report["steps_by_appliance_type"]["bottle_washer"] + overall_report["steps_by_appliance_type"]["rice_cooker"] + overall_report["steps_by_appliance_type"]["microwave_oven"] + overall_report["steps_by_appliance_type"]["bread_maker"] + overall_report["steps_by_appliance_type"]["washing_machine"]) / 6 
    overall_report["s_nipl_by_appliance_type"]["avg"] = (overall_report["s_nipl_by_appliance_type"]["dehumidifier"] + overall_report["s_nipl_by_appliance_type"]["bottle_washer"] + overall_report["s_nipl_by_appliance_type"]["rice_cooker"] + overall_report["s_nipl_by_appliance_type"]["microwave_oven"] + overall_report["s_nipl_by_appliance_type"]["bread_maker"] + overall_report["s_nipl_by_appliance_type"]["washing_machine"]) / 6

    # Explicitly modify only the four specified keys
    keys_to_modify = [
        "results_by_appliance_type",
        "steps_by_appliance_type",
        "s_nipl_by_appliance_type",
    ]

    for key in keys_to_modify:
        if key in overall_report:
            overall_report[key] = {sub_key: round(value, 2) for sub_key, value in overall_report[key].items()}

    with open(output_filepath, "w") as f:
        json.dump(overall_report, f, indent=4)
    return overall_report


    
    #[os.path.join(input_dir, machine_type) for machine_type in  if os.path.isdir(os.path.join(input_dir, machine_type))]

    pass 


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
    # a single appliance will have easy, hard, ambiguous testcases. 
    # for setting of NV_M_UR_LP, output is just _0_log_record.json.
    # just get: "execution results avg step (len of execution history)","score", "s-nipl"
    # list easy, hard, ambiguous testcases 
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
            # ours: "1/_3_log_record.json" or cot-action: "_0_log_record.json"
            with open(log_record_filepath, "r") as f: 
                log_record = json.load(f)
                #log_record = log_record["execution_results"][0]
                steps = 0 
                #if "execution_history" in log_record:
                #    steps = len(log_record["execution_history"])
                #    pass 
                #steps = len(log_record["execution_results"][0]["execution_history"])
                
                if any(s in testcase_id_dir for s in ["_10_oracle_V_proposed_M", "_9_oracle_V_oracle_M", "_5_HV_M_SR_LP_CL", "_4_M_SR_MA", "_7_HV_M_UR_MA", "_8_HV_M_SR_MA_OL"]):
                    if "execution_history" in log_record:
                        steps = len(log_record["execution_history"])
                elif any(s in testcase_id_dir for s in ["_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]):
                    steps = len(log_record["execution_results"][0]["execution_history"])

                if any(s in testcase_id_dir for s in ["_10_oracle_V_proposed_M", "_9_oracle_V_oracle_M", "_5_HV_M_SR_LP_CL", "_4_M_SR_MA", "_7_HV_M_UR_MA", "_8_HV_M_SR_MA_OL"]):
                    score_digit = log_record["score"]
                elif any(s in testcase_id_dir for s in ["_2_HV_M_UR_LP", "_1_NV_M_UR_LP"]):
                    score_digit = log_record["execution_results"][0]["score"]
                    
                score[testcase_id] = score_digit
                steps_taken[testcase_id] = steps
                if steps == 0:
                    s_nipl = score_digit
                else:
                    s_nipl = score_digit * min(1, testcase_info[int(testcase_id)-1]["number_of_steps"] / steps)
                s_nipl_dict[testcase_id] = s_nipl

                
                
                
        #testcase_id_dirs = 
    print(f"score: {score}, steps: {steps_taken}, s-nipl: {s_nipl_dict}\n ")
    return (score, steps_taken, s_nipl_dict)
    pass 


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

if __name__ == "__main__":
    
    #srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 

    gpt_model_type = "gpt-4o-2024-11-20"
    baseline_name = "_10_oracle_V_proposed_M"#"_8_HV_M_SR_MA_OL" , "_1_NV_M_UR_LP", "_2_HV_M_UR_LP", "_4_M_SR_MA","_5_HV_M_SR_LP_CL", "_7_HV_M_UR_MA", "_9_oracle_V_oracle_M"
    #input_dir = os.path.expanduser(f"~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselinesv1/{baseline_name}/gpt-4o-2024-11-20/_2_washing_machine/0")
    output_filepath = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/{baseline_name}/{gpt_model_type}_report.json")
    #generate_report_for_one_appliance(input_dir) 

    input_dir = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/{baseline_name}/{gpt_model_type}")
    testcase_optimal_step_length_dir = os.path.expanduser(f"~/TextToActions/datasetv2/simulated/_3_simulators/_5_testcases/_4_testcases_var_formatted")
    #batch_generate_report_for_one_gpt_model_type(input_dir, output_filepath)
    batch_generate_report_for_one_gpt_model_type_for_var_size(testcase_optimal_step_length_dir, input_dir, output_filepath)
    
    # calculate s-nipl: success * min (1, optimal step / actual step)