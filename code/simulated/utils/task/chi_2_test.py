# compare between our method and cot-action method for data points. 
# split between step < 5, step >= 5, and overall result. 

# 
import os
import json
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import GofChisquarePower

def run_chi2_analysis(our_data_filepath, cot_data_filepath, output_result_filepath):
    with open(our_data_filepath, 'r') as f:
        our_data_dict = json.load(f)
    with open(cot_data_filepath, 'r') as f:
        cot_data_dict = json.load(f)

    def extract_binary_data(data_dict, keys):
        data = []
        for k in keys:
            if k in data_dict:
                s = data_dict[k]['success']
                t = data_dict[k]['total']
                data.extend([1] * s + [0] * (t - s))
        return data

    def chi2_from_binary(data1, data2):
        our_1s = sum(data1)
        our_0s = len(data1) - our_1s
        cot_1s = sum(data2)
        cot_0s = len(data2) - cot_1s
        table = [[our_1s, our_0s], [cot_1s, cot_0s]]
        chi2, p, dof, expected = chi2_contingency(table)

        acc_our = our_1s / len(data1)
        acc_cot = cot_1s / len(data2)

        required_n = estimate_required_sample_size(acc_our, acc_cot)

        return chi2, p, acc_our, acc_cot, required_n

    def estimate_required_sample_size(acc_our, acc_cot, alpha=0.05, power=0.8):
        effect_size = abs(acc_our - acc_cot)
        if effect_size == 0:
            return None  # Cannot detect 0 difference
        try:
            h = proportion_effectsize(acc_our, acc_cot)
            analysis = GofChisquarePower()
            sample_size = analysis.solve_power(effect_size=h, alpha=alpha, power=power)
            return int(sample_size * 2)  # Total size (both groups)
        except:
            return None

    keys_lt_5 = [k for k in our_data_dict if int(k) < 5]
    keys_ge_5 = [k for k in our_data_dict if 5 <= int(k) <= 100]
    all_keys = [k for k in our_data_dict if int(k) <= 100]

    our_lt_5 = extract_binary_data(our_data_dict, keys_lt_5)
    cot_lt_5 = extract_binary_data(cot_data_dict, keys_lt_5)
    our_ge_5 = extract_binary_data(our_data_dict, keys_ge_5)
    cot_ge_5 = extract_binary_data(cot_data_dict, keys_ge_5)
    our_all = extract_binary_data(our_data_dict, all_keys)
    cot_all = extract_binary_data(cot_data_dict, all_keys)

    results = {}

    chi2, p, acc_our, acc_cot, required_n = chi2_from_binary(our_lt_5, cot_lt_5)
    results['step_size_<5'] = {
        'chi2': chi2,
        'p': p,
        'significant': "yes" if p < 0.05 else "no",
        'data_size': len(our_lt_5),
        'our_accuracy': acc_our,
        'cot_accuracy': acc_cot,
        'required_data_size': required_n
    }

    chi2, p, acc_our, acc_cot, required_n = chi2_from_binary(our_ge_5, cot_ge_5)
    results['step_size_>=5'] = {
        'chi2': chi2,
        'p': p,
        'significant': "yes" if p < 0.05 else "no",
        'data_size': len(our_ge_5),
        'our_accuracy': acc_our,
        'cot_accuracy': acc_cot,
        'required_data_size': required_n
    }

    chi2, p, acc_our, acc_cot, required_n = chi2_from_binary(our_all, cot_all)
    results['all_step_sizes'] = {
        'chi2': chi2,
        'p': p,
        'significant': "yes" if p < 0.05 else "no",
        'data_size': len(our_all),
        'our_accuracy': acc_our,
        'cot_accuracy': acc_cot,
        'required_data_size': required_n
    }

    with open(output_result_filepath, 'w') as f:
        json.dump(results, f, indent=2)

    return results



if __name__ == "__main__":
    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3

    #options = ["hard_ambi", "has_ambi", "no_ambi", "only_hard", "var"]
    options = ["only_easy"]
    for option in options:
        our_data_filepath = os.path.expanduser(f"~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_10_visualisation/_7_our_method_method_step_dict_{option}.json")
        cot_data_filepath = os.path.expanduser(f"~/TextToActions/dataset/simulated/_3_simulators/_5_testcases/_10_visualisation/_7_cot_action_method_step_dict_{option}.json")
        output_result_filepath = os.path.expanduser(f"~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/summary/chi2_results_{option}.json")

        run_chi2_analysis(our_data_filepath, cot_data_filepath, output_result_filepath)
    pass 
