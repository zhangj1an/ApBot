# this one, firstly test the number of steps needed to achieve the task. 
# then draw two graphs: number of steps taken, and accuracy 

# firstly, generate number v.s. number of adjusting var 
# then generate number v.s. the total number of steps needed 

# for both method, generate success rate v.s. number of adjusting var 
# for both method, generate success rate v.s. the total number of steps needed 
import os 
import json
import ast
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import sys
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.create_or_replace_path import create_or_replace_path

def tally_dataset(dataset_dir="", output_dir="", setting = "all"): # all or specific or var
    easy_dataset_dir = os.path.join(dataset_dir, "_6_testcases_specific_formatted")
    hard_dataset_dir = os.path.join(dataset_dir, "_9_testcases_compound_formatted")
    ambi_dataset_dir = os.path.join(dataset_dir, "_8_testcases_unified_formatted")
    var_dataset_dir = os.path.join(dataset_dir, "_4_testcases_var_formatted")

    if setting == "specific":
        dataset_dirs = [(easy_dataset_dir, "easy"), (hard_dataset_dir, "hard")]
    elif setting == "all":
        #dataset_dirs = [(easy_dataset_dir, "easy"), (hard_dataset_dir, "hard"), (ambi_dataset_dir, "ambi")]
        dataset_dirs = [(easy_dataset_dir, "easy"), (hard_dataset_dir, "hard"), (ambi_dataset_dir, "ambi")]
    elif setting == "var":
        dataset_dirs = [(var_dataset_dir, "var")]
    data_dict = {}

    for dataset_dir, label in dataset_dirs:
        data_dict[label] = {}
        #print(f"processing dataset_type: {label}")
        machine_type = [machine_type for machine_type in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, machine_type))] 
        for machine_type in machine_type:
            data_dict[label][machine_type] = {}
            machine_type_dir = os.path.join(dataset_dir, machine_type)
            testcase_ids = [testcase_id for testcase_id in os.listdir(machine_type_dir) if testcase_id.endswith(".py")]
            for testcase_id in testcase_ids: 
                testcase_id_digit = testcase_id.split(".")[0].split("_")[1]
                data_dict[label][machine_type][testcase_id_digit] = {}
                testcase_id_filepath = os.path.join(machine_type_dir, testcase_id) 
                loaded_data = []
                #print(f"loading {testcase_id_filepath}")
                with open(testcase_id_filepath, "r") as f:
                    content = f.read()
                    loaded_data = ast.literal_eval(content)
                
                if setting in ["specific" , "all"]:
                    for command_data in loaded_data:
                        command_id = command_data["id"]
                        command_number_of_steps = command_data["number_of_steps"]
                        command_number_of_variables = command_data["number_of_variables"]
                        data_dict[label][machine_type][testcase_id_digit][command_id] = {
                            "number_of_steps": command_number_of_steps,
                            "number_of_variables": command_number_of_variables
                        }
                elif setting == "var":
                    for command_data in loaded_data:
                        command_id = command_data["id"]
                        command_number_of_variables = machine_type.split("_")[1]
                        data_dict[label][machine_type][testcase_id_digit][command_id] = {
                            "number_of_variables": command_number_of_variables
                        } 
                
    # save data_dict to json file 
    # output_filepath = os.path.join(output_dir, "_0_data_dict.json")
    create_or_replace_path(output_dir)
    output_filepath = os.path.join(output_dir, "_0_data_dict_var.json")
    with open(output_filepath, "w") as f:
        json.dump(data_dict, f, indent=4)
    print(f"data_dict saved to {output_filepath}")
   
def summarise_dataset_by_var_size(input_filepath, output_dir):
    with open(input_filepath, "r") as f:
        data_dict = json.load(f) 
    number_of_variables_dict = {}
    for label in data_dict:
        for machine_type in data_dict[label]:
            for testcase_id in data_dict[label][machine_type]:
                for command_id in data_dict[label][machine_type][testcase_id]:
                    command_data = data_dict[label][machine_type][testcase_id][command_id]
                    number_of_variables = command_data["number_of_variables"]


                    

                    if str(number_of_variables) not in number_of_variables_dict:
                        number_of_variables_dict[str(number_of_variables)] = 1
                    else:
                        number_of_variables_dict[str(number_of_variables)] += 1

    # save number_of_variables_dict to json file
    output_filepath = os.path.join(output_dir, "_1_data_dict_number_of_variables.json")
    with open(output_filepath, "w") as f:
        json.dump(number_of_variables_dict, f, indent=4)
    pass 


def summarise_dataset(input_filepath, output_dir):
    with open(input_filepath, "r") as f:
        data_dict = json.load(f) 
    number_of_steps_dict = {}
    number_of_variables_dict = {}
    number_of_avg_steps_dict = {}
    number_of_steps_dict_by_type = {}
    number_of_variables_dict_by_type = {}
    number_of_avg_steps_dict_by_type = {}
    for label in data_dict:
        for machine_type in data_dict[label]:
            for testcase_id in data_dict[label][machine_type]:
                for command_id in data_dict[label][machine_type][testcase_id]:
                    command_data = data_dict[label][machine_type][testcase_id][command_id]
                    number_of_steps = command_data["number_of_steps"]
                    number_of_variables = command_data["number_of_variables"]


                    if str(number_of_steps) not in number_of_steps_dict:
                        number_of_steps_dict[str(number_of_steps)] = 1
                    else:
                        number_of_steps_dict[str(number_of_steps)] += 1
                    if str(number_of_steps) not in number_of_steps_dict_by_type:
                        number_of_steps_dict_by_type[str(number_of_steps)] = {}
                    if machine_type not in number_of_steps_dict_by_type[str(number_of_steps)]:
                        number_of_steps_dict_by_type[str(number_of_steps)][machine_type] = 1
                    else:
                        number_of_steps_dict_by_type[str(number_of_steps)][machine_type] += 1


                    if str(number_of_variables) not in number_of_variables_dict:
                        number_of_variables_dict[str(number_of_variables)] = 1
                    else:
                        number_of_variables_dict[str(number_of_variables)] += 1
                    if str(number_of_variables) not in number_of_variables_dict_by_type:
                        number_of_variables_dict_by_type[str(number_of_variables)] = {}
                    if machine_type not in number_of_variables_dict_by_type[str(number_of_variables)]:
                        number_of_variables_dict_by_type[str(number_of_variables)][machine_type] = 1
                    else:
                        number_of_variables_dict_by_type[str(number_of_variables)][machine_type] += 1

                    avg_step = round(number_of_steps/number_of_variables * 2) / 2
                    if str(avg_step) not in number_of_avg_steps_dict:
                        number_of_avg_steps_dict[str(avg_step)] = 1
                    else:
                        number_of_avg_steps_dict[str(avg_step)] += 1
                    if str(avg_step) not in number_of_avg_steps_dict_by_type:
                        number_of_avg_steps_dict_by_type[str(avg_step)] = {}
                    if machine_type not in number_of_avg_steps_dict_by_type[str(avg_step)]:
                        number_of_avg_steps_dict_by_type[str(avg_step)][machine_type] = 1
                    else:
                        number_of_avg_steps_dict_by_type[str(avg_step)][machine_type] += 1
    output_filepath = os.path.join(output_dir, "_1_data_dict_number_of_steps_by_type_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(number_of_steps_dict_by_type, f, indent=4)
    
    # save number_of_avg_steps_dict to json file
    output_filepath = os.path.join(output_dir, "_3_data_dict_number_of_avg_steps_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(number_of_avg_steps_dict, f, indent=4)
    output_filepath = os.path.join(output_dir, "_3_data_dict_number_of_avg_steps_by_type_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(number_of_avg_steps_dict_by_type, f, indent=4)

    # save number_of_steps_dict to json file
    output_filepath = os.path.join(output_dir, "_1_data_dict_number_of_steps_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(number_of_steps_dict, f, indent=4)
    

    # save number_of_variables_dict to json file
    output_filepath = os.path.join(output_dir, "_2_data_dict_number_of_variables_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(number_of_variables_dict, f, indent=4)
    output_filepath = os.path.join(output_dir, "_2_data_dict_number_of_variables_by_type_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(number_of_variables_dict_by_type, f, indent=4)
    pass 

def draw_dataset_var_graph(input_json_filepath, output_dir):
    
    var_count_dict = {}
    with open(input_json_filepath, "r") as f:
        var_count_dict = json.load(f)
    output_filepath = os.path.join(output_dir, "_6_data_dict_number_of_variables_binned.png")
    # sort the dictionary by key
    sorted_items = sorted(var_count_dict.items(), key=lambda x: int(x[0]))
    labels = [k for k, v in sorted_items]
    values = [v for k, v in sorted_items]
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color='lightgray', edgecolor='black')
    plt.xlabel('Number of Variables')
    plt.ylabel('Data Size')
    plt.title('Data Size by Number of Adjusting Variables Required to Achieve a Command')
    plt.tight_layout()
    plt.savefig(output_filepath)
    print("done")

    pass 
def draw_dataset_var_graph_detail(input_json_filepath, output_dir):
    with open(input_json_filepath, "r") as f:
        raw_data = json.load(f)

    # Normalize appliance names and define colors
    appliance_name_map = {
        "_1_microwave": "microwave",
        "_2_washing_machine": "washing machine",
        "_3_rice_cooker": "rice cooker",
        "_4_air_purifier": "air purifier"
    }
    appliance_colors = {
        "microwave": "lightpink",
        "rice cooker": "lightyellow",
        "washing machine": "lightblue",
        "air purifier": "lightgreen"
    }

    # Extract all unique appliance types and normalize names
    appliance_types = set()
    binned_appliance_counts = {}
    for var_count, appliance_dict in raw_data.items():
        binned_appliance_counts[var_count] = defaultdict(int)
        for raw_appliance, count in appliance_dict.items():
            appliance = appliance_name_map.get(raw_appliance, raw_appliance)
            binned_appliance_counts[var_count][appliance] += count
            appliance_types.add(appliance)

    appliance_types = sorted(appliance_types)

    # Sort the variable bins
    sorted_items = sorted(binned_appliance_counts.items(), key=lambda x: int(x[0]))
    labels = [k for k, _ in sorted_items]

    # Prepare data for each appliance
    bar_data = {appliance: [] for appliance in appliance_types}
    for _, counts in sorted_items:
        for appliance in appliance_types:
            bar_data[appliance].append(counts.get(appliance, 0))

    # Stack the bars
    plt.figure(figsize=(8, 6))
    bottom = [0] * len(labels)
    for appliance in appliance_types:
        plt.bar(
            labels,
            bar_data[appliance],
            bottom=bottom,
            label=appliance,
            color=appliance_colors.get(appliance, "gray"),
            edgecolor="black"
        )
        bottom = [b + v for b, v in zip(bottom, bar_data[appliance])]

    plt.xlabel('Number of Variables')
    plt.ylabel('Data Size')
    plt.title('Data Size by No. of Variables Adjusted to Achieve a Command')
    plt.legend(title='Appliance Type', loc='upper right')
    plt.ylim(0, 50)
    plt.yticks(range(0, 50, 10))
    plt.tight_layout()

    output_filepath = os.path.join(output_dir, "_6_data_dict_number_of_variables_binned_stacked.png")
    plt.savefig(output_filepath)
    print("done")
    plt.close()

    pass 
def draw_dataset_step_graph_detail(input_json_filepath, output_dir):
    bin_labels = [str(i) for i in range(1, 26)]

    # Load the nested step data with appliance type breakdown
    with open(input_json_filepath, "r") as f:
        raw_data = json.load(f)

    # Normalize appliance names and prepare color mapping
    appliance_name_map = {
        "_1_microwave": "microwave",
        "_2_washing_machine": "washing machine",
        "_3_rice_cooker": "rice cooker",
        "_4_air_purifier": "air purifier"
    }
    appliance_colors = {
        "microwave": "lightpink",
        "rice cooker": "lightyellow",
        "washing machine": "lightblue",
        "air purifier": "lightgreen"
    }

    # Create a nested dict: step → appliance → count
    appliance_types = set()
    binned_appliance_counts = {label: defaultdict(int) for label in bin_labels}
    
    for step, appliance_dict in raw_data.items():
        if step not in bin_labels:
            continue
        for raw_appliance, count in appliance_dict.items():
            appliance = appliance_name_map.get(raw_appliance, raw_appliance)
            appliance_types.add(appliance)
            binned_appliance_counts[step][appliance] += count

    # Sort appliance types for consistent coloring
    appliance_types = sorted(appliance_types)

    # Prepare data for stacked bar plot
    labels = [label for label in bin_labels if sum(binned_appliance_counts[label].values()) > 0]

    bottom = [0] * len(labels)
    bar_data = {appliance: [] for appliance in appliance_types}

    for label in labels:
        for appliance in appliance_types:
            count = binned_appliance_counts[label][appliance]
            bar_data[appliance].append(count)

    # Plotting
    plt.figure(figsize=(10, 6))
    for appliance in appliance_types:
        plt.bar(
            labels,
            bar_data[appliance],
            bottom=bottom,
            label=appliance,
            color=appliance_colors.get(appliance, 'gray'),
            edgecolor='black'
        )
        bottom = [b + v for b, v in zip(bottom, bar_data[appliance])]

    plt.xlabel('Number of Steps')
    plt.ylabel('Data Size')
    plt.title('Data Size by Required Step Count to Achieve a Command')
    plt.ylim(0, 70)
    plt.yticks(range(0, 70, 10))
    plt.legend(title='Appliance Type', loc='upper right')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save output
    output_filepath = os.path.join(output_dir, "_4_data_dict_number_of_steps_binned_detail_stacked.png")
    plt.savefig(output_filepath)
    print("done")
    plt.close()

    pass 
def draw_dataset_step_graph(input_json_filepath, output_dir):

    bin_ranges_2 = { f"{i}": range(i, i+1) for i in range(1, 26) }
    step_count_dict = {}
    with open(input_json_filepath, "r") as f:
        step_count_dict = json.load(f)
    
    output_filepath_2 = os.path.join(output_dir, "_4_data_dict_number_of_steps_binned_detail.png")

    binned_counts_detail = defaultdict(int)
    for step, count in step_count_dict.items():
        for label, r in bin_ranges_2.items():
            if int(step) in r:
                binned_counts_detail[label] += count
                break

    # Prepare plot
    sorted_items_detail = sorted(binned_counts_detail.items(), key=lambda x: int(x[0]))
    labels_detail = [k for k, v in sorted_items_detail]
    values_detail = [v for k, v in sorted_items_detail]

    def rough_sort_key(label):
        if '+' in label:
            return float(label.replace('+', '')) + 0.5  # e.g., '8+' → 8.5
        else:
            return float(label.split('–')[0])  # e.g., '4–5' → 4.0

    plt.figure(figsize=(8, 6))
    plt.bar(labels_detail, values_detail, color='lightgray', edgecolor='black')
    plt.xlabel('Number of Steps (Binned)')
    plt.ylabel('Data Size')
    plt.title('Data Size by Number of Steps Required to Achieve a Command')
    plt.tight_layout()
    plt.savefig(output_filepath_2)
    print("done")
    plt.close()
    pass 

def draw_dataset_avg_step_graph_detail(input_json_filepath, output_dir):
    with open(input_json_filepath, "r") as f:
        raw_data = json.load(f)

    # Normalize appliance names and define colors
    appliance_name_map = {
        "_1_microwave": "microwave",
        "_2_washing_machine": "washing machine",
        "_3_rice_cooker": "rice cooker",
        "_4_air_purifier": "air purifier"
    }
    appliance_colors = {
        "microwave": "lightpink",
        "rice cooker": "lightyellow",
        "washing machine": "lightblue",
        "air purifier": "lightgreen"
    }

    # Build nested structure: bin → appliance → count
    appliance_types = set()
    binned_appliance_counts = {}
    for step_bin, appliance_dict in raw_data.items():
        binned_appliance_counts[step_bin] = defaultdict(int)
        for raw_appliance, count in appliance_dict.items():
            appliance = appliance_name_map.get(raw_appliance, raw_appliance)
            binned_appliance_counts[step_bin][appliance] += count
            appliance_types.add(appliance)

    appliance_types = sorted(appliance_types)

    # Sort bins by float
    sorted_items = sorted(binned_appliance_counts.items(), key=lambda x: float(x[0]))
    labels = [str(float(k)) for k, _ in sorted_items]

    # Prepare data for each appliance
    bar_data = {appliance: [] for appliance in appliance_types}
    for _, counts in sorted_items:
        for appliance in appliance_types:
            bar_data[appliance].append(counts.get(appliance, 0))

    # Stack the bars
    plt.figure(figsize=(10, 6))
    bottom = [0] * len(labels)
    for appliance in appliance_types:
        plt.bar(
            labels,
            bar_data[appliance],
            bottom=bottom,
            label=appliance,
            color=appliance_colors.get(appliance, "gray"),
            edgecolor="black"
        )
        bottom = [b + v for b, v in zip(bottom, bar_data[appliance])]

    plt.xlabel('Data Size by Required Step Count per Variable to Achieve a Command')
    plt.ylabel('Data Size')
    plt.title('Data Size by Step Count per Variable')
    plt.legend(title='Appliance Type', loc='upper right')
    plt.ylim(0, 50)
    plt.yticks(range(0, 50, 10))
    plt.tight_layout()

    output_filepath = os.path.join(output_dir, "_5_data_dict_step_count_per_var_binned_stacked.png")
    plt.savefig(output_filepath)
    print("done")
    plt.close()

def draw_dataset_avg_step_graph(input_json_filepath, output_dir):
    # Load the data
    with open(input_json_filepath, "r") as f:
        var_count_dict = json.load(f)

    # Sort the dictionary by float key
    sorted_items = sorted(var_count_dict.items(), key=lambda x: float(x[0]))

    # Extract sorted labels and values
    labels = [str(float(k)) for k, v in sorted_items]  # Ensure consistent float-style labels
    values = [v for k, v in sorted_items]

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color='lightgray', edgecolor='black')
    plt.xlabel('Number of Variables')
    plt.ylabel('Data Size')
    plt.title('Data Size by Step Count per Variable')
    plt.tight_layout()

    # Save figure
    output_filepath = os.path.join(output_dir, "_5_data_dict_step_count_per_var_binned.png")
    plt.savefig(output_filepath)
    print("done")
def draw_method_success_rate_graph(method_step_filepath, method_label, dataset_step_filepath, output_dir):
    method_step_dict = {}
    method_var_dict = {}
    method_avg_step_dict = {}
    with open(method_step_filepath, "r") as f:
        method_result_dict = json.load(f)
    with open(dataset_step_filepath, "r") as f:
        dataset_dict = json.load(f) 
    for machine_type in method_result_dict["results_details"]:
        for machine_id in method_result_dict["results_details"][machine_type]:
            for testcase_difficulty in method_result_dict["results_details"][machine_type][machine_id]:
                if testcase_difficulty == "avg":
                    continue
                #print(f"processing machine_type: {machine_type}, machine_id: {machine_id}, testcase_difficulty: {testcase_difficulty}")
                for command_id in method_result_dict["results_details"][machine_type][machine_id][testcase_difficulty]:
                    score = method_result_dict["results_details"][machine_type][machine_id][testcase_difficulty][command_id]
                
                    for label in dataset_dict:
                        if label in testcase_difficulty:
                            for machine_type_2 in dataset_dict[label]:
                                if machine_type in machine_type_2:
                                    
                                    number_of_steps = dataset_dict[label][machine_type_2][machine_id][command_id]["number_of_steps"]
                                    number_of_variables = dataset_dict[label][machine_type_2][machine_id][command_id]["number_of_variables"]
                                    avg_steps = round(number_of_steps/number_of_variables * 2) / 2
                                    if str(avg_steps) not in method_avg_step_dict:
                                        # add the score 
                                        method_avg_step_dict[str(avg_steps)] = {"success": 0, "total": 0}
                                    if score == 1:
                                        method_avg_step_dict[str(avg_steps)]["success"] += 1
                                    method_avg_step_dict[str(avg_steps)]["total"] += 1
                                    if str(number_of_steps) not in method_step_dict:
                                        # add the score 
                                        method_step_dict[str(number_of_steps)] = {"success": 0, "total": 0}
                                    if score == 1:
                                        method_step_dict[str(number_of_steps)]["success"] += 1
                                    
                                    method_step_dict[str(number_of_steps)]["total"] += 1
                                    if str(number_of_variables) not in method_var_dict:
                                        # add the score 
                                        method_var_dict[str(number_of_variables)] = {"success": 0, "total": 0}
                                    if score == 1:
                                        method_var_dict[str(number_of_variables)]["success"] += 1
                                    method_var_dict[str(number_of_variables)]["total"] += 1
    # save method_step_dict to json file
    output_filepath = os.path.join(output_dir, f"_7_{method_label}_method_step_dict_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(method_step_dict, f, indent=4)
    # draw the graph
    output_filepath = os.path.join(output_dir, f"_7_{method_label}_method_step_dict_has_ambi.png")
    plt.figure(figsize=(8, 6))
    # sort the dictionary by key
    sorted_items = sorted(method_step_dict.items(), key=lambda x: int(x[0]))
    labels = [k for k, v in sorted_items]
    values = [v for k, v in sorted_items]
    success_rate = [v["success"] / v["total"] for v in values] 
    plt.bar(labels, success_rate, color='lightgray', edgecolor='black')
    plt.xlabel('Number of Steps')
    plt.ylabel('Success Rate')
    plt.title('Success Rate by Oracle Number of Steps Required to Achieve a Command')
    plt.tight_layout()
    plt.savefig(output_filepath)
    # save method_var_dict to json file

     
    output_filepath = os.path.join(output_dir, f"_8_{method_label}_method_var_dict_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(method_var_dict, f, indent=4)
    # draw the graph
    output_filepath = os.path.join(output_dir, f"_8_{method_label}_method_var_dict_has_ambi.png")
    plt.figure(figsize=(8, 6))
    # sort the dictionary by key
    sorted_items = sorted(method_var_dict.items(), key=lambda x: int(x[0]))
    labels = [k for k, v in sorted_items]
    values = [v for k, v in sorted_items]
    success_rate = [v["success"] / v["total"] for v in values]
    plt.bar(labels, success_rate, color='lightgray', edgecolor='black')
    plt.xlabel('Number of Variables')
    plt.ylabel('Success Rate')
    plt.title('Success Rate by Oracle Number of Adjusting Variables Required to Achieve a Command')
    plt.tight_layout()
    plt.savefig(output_filepath)
    
    # save method_avg_step_dict to json file
    output_filepath = os.path.join(output_dir, f"_9_{method_label}_method_avg_step_dict_has_ambi.json")
    with open(output_filepath, "w") as f:
        json.dump(method_avg_step_dict, f, indent=4)
    # draw the graph
    output_filepath = os.path.join(output_dir, f"_9_{method_label}_method_avg_step_dict_has_ambi.png")
    plt.figure(figsize=(8, 6))
    # sort the dictionary by key
    sorted_items = sorted(method_avg_step_dict.items(), key=lambda x: float(x[0]))
    labels = [k for k, v in sorted_items]
    values = [v for k, v in sorted_items]
    success_rate = [v["success"] / v["total"] for v in values]
    plt.bar(labels, success_rate, color='lightgray', edgecolor='black')
    plt.xlabel('Number of Steps per Variable')
    plt.ylabel('Success Rate')
    plt.title('Success Rate by Oracle Step Count per Variable Required to Achieve a Command')
    plt.tight_layout()
    plt.savefig(output_filepath)
    
    
    pass 


def draw_combined_success_rate_graph(data_info_filepath, cot_image_filepath, cot_action_filepath, ours_filepath, output_filepath, setting = "step"): # step or var or avg_step
    with open(data_info_filepath, "r") as f:
        data_info_dict = json.load(f)
    with open(cot_image_filepath, "r") as f:
        cot_image_dict = json.load(f)
    with open(cot_action_filepath, "r") as f:
        cot_action_dict = json.load(f)
    with open(ours_filepath, "r") as f:
        ours_dict = json.load(f)

    # Define x-axis bins
    if setting == "step":
        bins = list(range(1, 9))  # 1 to 8
        bin_labels = [str(i) for i in bins] + ["9-25"]
    elif setting == "var":
        bins = list(range(1, 8)) 
        bin_labels = [str(i) for i in bins]
    elif setting == "avg_step":
        bins = [round(i, 1) for i in [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.5]]  # 1 to 4.5 in units of 0.5
        bin_labels = [str(i) for i in bins] + ["5-13"]

    # Initialize bar plot bins
    binned_counts = defaultdict(int)
    for key, count in data_info_dict.items():
        if setting == "step" or setting == "var":
            k = int(key)
        elif setting == "avg_step":
            k = round(float(key), 1)
        if setting == "step":
            label = str(k) if k in bins else "9-25"
        elif setting == "avg_step":
            label = f"{k:.1f}" if k in bins else "5-13"
        elif setting == "var":
            label = str(k) 
        binned_counts[label] += count

    

    # Bar values
    x_labels = bin_labels
    y_data_size = [binned_counts[label] for label in x_labels]

    def compute_success_rates(data_dict, setting = "step"):
        bin_total = defaultdict(int)
        bin_success = defaultdict(int)
        for key, entry in data_dict.items():
            if setting == "step" or setting == "var":
                k = int(key)
            elif setting == "avg_step":
                k = round(float(key), 1)
            print("key:", k  )
            print("bins:", bins)
            if setting == "step":
                label = str(k) if k in bins else "9-25"
            elif setting == "var":
                label = str(k)
            elif setting == "avg_step":
                label = f"{k:.1f}" if k in bins else "5-13"
            print("label:", label)
            bin_total[label] += entry["total"]
            bin_success[label] += entry["success"]
        return [
            bin_success[label] / bin_total[label]
            if bin_total[label] > 0 else 0
            for label in x_labels
        ]
    
    # Compute success rates
    y_cot_image = compute_success_rates(cot_image_dict, setting=setting)
    y_cot_action = compute_success_rates(cot_action_dict, setting=setting)
    y_ours = compute_success_rates(ours_dict, setting=setting)

    # Start plotting
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar chart
    bar_plot = ax1.bar(x_labels, y_data_size, color='lightgray', edgecolor='black', width=0.6, label='Data size')
    ax1.set_ylabel("Data size", fontsize=12)
    if setting == "step":
        ax1.set_ylim(0, 70)
        ax1.set_yticks(range(0, 70, 10))
    elif setting == "var":
        ax1.set_ylim(0, 50)
        ax1.set_yticks(range(0, 180, 10))
    elif setting == "avg_step":
        ax1.set_ylim(0, 50)
        ax1.set_yticks(range(0, 51, 10))

    for x, y in zip(x_labels, y_data_size):
        ax1.text(x, y + 0.2, str(y), ha='center', va='bottom', fontsize=9)

    # Line plot (success rate)
    ax2 = ax1.twinx()
    line_cot_image, = ax2.plot(x_labels, y_cot_image, marker='o', color='blue', linewidth=2, label='cot-image')
    line_cot_action, = ax2.plot(x_labels, y_cot_action, marker='s', color='green', linewidth=2, label='cot-action')
    line_ours, = ax2.plot(x_labels, y_ours, marker='^', color='red', linewidth=2, label='ours')

    ax2.set_ylabel("Success rate", fontsize=12)
    ax2.set_ylim(-0.05, 1.05)
    ax2.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

    # Add legend
    ax2.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))

    # X-axis
    if setting == "step":
        ax1.set_xlabel("Number of Steps")
        ax1.set_title("Success Rate (Lines) and Data Size (Bars)\nby Oracle Step Count", fontsize=14)
    elif setting == "var":
        ax1.set_xlabel("Number of Variables")
        ax1.set_title("Success Rate (Lines) and Data Size (Bars)\nby Number of Adjusted Variables", fontsize=14)
    elif setting == "avg_step":
        ax1.set_xlabel("Average Step Count per Variable")
        ax1.set_title("Success Rate (Lines) and Data Size (Bars)\nby Oracle Step Count per Variable", fontsize=14)

    plt.tight_layout()

    if output_filepath:
        plt.savefig(output_filepath)
    plt.close()

    pass 




if __name__ == "__main__":
    #srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 

    output_dir_data_graph = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_10_visualisation/")
    dataset_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_3_simulators/_5_testcases")
    data_info_filepath = os.path.join(output_dir_data_graph, "_0_data_dict_var.json")
    #tally_dataset(dataset_dir=dataset_dir, output_dir=output_dir_data_graph, setting = "var")
    summarise_dataset_by_var_size(input_filepath=data_info_filepath, output_dir=output_dir_data_graph)
    
    # for easy, hard, ambi
    #summarise_dataset(input_filepath=data_info_filepath, output_dir=output_dir_data_graph)

    #draw_dataset_step_graph_detail(input_json_filepath=os.path.join(output_dir_data_graph, "_1_data_dict_number_of_vars_by_type.json"), output_dir=output_dir_data_graph)

    ############
    # not impt 
    ############
    #draw_dataset_step_graph(input_json_filepath=os.path.join(output_dir_data_graph, "_1_data_dict_number_of_steps.json"), output_dir=output_dir_data_graph)
    #draw_dataset_var_graph(input_json_filepath=os.path.join(output_dir_data_graph, "_2_data_dict_number_of_variables.json"), output_dir=output_dir_data_graph)
    #draw_dataset_var_graph_detail(input_json_filepath=os.path.join(output_dir_data_graph, "_2_data_dict_number_of_variables_by_type.json"), output_dir=output_dir_data_graph)
    #draw_dataset_avg_step_graph(input_json_filepath=os.path.join(output_dir_data_graph, "_3_data_dict_number_of_avg_steps.json"), output_dir=output_dir_data_graph)
    #draw_dataset_avg_step_graph_detail(input_json_filepath=os.path.join(output_dir_data_graph, "_3_data_dict_number_of_avg_steps_by_type.json"), output_dir=output_dir_data_graph)
    
    cot_image_method_step_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselinesv1/_1_NV_M_UR_LP/gpt-4o-2024-11-20_report.json")
    cot_action_method_step_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselines/_1_M_UR_LP/gpt-4o-2024-11-20_report.json")
    our_method_agnostic_method_step_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_6_results/_6_paper_exp/baselines/_4_M_SR_MA/gpt-4o-2024-11-20_report.json")
    #draw_method_success_rate_graph(cot_image_method_step_filepath, "cot_image", data_info_filepath, output_dir_data_graph)
    #draw_method_success_rate_graph(cot_action_method_step_filepath, "cot_action",data_info_filepath, output_dir_data_graph)
    #draw_method_success_rate_graph(our_method_agnostic_method_step_filepath, "our_method", data_info_filepath, output_dir_data_graph)



    dataset_step_filepath = os.path.join(output_dir_data_graph, "_1_data_dict_number_of_steps.json")
    cot_image_step_filepath = os.path.join(output_dir_data_graph, "_7_cot_image_method_step_dict.json")
    cot_action_step_filepath = os.path.join(output_dir_data_graph, "_7_cot_action_method_step_dict.json")
    ours_step_filepath = os.path.join(output_dir_data_graph, "_7_our_method_method_step_dict.json")
    output_step_filepath = os.path.join(output_dir_data_graph, "_10_combined_step_success_rate.png")
    #draw_combined_success_rate_graph(dataset_step_filepath , cot_image_step_filepath, cot_action_step_filepath, ours_step_filepath, output_step_filepath, setting="step")

    dataset_var_filepath = os.path.join(output_dir_data_graph, "_2_data_dict_number_of_variables_has_ambi.json")
    cot_image_var_filepath = os.path.join(output_dir_data_graph, "_8_cot_image_method_var_dict_has_ambi.json")
    cot_action_var_filepath = os.path.join(output_dir_data_graph, "_8_cot_action_method_var_dict_has_ambi.json")
    ours_var_filepath = os.path.join(output_dir_data_graph, "_8_our_method_method_var_dict_has_ambi.json")
    output_var_filepath = os.path.join(output_dir_data_graph, "_10_combined_var_success_rate_has_ambi.png")
    #draw_combined_success_rate_graph(dataset_var_filepath , cot_image_var_filepath, cot_action_var_filepath, ours_var_filepath, output_var_filepath, setting="var")

    dataset_avg_step_filepath = os.path.join(output_dir_data_graph, "_3_data_dict_number_of_avg_steps_has_ambi.json")
    cot_image_avg_step_filepath = os.path.join(output_dir_data_graph, "_9_cot_image_method_avg_step_dict_has_ambi.json")
    cot_action_avg_step_filepath = os.path.join(output_dir_data_graph, "_9_cot_action_method_avg_step_dict_has_ambi.json")
    ours_avg_step_filepath = os.path.join(output_dir_data_graph, "_9_our_method_method_avg_step_dict_has_ambi.json")
    output_avg_step_filepath = os.path.join(output_dir_data_graph, "_10_combined_avg_step_success_rate_has_ambi.png")
    #draw_combined_success_rate_graph(dataset_avg_step_filepath , cot_image_avg_step_filepath, cot_action_avg_step_filepath, ours_avg_step_filepath, output_avg_step_filepath, setting="avg_step") # "avg_step" or "step" or "var"