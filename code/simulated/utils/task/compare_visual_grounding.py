# input is 

import matplotlib.pyplot as plt
import numpy as np
import json
import os
import numpy as np
from collections import defaultdict
import matplotlib
from matplotlib.lines import Line2D
matplotlib.use('Agg')


def compute_metrics(instances):
    precision = defaultdict(list)
    recall = defaultdict(list)
    f1 = defaultdict(list)
    for inst in instances:
        mt = inst["machine_type"]
        p = inst["precision"]
        r = inst["recall"]
        f1_score = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        precision[mt].append(p)
        recall[mt].append(r)
        f1[mt].append(f1_score)
    return precision, recall, f1

def compute_f1_scores(instance_data):
    f1_by_appliance = defaultdict(list)
    for item in instance_data:
        precision = item["precision"]
        recall = item["recall"]
        if precision + recall > 0:
            f1 = 2 * precision * recall / (precision + recall)
        else:
            f1 = 0.0
        f1_by_appliance[item["machine_type"]].append(f1)
    return f1_by_appliance

def compute_data_sizes(instances):
    data_sizes = defaultdict(int)
    for item in instances:
        data_sizes[item["machine_type"]] += item["total_action"]
    return data_sizes

def scale_bubble_sizes(size_dicts, max_radius=45):
    # Combine all sizes
    all_sizes = list(size_dicts[0].values()) + list(size_dicts[1].values())
    max_size = max(all_sizes)

    def scale_area(s):
        if max_size == 0:
            return 1  # fallback
        scale = s / max_size
        radius = max_radius * np.sqrt(scale)
        return np.pi * radius ** 2  # scatter() expects area in pt²

    return (
        {k: scale_area(v) for k, v in size_dicts[0].items()},
        {k: scale_area(v) for k, v in size_dicts[1].items()},
    )

def instance_level_bubble_chart_all(molmo_result_filepath, gpt_result_filepath, output_prefix):
    with open(molmo_result_filepath, 'r') as f:
        molmo_instances = json.load(f)
    with open(gpt_result_filepath, 'r') as f:
        gpt_instances = json.load(f)

    molmo_precision, molmo_recall, molmo_f1 = compute_metrics(molmo_instances)
    gpt_precision, gpt_recall, gpt_f1 = compute_metrics(gpt_instances)

    molmo_data_sizes = compute_data_sizes(molmo_instances)
    gpt_data_sizes = compute_data_sizes(gpt_instances)

    molmo_scaled, gpt_scaled = scale_bubble_sizes((molmo_data_sizes, gpt_data_sizes))

    appliance_types = sorted(set(molmo_f1.keys()).union(set(gpt_f1.keys())))
    metrics = {
        "Precision": (molmo_precision, gpt_precision),
        "Recall": (molmo_recall, gpt_recall),
        "F1 Score": (molmo_f1, gpt_f1)
    }

    for metric_name, (molmo_metric, gpt_metric) in metrics.items():
        x = np.arange(len(appliance_types) + 1)
        fig, ax = plt.subplots(figsize=(16, 8))

        for i, appliance in enumerate(appliance_types):
            gpt_mean = np.mean(gpt_metric[appliance])
            gpt_std = np.std(gpt_metric[appliance])
            gpt_size = gpt_scaled[appliance]

            molmo_mean = np.mean(molmo_metric[appliance])
            molmo_std = np.std(molmo_metric[appliance])
            molmo_size = molmo_scaled[appliance]

            ax.scatter(i - 0.15, gpt_mean, s=gpt_size, label="Text2Action" if i == 0 else "",
                       alpha=0.6, edgecolors='black', color='green')
            ax.errorbar(i - 0.15, gpt_mean, yerr=gpt_std, fmt='none', ecolor='black', capsize=4)

            ax.scatter(i + 0.15, molmo_mean, s=molmo_size, label="Molmo" if i == 0 else "",
                       alpha=0.6, edgecolors='black', color='pink')
            ax.errorbar(i + 0.15, molmo_mean, yerr=molmo_std, fmt='none', ecolor='black', capsize=4)

        gpt_all = [score for scores in gpt_metric.values() for score in scores]
        molmo_all = [score for scores in molmo_metric.values() for score in scores]
        gpt_avg = np.mean(gpt_all)
        molmo_avg = np.mean(molmo_all)
        gpt_std = np.std(gpt_all)
        molmo_std = np.std(molmo_all)
        gpt_size = np.mean(list(gpt_scaled.values()))
        molmo_size = np.mean(list(molmo_scaled.values()))

        ax.scatter(len(appliance_types) - 0.3, gpt_avg, s=gpt_size, color='green', alpha=0.6,
                   edgecolors='black')
        ax.errorbar(len(appliance_types) - 0.3, gpt_avg, yerr=gpt_std, fmt='none', ecolor='black', capsize=4)

        ax.scatter(len(appliance_types) + 0.3, molmo_avg, s=molmo_size, color='pink', alpha=0.6,
                   edgecolors='black')
        ax.errorbar(len(appliance_types) + 0.3, molmo_avg, yerr=molmo_std, fmt='none', ecolor='black', capsize=4)

        overall_action_size = round(
            (sum(molmo_data_sizes.values()) + sum(gpt_data_sizes.values())) / (2 * 5 * len(appliance_types)), 1
        )

        xtick_labels = [
            f"{' '.join(a.split('_')[2:])}\n(avg action size: {round((molmo_data_sizes[a] + gpt_data_sizes[a]) / 10, 1)})"
            for a in appliance_types
        ] + [f"overall\n(avg action size: {overall_action_size})"]

        ax.set_xticks(x)
        ax.set_xticklabels(xtick_labels)
        ax.set_ylabel(metric_name)
        ax.set_title(f"Action Grounding {metric_name} per Appliance Type")
        ax.set_ylim(0.3, 1.1)
        ax.set_xlim(-0.6, len(appliance_types) +0.6 )

        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Text2Action',
                   markerfacecolor='green', markersize=10, markeredgecolor='black'),
            Line2D([0], [0], marker='o', color='w', label='Molmo',
                   markerfacecolor='pink', markersize=10, markeredgecolor='black')
        ]
        ax.legend(handles=legend_elements, prop={'size': 10}, loc='lower right', framealpha=0.9)

        plt.tight_layout()
        img_filepath = output_prefix.split(".")[0] + f"_{metric_name.lower().replace(' ', '_')}.png"
        plt.savefig(img_filepath)
        plt.close()
    
    # Save stats to JSON
    stats = {}
    for appliance in appliance_types:
        stats[appliance] = {
            "gpt_precision": np.mean(gpt_precision[appliance]),
            "gpt_recall": np.mean(gpt_recall[appliance]),
            "gpt_f1": np.mean(gpt_f1[appliance]),
            "molmo_precision": np.mean(molmo_precision[appliance]),
            "molmo_recall": np.mean(molmo_recall[appliance]),
            "molmo_f1": np.mean(molmo_f1[appliance])
        }

    stats["overall"] = {
        "gpt_precision": np.mean([s for scores in gpt_precision.values() for s in scores]),
        "gpt_recall": np.mean([s for scores in gpt_recall.values() for s in scores]),
        "gpt_f1": np.mean([s for scores in gpt_f1.values() for s in scores]),
        "molmo_precision": np.mean([s for scores in molmo_precision.values() for s in scores]),
        "molmo_recall": np.mean([s for scores in molmo_recall.values() for s in scores]),
        "molmo_f1": np.mean([s for scores in molmo_f1.values() for s in scores])
    }

    stats_path = os.path.join(os.path.dirname(os.path.dirname(gpt_result_filepath)), "stats.json")
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=4)

def instance_level_bubble_chart(molmo_result_filepath, gpt_result_filepath, output_filepath):
    with open(molmo_result_filepath, 'r') as f:
        molmo_instances = json.load(f)
    with open(gpt_result_filepath, 'r') as f:
        gpt_instances = json.load(f)

    molmo_f1 = compute_f1_scores(molmo_instances)
    gpt_f1 = compute_f1_scores(gpt_instances)

    molmo_data_sizes = compute_data_sizes(molmo_instances)
    gpt_data_sizes = compute_data_sizes(gpt_instances)

    molmo_scaled, gpt_scaled = scale_bubble_sizes((molmo_data_sizes, gpt_data_sizes))

    appliance_types = sorted(set(molmo_f1.keys()).union(set(gpt_f1.keys())))
    #x = np.arange(len(appliance_types) + 1)  # +1 for overall average
    x = np.arange(0, (len(appliance_types) + 1) * 2, 2)  # space out the appliance types


    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot per appliance type
    for i, appliance in enumerate(appliance_types):
        gpt_mean = np.mean(gpt_f1[appliance])
        gpt_std = np.std(gpt_f1[appliance])
        gpt_size = gpt_scaled[appliance]

        molmo_mean = np.mean(molmo_f1[appliance])
        molmo_std = np.std(molmo_f1[appliance])
        molmo_size = molmo_scaled[appliance]

        ax.scatter(i - 0.15, gpt_mean, s=gpt_size, label="GPT Prompting" if i == 0 else "",
                   alpha=0.6, edgecolors='black', color='green')
        ax.errorbar(i - 0.15, gpt_mean, yerr=gpt_std, fmt='none', ecolor='black', capsize=4)

        ax.scatter(i + 0.15, molmo_mean, s=molmo_size, label="Molmo" if i == 0 else "",
                   alpha=0.6, edgecolors='black', color='pink')
        ax.errorbar(i + 0.15, molmo_mean, yerr=molmo_std, fmt='none', ecolor='black', capsize=4)

    # Add overall average
    gpt_all = [score for scores in gpt_f1.values() for score in scores]
    molmo_all = [score for scores in molmo_f1.values() for score in scores]
    gpt_avg = np.mean(gpt_all)
    molmo_avg = np.mean(molmo_all)
    gpt_std = np.std(gpt_all)
    molmo_std = np.std(molmo_all)
    gpt_size = np.mean(list(gpt_scaled.values()))
    molmo_size = np.mean(list(molmo_scaled.values()))

    ax.scatter(len(appliance_types) - 0.15, gpt_avg, s=gpt_size, color='green', alpha=0.6,
               edgecolors='black')
    ax.errorbar(len(appliance_types) - 0.15, gpt_avg, yerr=gpt_std, fmt='none', ecolor='black', capsize=4)

    ax.scatter(len(appliance_types) + 0.15, molmo_avg, s=molmo_size, color='pink', alpha=0.6,
               edgecolors='black')
    ax.errorbar(len(appliance_types) + 0.15, molmo_avg, yerr=molmo_std, fmt='none', ecolor='black', capsize=4)

    # Compute overall average action size across all appliances
    overall_action_size = round(
        (sum(molmo_data_sizes.values()) + sum(gpt_data_sizes.values())) / (2 * 5 * len(appliance_types)), 1
    )

    # X-tick labels
    xtick_labels = [
        f"{' '.join(a.split('_')[2:])}\n(avg action size: {round((molmo_data_sizes[a] + gpt_data_sizes[a]) / 10, 1)})"
        for a in appliance_types
    ] + [f"overall\n(avg action size: {overall_action_size})"]

    ax.set_xticks(x)
    ax.set_xticklabels(xtick_labels)
    ax.set_ylabel("F1 Score")
    ax.set_title("Action Grounding F1 Score per Appliance Type")
    ax.set_ylim(0.4, 1.1)
    ax.set_xlim(-0.6, len(appliance_types) + 0.6)

    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='GPT Prompting',
               markerfacecolor='green', markersize=10, markeredgecolor='black'),
        Line2D([0], [0], marker='o', color='w', label='Molmo',
               markerfacecolor='pink', markersize=10, markeredgecolor='black')
    ]
    ax.legend(handles=legend_elements, prop={'size': 10}, loc='lower right', framealpha=0.9)

    plt.tight_layout()
    plt.savefig(output_filepath)
    plt.close()

def instance_level_graph(molmo_result_filepath, gpt_result_filepath, output_filepath):
    with open(molmo_result_filepath, 'r') as f:
        molmo_instances = json.load(f)
    with open(gpt_result_filepath, 'r') as f:
        gpt_instances = json.load(f)

    molmo_f1 = compute_f1_scores(molmo_instances)
    gpt_f1 = compute_f1_scores(gpt_instances)

    appliance_types = sorted(molmo_f1.keys())

    molmo_means = [np.mean(molmo_f1[appliance]) for appliance in appliance_types]
    molmo_stds = [np.std(molmo_f1[appliance]) for appliance in appliance_types]

    gpt_means = [np.mean(gpt_f1[appliance]) for appliance in appliance_types]
    gpt_stds = [np.std(gpt_f1[appliance]) for appliance in appliance_types]

    x = np.arange(len(appliance_types))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, molmo_means, width, yerr=molmo_stds, capsize=5, label='Molmo')
    ax.bar(x + width/2, gpt_means, width, yerr=gpt_stds, capsize=5, label='GPT Prompting')

    ax.set_ylabel("F1 Score")
    ax.set_title("Action Grounding F1 Score per Appliance Type")
    ax.set_xticks(x)
    ax.set_xticklabels([' '.join(a.split('_')[2:]) for a in appliance_types])

    ax.set_ylim(0, 1.1)
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_filepath)
    plt.close()

def machine_type_level_graph(molmo_result_filepath, gpt_result_filepath, output_filepath):
    with open(molmo_result_filepath, 'r') as f:
        molmo_data = json.load(f)
    with open(gpt_result_filepath, 'r') as f:
        gpt_data = json.load(f)
    
    appliance_types = [entry["machine_type"] for entry in molmo_data]
    metrics = ["machine_level_precision", "machine_level_recall"]

    molmo_precision = [entry["machine_level_precision"] for entry in molmo_data]
    molmo_recall = [entry["machine_level_recall"] for entry in molmo_data]

    gpt_precision = [entry["machine_level_precision"] for entry in gpt_data]
    gpt_recall = [entry["machine_level_recall"] for entry in gpt_data]

    x = np.arange(len(appliance_types))  # appliance indices
    width = 0.35  # bar width

    fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Precision plot
    ax[0].bar(x - width/2, molmo_precision, width, label='Molmo')
    ax[0].bar(x + width/2, gpt_precision, width, label='GPT Prompting')
    ax[0].set_ylabel('Precision')
    ax[0].set_title('Action Grounding Precision per Appliance Type')
    ax[0].legend()
    ax[0].set_ylim(0, 1.1)

    # Recall plot
    ax[1].bar(x - width/2, molmo_recall, width, label='Molmo')
    ax[1].bar(x + width/2, gpt_recall, width, label='GPT Prompting')
    ax[1].set_ylabel('Recall')
    ax[1].set_title('Action Grounding Recall per Appliance Type')
    ax[1].legend()
    ax[1].set_ylim(0, 1.1)

    # Common x-axis labels
    ax[1].set_xticks(x)
    ax.set_xticklabels([' '.join(a.split('_')[2:]) for a in appliance_types])

    plt.tight_layout()
    plt.savefig(output_filepath)
    plt.close()
    #plt.show()

if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    molmo_type_result_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_1_visual_grounding_action_results/molmo/_2_machine_type_level.json")
    gpt_type_result_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_1_visual_grounding_action_results/ours/_2_machine_type_level.json")
    output_type_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_1_visual_grounding_action_results/_0_machine_type_level_graph.png")
    
    #machine_type_level_graph(molmo_type_result_filepath, gpt_type_result_filepath, output_type_filepath)
    
    molmo_instance_result_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_1_visual_grounding_action_results/molmo/_1_instance_level.json")
    gpt_instance_result_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_1_visual_grounding_action_results/ours/_1_instance_level.json")
    output_instance_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_1_visual_grounding_action_results/_1_instance_level_graph.png")
    #instance_level_graph(molmo_instance_result_filepath, gpt_instance_result_filepath, output_instance_filepath)
    output_bubble_filepath = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_1_visual_grounding_action_results/_2_bubble_chart.png")
    #instance_level_bubble_chart(molmo_instance_result_filepath, gpt_instance_result_filepath, output_bubble_filepath)
    instance_level_bubble_chart_all(molmo_instance_result_filepath, gpt_instance_result_filepath, output_bubble_filepath)
