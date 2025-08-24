import json
from scipy.stats import ttest_rel
import os
from collections import defaultdict
from math import isnan

def compute_f1(tp, fp, fn):
    if tp + fp == 0 or tp + fn == 0:
        return 0.0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)

def grounding_paired_t_test_f1_by_appliance_type(molmo_data_filepath, gpt_data_filepath, output_filepath="result.json"):

    with open(molmo_data_filepath, "r") as f:
        molmo_data = json.load(f)
    with open(gpt_data_filepath, "r") as f:
        gpt_data = json.load(f)
        
    grouped_gpt = defaultdict(list)
    grouped_molmo = defaultdict(list)
    overall_gpt = []
    overall_molmo = []

    # Helper to index by (machine_type, machine_id) for sorting consistency
    gpt_indexed = {(d["machine_type"], d["machine_id"]): d for d in gpt_data}
    molmo_indexed = {(d["machine_type"], d["machine_id"]): d for d in molmo_data}

    # Sort to ensure consistent pairing
    keys = sorted(gpt_indexed.keys())

    for key in keys:
        gpt = gpt_indexed[key]
        molmo = molmo_indexed[key]

        gpt_f1 = compute_f1(gpt["TP"], gpt["FP"], gpt["FN"])
        molmo_f1 = compute_f1(molmo["TP"], molmo["FP"], molmo["FN"])

        grouped_gpt[gpt["machine_type"]].append(gpt_f1)
        grouped_molmo[molmo["machine_type"]].append(molmo_f1)

        overall_gpt.append(gpt_f1)
        overall_molmo.append(molmo_f1)

    # Compute t-test and save results
    results = {}
    for machine_type in grouped_gpt:
        gpt_scores = grouped_gpt[machine_type]
        molmo_scores = grouped_molmo[machine_type]
        if all(abs(x - y) < 1e-10 for x, y in zip(gpt_scores, molmo_scores)):
            t_stat, p_val = 0.0, 1.0  # or custom handling
        else:
            t_stat, p_val = ttest_rel(gpt_scores, molmo_scores)
        
        results[machine_type] = {
            "t_statistic": t_stat,
            "p_value": p_val,
            "gpt_f1": gpt_scores,
            "molmo_f1": molmo_scores
        }

    # Overall t-test
    overall_t, overall_p = ttest_rel(overall_gpt, overall_molmo)
    results["overall"] = {
        "t_statistic": overall_t,
        "p_value": overall_p,
        "gpt_f1": overall_gpt,
        "molmo_f1": overall_molmo
    }
    # Write to file
    with open(output_filepath, 'w') as f:
        json.dump(results, f, indent=4)

    return results

def reasoning_paired_t_test_by_difficulty(ours_data_filepath, others_data_filepath, output_filepath="result_by_difficulty.json"):
    with open(ours_data_filepath, "r") as f:
        ours_data = json.load(f)
    with open(others_data_filepath, "r") as f:
        others_data = json.load(f)

    difficulty_levels = ["easy", "hard", "ambiguous"]
    result = {}
    p_values = []
    t_statistics = []

    for difficulty in difficulty_levels:
        ours_scores = []
        others_scores = []

        for appliance in ours_data["results_details"]:
            for instance_id in map(str, range(5)):
                if instance_id in ours_data["results_details"][appliance]:
                    if difficulty in ours_data["results_details"][appliance][instance_id]:
                        ours_instance_scores = ours_data["results_details"][appliance][instance_id][difficulty].values()
                        others_instance_scores = others_data["results_details"][appliance][instance_id][difficulty].values()
                        ours_scores.extend(list(ours_instance_scores))
                        others_scores.extend(list(others_instance_scores))

        t_stat, p_val = ttest_rel(ours_scores, others_scores)
        result[difficulty] = {
            "t_statistic": t_stat,
            "p_value": p_val
        }
        p_values.append(p_val)
        t_statistics.append(t_stat)

    result["average_p_value"] = sum(p_values) / len(p_values)
    result["average_t_statistic"] = sum(t_statistics) / len(t_statistics)

    with open(output_filepath, "w") as f:
        json.dump(result, f, indent=2)

    return result

def reasoning_paired_t_test_by_appliance_type_hard(ours_data_filepath, others_data_filepath, output_filepath="result.json"):

    with open(ours_data_filepath, "r") as f:
        ours_data = json.load(f)
    with open(others_data_filepath, "r") as f:
        cot_action_data = json.load(f)
    appliance_types = ["microwave", "washing_machine", "rice_cooker", "air_purifier"]
    result = {}

    p_values = []
    t_statistics = []

    for appliance in appliance_types:
        ours_scores = []
        cot_scores = []

        for instance_id in map(str, range(5)):
            for difficulty in ["hard"]:
                if instance_id in ours_data["results_details"][appliance]:
                    ours_instance_scores = ours_data["results_details"][appliance][instance_id][difficulty].values()
                    cot_instance_scores = cot_action_data["results_details"][appliance][instance_id][difficulty].values()

                    ours_scores.extend(list(ours_instance_scores))
                    cot_scores.extend(list(cot_instance_scores))
        #print("ours_scores, length", ours_scores, len(ours_scores))
        #print("cot_scores, length", cot_scores, len(cot_scores))
       
        t_stat, p_val = ttest_rel(ours_scores, cot_scores)
        result[appliance] = {
            "t_statistic": t_stat,
            "p_value": p_val
        }
        p_values.append(p_val)
        t_statistics.append(t_stat)

    result["average_p_value"] = sum(p_values) / len(p_values)
    result["average_t_statistic"] = sum(t_statistics) / len(t_statistics)

    with open(output_filepath, "w") as f:
        json.dump(result, f, indent=2)

    return result

def reasoning_paired_t_test_by_step_size(ours_data_filepath, cot_action_data_filepath, output_filepath):
    with open(ours_data_filepath, "r") as f:
        ours_dict = json.load(f)
    with open(cot_action_data_filepath, "r") as f:
        cot_action_dict = json.load(f)
    
    def extract_success_rates(data):
        return {
            k: v["success"] / v["total"] if v["total"] > 0 else 0.0
            for k, v in data.items()
        }

    ours_rates = extract_success_rates(ours_dict)
    cot_rates = extract_success_rates(cot_action_dict)

    # Collect matched keys (still strings, use int for comparisons)
    common_keys = sorted(set(ours_rates.keys()) & set(cot_rates.keys()), key=lambda x: int(x))
    
    group_lt_5 = [k for k in common_keys if int(k) < 5]
    group_5_to_10 = [k for k in common_keys if 5 <= int(k) <= 8]
    group_gt_10 = [k for k in common_keys if int(k) > 8]

    def get_rates(keys):
        ours = [ours_rates[k] for k in keys]
        cot = [cot_rates[k] for k in keys]
        return ours, cot

    results = {}

    def run_ttest(ours, cot):
        if len(ours) > 1:
            t_val, p_val = ttest_rel(ours, cot)
        else:
            t_val, p_val = None, None
        return {"t_value": t_val, "p_value": p_val}

    results["step_<5"] = run_ttest(*get_rates(group_lt_5))
    results["step_5_to_8"] = run_ttest(*get_rates(group_5_to_10))
    results["step_>8"] = run_ttest(*get_rates(group_gt_10))
    results["overall"] = run_ttest(*get_rates(common_keys))

    with open(output_filepath, "w") as f:
        json.dump(results, f, indent=2)

    return results

def reasoning_paired_t_test_by_step_size_grouped(ours_data_filepath, cot_action_data_filepath, output_filepath):
    with open(ours_data_filepath, "r") as f:
        ours_dict = json.load(f)
    with open(cot_action_data_filepath, "r") as f:
        cot_action_dict = json.load(f)
    
    def preprocess_dict(data):
        updated_dict = {}
        updated_dict["9-25"] = {"success": 0, "total": 0}
        for key, value in data.items():
            if int(key) < 9:
                updated_dict[key] = value
            else:
                updated_dict["9-25"]["success"] += value["success"]
                updated_dict["9-25"]["total"] += value["total"]
        return updated_dict
    
    ours_dict = preprocess_dict(ours_dict)
    cot_action_dict = preprocess_dict(cot_action_dict)
    print("ours_dict", ours_dict)
    print("cot_action_dict", cot_action_dict)
    exit()
    def extract_success_rates(data):
        return {
            k: v["success"] / v["total"] if v["total"] > 0 else 0.0
            for k, v in data.items()
        }

    ours_rates = extract_success_rates(ours_dict)
    cot_rates = extract_success_rates(cot_action_dict)

    # Collect matched keys (still strings, use int for comparisons)
    common_keys = sorted(set(ours_rates.keys()) & set(cot_rates.keys()), key=lambda x: int(x))
    
    group_lt_5 = [k for k in common_keys if int(k) < 5]
    group_5_to_10 = [k for k in common_keys if 5 <= int(k) <= 8]
    group_gt_10 = [k for k in common_keys if int(k) > 8]

    def get_rates(keys):
        ours = [ours_rates[k] for k in keys]
        cot = [cot_rates[k] for k in keys]
        return ours, cot

    results = {}

    def run_ttest(ours, cot):
        if len(ours) > 1:
            t_val, p_val = ttest_rel(ours, cot)
        else:
            t_val, p_val = None, None
        return {"t_value": t_val, "p_value": p_val}

    results["step_<5"] = run_ttest(*get_rates(group_lt_5))
    results["step_5_to_8"] = run_ttest(*get_rates(group_5_to_10))
    results["step_>8"] = run_ttest(*get_rates(group_gt_10))
    results["overall"] = run_ttest(*get_rates(common_keys))

    with open(output_filepath, "w") as f:
        json.dump(results, f, indent=2)

    return results


def reasoning_paired_t_test_by_appliance_type(ours_data_filepath, others_data_filepath, output_filepath="result.json"):

    with open(ours_data_filepath, "r") as f:
        ours_data = json.load(f)
    with open(others_data_filepath, "r") as f:
        cot_action_data = json.load(f)
    appliance_types = ["microwave", "washing_machine", "rice_cooker", "air_purifier"]
    result = {}

    p_values = []
    t_statistics = []

    for appliance in appliance_types:
        ours_scores = []
        cot_scores = []

        for instance_id in map(str, range(5)):
            for difficulty in ["easy", "hard", "ambiguous"]:
                if instance_id in ours_data["results_details"][appliance]:
                    ours_instance_scores = ours_data["results_details"][appliance][instance_id][difficulty].values()
                    cot_instance_scores = cot_action_data["results_details"][appliance][instance_id][difficulty].values()

                    ours_scores.extend(list(ours_instance_scores))
                    cot_scores.extend(list(cot_instance_scores))
        #print("ours_scores, length", ours_scores, len(ours_scores))
        #print("cot_scores, length", cot_scores, len(cot_scores))
       
        t_stat, p_val = ttest_rel(ours_scores, cot_scores)
        result[appliance] = {
            "t_statistic": t_stat,
            "p_value": p_val
        }
        p_values.append(p_val)
        t_statistics.append(t_stat)

    result["average_p_value"] = sum(p_values) / len(p_values)
    result["average_t_statistic"] = sum(t_statistics) / len(t_statistics)

    with open(output_filepath, "w") as f:
        json.dump(result, f, indent=2)

    return result

if __name__ == "__main__":

    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3

    output_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/summary/ours_vs_cot_action_by_step_size.json")
    pass 
    ours_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselines/_4_M_SR_MA/gpt-4o-2024-11-20_report.json")

    # cot-action
    others_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselines/_1_M_UR_LP/gpt-4o-2024-11-20_report.json")

    # cot-image
    #others_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselinesv1/_1_NV_M_UR_LP/gpt-4o-2024-11-20_report.json")

    #reasoning_paired_t_test_by_difficulty(ours_data_filepath, others_data_filepath, output_filepath)
    #reasoning_paired_t_test_by_appliance_type_hard(ours_data_filepath, others_data_filepath, output_filepath)

    ours_step_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_10_visualisation/_7_our_method_method_step_dict.json")
    others_step_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_10_visualisation/_7_cot_action_method_step_dict.json")
    reasoning_paired_t_test_by_step_size(ours_step_data_filepath, others_step_data_filepath, output_filepath)
    #reasoning_paired_t_test_by_step_size_grouped(ours_step_data_filepath, others_step_data_filepath, output_filepath)

    molmo_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_1_visual_grounding_action_results/molmo/_1_instance_level.json")
    gpt_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_1_visual_grounding_action_results/ours/_1_instance_level.json")
    grounding_result_data_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_1_visual_grounding_action_results/result_by_difficulty.json")
    #grounding_paired_t_test_f1_by_appliance_type(molmo_data_filepath, gpt_data_filepath, output_filepath=grounding_result_data_filepath)

    
