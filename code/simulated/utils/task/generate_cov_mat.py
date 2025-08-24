import os
import json
import sys

# Add the desired path
sys.path.append(os.path.expanduser("~/TextToActions/code/simulated"))

import json
import os
import itertools
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
from scipy.stats import chi2_contingency

def chi2_test_between_methods_by_appliance(method_list, output_dir, filename_prefix):
    """
    Args:
        method_list: list of (method_name, filepath) tuples
        output_dir: where to save the results
        filename_prefix: prefix for filenames
    Outputs:
        For each appliance type:
            - Saves a heatmap '{output_dir}/{filename_prefix}_{appliance}_cov_mat.png'
        Also saves:
            - '{output_dir}/{filename_prefix}_chi2_results_by_appliance.json' with all details
    """
    appliance_types = [
        "dehumidifier",
        "bottle_washer",
        "rice_cooker",
        "microwave_oven",
        "bread_maker",
        "washing_machine"
    ]

    os.makedirs(output_dir, exist_ok=True)

    # Load all methods' accuracies
    method_scores = {}
    for method_name, filepath in method_list:
        with open(filepath, 'r') as f:
            data = json.load(f)
        scores = {}
        for appliance in appliance_types:
            scores[appliance] = data['results_by_appliance_type'][appliance]
        method_scores[method_name] = scores

    method_names = list(method_scores.keys())
    n_methods = len(method_names)

    results_json = {}

    for appliance in appliance_types:
        p_value_matrix = np.ones((n_methods, n_methods))
        chi2_matrix = np.zeros((n_methods, n_methods))
        significance_matrix = np.zeros((n_methods, n_methods))

        results_json[appliance] = {}

        for i, j in itertools.combinations(range(n_methods), 2):
            method_i = method_names[i]
            method_j = method_names[j]
            acc_i = method_scores[method_i][appliance]
            acc_j = method_scores[method_j][appliance]

            # Assume 300 samples per method
            success_i = int(acc_i * 300)
            success_j = int(acc_j * 300)
            fail_i = 300 - success_i
            fail_j = 300 - success_j

            contingency_table = np.array([
                [success_i, fail_i],
                [success_j, fail_j]
            ])

            chi2, p, _, _ = chi2_contingency(contingency_table)

            # Fill matrices
            chi2_matrix[i, j] = chi2
            chi2_matrix[j, i] = chi2

            p_value_matrix[i, j] = p
            p_value_matrix[j, i] = p

            significance = int(p < 0.05)
            significance_matrix[i, j] = significance
            significance_matrix[j, i] = significance

            # Save result
            results_json[appliance][f"{method_i} vs {method_j}"] = {
                "chi2_value": chi2,
                "p_value": p,
                "significant": significance == 1
            }

        # === Plot heatmap per appliance ===
        cmap = mcolors.ListedColormap(["green", "blue"])
        bounds = [0, 0.05, 1]
        norm = mcolors.BoundaryNorm(bounds, cmap.N)

        plt.figure(figsize=(10, 8))
        sns.heatmap(
            p_value_matrix, 
            xticklabels=method_names, 
            yticklabels=method_names, 
            annot=True, 
            fmt=".3f", 
            cmap=cmap, 
            norm=norm,
            cbar=True,
            cbar_kws={"ticks": [0.025, 0.525], "label": "p-value"}
        )
        plt.title(f"p-value matrix for {appliance}\n(Green: p<0.05 Significant, Blue: p>0.05 Not Significant)")
        plt.xticks(rotation=45, ha="right")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"{filename_prefix}_{appliance}_cov_mat.png"), bbox_inches='tight')
        plt.close()

    # === Save full JSON ===
    with open(os.path.join(output_dir, f"{filename_prefix}_chi2_results_by_appliance.json"), "w") as f:
        json.dump(results_json, f, indent=4)

    print(f"Saved all heatmaps and {filename_prefix}_chi2_results_by_appliance.json into {output_dir}.")

def chi2_test_between_methods_avg(method_list, output_dir, filename):
    """
    Args:
        method_list: list of (method_name, filepath) tuples
    Outputs:
        Saves a heatmap 'cov_mat.png' and a json 'chi2_results.json' with pairwise chi2, p-value, significance
    """
    method_scores = {}
    for method_name, filepath in method_list:
        with open(filepath, 'r') as f:
            data = json.load(f)
        acc = data['results_by_appliance_type']['avg']
        method_scores[method_name] = acc

    method_names = list(method_scores.keys())
    n_methods = len(method_names)

    p_value_matrix = np.ones((n_methods, n_methods))
    chi2_matrix = np.zeros((n_methods, n_methods))
    significance_matrix = np.zeros((n_methods, n_methods))

    results_json = {}

    for i, j in itertools.combinations(range(n_methods), 2):
        method_i = method_names[i]
        method_j = method_names[j]
        acc_i = method_scores[method_i]
        acc_j = method_scores[method_j]

        # Assume 300 samples per method
        success_i = int(acc_i * 300)
        success_j = int(acc_j * 300)
        fail_i = 300 - success_i
        fail_j = 300 - success_j

        contingency_table = np.array([
            [success_i, fail_i],
            [success_j, fail_j]
        ])

        chi2, p, _, _ = chi2_contingency(contingency_table)

        # Fill matrices
        chi2_matrix[i, j] = chi2
        chi2_matrix[j, i] = chi2

        p_value_matrix[i, j] = p
        p_value_matrix[j, i] = p

        significance = int(p < 0.05)
        significance_matrix[i, j] = significance
        significance_matrix[j, i] = significance

        # Save result
        results_json[f"{method_i} vs {method_j}"] = {
            "chi2_value": chi2,
            "p_value": p,
            "significant": significance == 1
        }

    # === Plot ===
    # Custom colormap: green for p < 0.05, blue otherwise
    cmap = mcolors.ListedColormap(["green", "blue"])
    bounds = [0, 0.05, 1]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    plt.figure(figsize=(10, 8))
    sns.heatmap(
        p_value_matrix, 
        xticklabels=method_names, 
        yticklabels=method_names, 
        annot=True, 
        fmt=".3f", 
        cmap=cmap, 
        norm=norm,
        cbar=True,
        cbar_kws={"ticks": [0.025, 0.525], "label": "p-value"}
    )
    plt.title("p-value matrix (Chi-square Test)\n(Green: p<0.05 Significant, Blue: p>0.05 Not Significant)")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{filename}_cov_mat.png"), bbox_inches='tight')
    plt.close()

    # === Save JSON ===
    with open(os.path.join(output_dir, f"{filename}_chi2_results.json"), "w") as f:
        json.dump(results_json, f, indent=4)

    print("Saved heatmap to cov_mat.png and detailed results to chi2_results.json.")



if __name__ == "__main__":
    root_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1")
    method_list = ["_1_NV_M_UR_LP", "_2_HV_M_UR_LP",  "_5_HV_M_SR_LP_CL", "_7_HV_M_UR_MA", "_8_HV_M_SR_MA_OL", "_4_M_SR_MA", "_10_oracle_V_proposed_M", "_9_oracle_V_oracle_M"]
    method_names = ["cot + image", "cot + action", "ours w/o button policy", "ours w/o structured reasoning", "ours w/o close loop update", "ours", "oracle P", "oracle P + M"]
    name_result_list = []
    for i, method in enumerate(method_list):
        method_path = os.path.join(root_dir, method)
        if not os.path.exists(method_path):
            print(f"Path {method_path} does not exist.")
            continue
        json_file = os.path.join(method_path, "gpt-4o-2024-11-20_report.json")
        if not os.path.exists(json_file):
            print(f"File {json_file} does not exist.")
            continue

        name_result_list.append((method_names[i], json_file))
    result_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_11_visualisation")
    #chi2_test_between_methods(name_result_list[:6], result_dir, "baselines")
    #chi2_test_between_methods_avg(name_result_list[-3:], result_dir, "error_analysis")
    #chi2_test_between_methods_by_appliance(name_result_list[:6], result_dir, "baselines")
    #chi2_test_between_methods_by_appliance(name_result_list[-3:], result_dir, "error_analysis")
        
    