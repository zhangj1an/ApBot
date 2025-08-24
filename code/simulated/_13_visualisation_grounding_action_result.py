# 1. grade the visual grounding results:
# a rough estimate, as the TP can be wrong,
# total score is the total number of oracle actions 

import os 
import sys
sys.path.append(os.path.expanduser("~/TextToActions/code"))
import simulated._0_t2a_config
import json
from simulated.utils.create_or_replace_path import create_or_replace_path
from PIL import Image, ImageDraw, ImageFont
from foundation_models.gpt_4o_model import GPT4O
#from _3_detect_bbox_from_photos import group_boxes_within_distance, calculate_area
#from foundation_models.owlv2_crane5_query import OWLViT, visualize_image
from simulated.utils.task.visualize_image import visualize_bboxes_with_legend
def get_precision_and_recall(TP, FP, FN):
    if TP + FP == 0:
        precision = 0
    else: 
        precision = TP / (TP + FP)
    if TP + FN == 0:
        recall = 0
    else:
        recall = TP / (TP + FN)

    return precision, recall
def evaluate_visual_grounding_action_result(proposed_action_to_oracle_action_mapping_filepath, oracle_actions_filepath):
    with open(proposed_action_to_oracle_action_mapping_filepath, "r") as f:
        proposed_action_to_oracle_action_mapping = json.load(f)
    with open(oracle_actions_filepath, "r") as f:
        oracle_actions = json.load(f)

    
    TP = 0
    FP = 0
    FN = 0
    fn_names = []
    total_action = len(oracle_actions)
    # TP: the oracle action is present in the first choice of the grounded actions (true value is lower)
    # FP: the actions are proposed but cannot be grounded to any oracle actions (true value is higher)
    # FN: the oracle action is not present in the first choice of the grounded actions (true value is higher)
    # precision: TP / (TP + FP) (true value is lower)
    # recall: TP / (TP + FN) (true value is lower)

    all_oracle_options = []
    for oracle_action in oracle_actions:
        all_oracle_options += oracle_action["action"]
    for oracle_action in oracle_actions:
        
        oracle_action_name = oracle_action["action"]
        if oracle_action_name == "check_display" or oracle_action_name == "check_digital_display":
            continue
        found = False
        for proposed_action in proposed_action_to_oracle_action_mapping:
            
            if len(proposed_action_to_oracle_action_mapping[proposed_action])>0 and oracle_action_name in proposed_action_to_oracle_action_mapping[proposed_action][0]:
                # use gpt to check if the action is matching 
                # oracle action name 
                # proposed_action 
                # is it oracle action is the closest match among all available oracle actions 
                
                joined_options = "\n".join(all_oracle_options)
                prompt = (
                    f"An appliance has the following available actions:\n{joined_options}. "
                    f"Semantically, do you think the closest action name to {proposed_action} is {oracle_action_name}?\n\n"
                    "Answer with 'yes' or 'no'."
                )

                model = GPT4O()
                #print("deciding between proposed:{} and oracle: {}".format(proposed_action, oracle_action_name))
                response = model.chat_with_text(prompt).lower()
                #print("Response: ", response) 
                

                if "yes" in response:
                    TP += 1
                    found = True 
                elif "no" in response:
                    FP += 1 
        if not found:
            FN += 1
            fn_names += [oracle_action_name]

    
    for proposed_action in proposed_action_to_oracle_action_mapping:
        if len(proposed_action_to_oracle_action_mapping[proposed_action]) == 0:
            FP += 1

    precision, recall = get_precision_and_recall(TP, FP, FN)

    return total_action, TP, FP, FN, precision, recall, fn_names


def batch_evaluate_visual_grounding_action_result(oracle_actions_dir, proposed_action_to_oracle_action_mapping_dir, visual_grounding_action_score_dir):

    create_or_replace_path(visual_grounding_action_score_dir)
    result = []
    machine_level_result = []
    overall_result = []
    machine_type_list = [f for f in os.listdir(oracle_actions_dir) if os.path.isdir(os.path.join(oracle_actions_dir, f))]
    overall_TP = 0
    overall_FP = 0
    overall_FN = 0
    overall_total_action = 0
    overall_fn_names = []
    for machine_type in machine_type_list:
        machine_level_TP = 0
        machine_level_FP = 0
        machine_level_FN = 0
        machine_level_total_action = 0
        machine_level_fn_names = []
        machine_id_files = [f for f in os.listdir(os.path.join(oracle_actions_dir, machine_type)) if f.endswith(".json")]
        for machine_id_file in machine_id_files:
            machine_id = machine_id_file.split(".")[0]
            proposed_action_to_oracle_action_mapping_filepath = os.path.join(proposed_action_to_oracle_action_mapping_dir, machine_type, machine_id + ".json")
            oracle_actions_filepath = os.path.join(oracle_actions_dir, machine_type, machine_id + ".json")

            
            print("Evaluating visual grounding action result for machine type: {}, machine id: {}".format(machine_type, machine_id))
            total_action, TP, FP, FN, precision, recall, fn_names = evaluate_visual_grounding_action_result(proposed_action_to_oracle_action_mapping_filepath, oracle_actions_filepath)
            machine_level_TP += TP
            machine_level_FP += FP
            machine_level_FN += FN
            machine_level_total_action += total_action
            machine_level_fn_names += fn_names
            overall_TP += TP
            overall_FP += FP
            overall_FN += FN
            overall_total_action += total_action
            overall_fn_names += fn_names
            datapoint_result = {"machine_type": machine_type,
                    "machine_id": machine_id,
                    "total_action": total_action,
                    "TP": TP,
                    "FP": FP,
                    "FN": FN,
                    "precision": precision,
                    "recall": recall,
                    "fn_actions": fn_names
                }
            result.append(datapoint_result)
            print("Result for machine type: {}, machine id: {}, total action: {}, TP: {}, FP: {}, FN: {}, precision: {}, recall: {}".format(machine_type, machine_id, total_action, TP, FP, FN, precision, recall))
            #exit()
        machine_level_precision, machine_level_recall = get_precision_and_recall(machine_level_TP, machine_level_FP, machine_level_FN)
        datapoint_result = {"machine_type": machine_type,
                "machine_level_total_action": machine_level_total_action,
                "machine_level_TP": machine_level_TP,
                "machine_level_FP": machine_level_FP,
                "machine_level_FN": machine_level_FN,
                "machine_level_precision": machine_level_precision,
                "machine_level_recall": machine_level_recall,
                "machine_level_fn_actions": machine_level_fn_names
            }
        machine_level_result.append(datapoint_result)

    overall_precision, overall_recall = get_precision_and_recall(overall_TP, overall_FP, overall_FN)
    overall_result = {"overall_TP": overall_TP,
                      "overall_total_action": overall_total_action,
            "overall_FP": overall_FP,
            "overall_FN": overall_FN,
            "overall_precision": overall_precision,
            "overall_recall": overall_recall,
            "overall_fn_actions": overall_fn_names
        }
    instance_level_result_filepath = os.path.join(visual_grounding_action_score_dir, "_1_instance_level.json")
    create_or_replace_path(instance_level_result_filepath)
    with open(instance_level_result_filepath, "w") as f:
        json.dump(result, f, indent=4)
    
    machine_level_result_filepath =  os.path.join(visual_grounding_action_score_dir, "_2_machine_type_level.json") 
    create_or_replace_path(machine_level_result_filepath)
    with open(machine_level_result_filepath, "w") as f:
        json.dump(machine_level_result, f, indent=4)
    
    overall_result_filepath = os.path.join(visual_grounding_action_score_dir, "_3_overall.json") 
    create_or_replace_path(overall_result_filepath)
    with open(overall_result_filepath, "w") as f:
        json.dump(overall_result, f, indent=4)

def add_or_update_item(items, new_item):
    """
    Adds a new item to the list or updates the label of an existing item if the bbox matches.

    :param items: List of dictionaries, each containing 'bbox' and 'label'.
    :param new_item: Dictionary with 'bbox' and 'label' to add or merge.
    :return: None (the list is modified in place)
    """
    for item in items:
        if item['bbox'] == new_item['bbox']:
            # If the bbox matches, concatenate the labels and return
            item['label'] += "\n" + new_item['label']
            return False
    # If no existing bbox matches, add the new item to the list
    items.append(new_item)
    return True

def batch_visualise_actions(oracle_action_mapping_dir, control_panel_images_dir, visualisation_output_dir):
    machine_type_list = [f for f in os.listdir(oracle_action_mapping_dir) if os.path.isdir(os.path.join(oracle_action_mapping_dir, f))]
    for machine_type in machine_type_list:
        machine_id_files = [f for f in os.listdir(os.path.join(oracle_action_mapping_dir, machine_type)) if f.endswith(".json")]
        for machine_id_file in machine_id_files:
            machine_id = machine_id_file.split(".")[0]
            oracle_action_mapping_filepath = os.path.join(oracle_action_mapping_dir, machine_type, machine_id + ".json")
            control_panel_image_machine_type_dir = os.path.join(control_panel_images_dir, machine_type)
            visualisation_output_machine_type_dir = os.path.join(visualisation_output_dir, machine_type)
            #if "_1_microwave/4" not in oracle_action_mapping_filepath:
            #    continue
            #if not any(substring in oracle_action_mapping_filepath for substring in ["_1_microwave/1", "_1_microwave/2","_1_microwave/3", "_3_rice_cooker/0", "_3_rice_cooker/3"]):
            #    continue
            visualise_actions_in_single_image(oracle_action_mapping_filepath, control_panel_image_machine_type_dir, visualisation_output_machine_type_dir, machine_id)
            

    pass 


def add_text_to_the_right_of_image(image, text, text_width = 100):
    """
    Adds a chunk of text below an image.

    :param image: A PIL Image object.
    :param text: The text string to add below the image.
    :param text_height: The height of the text area in pixels.
    :return: A new PIL Image object with the text added.
    """
    width, height = image.size

    # Create a new image with extra space for the text
    new_image = Image.new('RGB', (width + text_width, height ), (255, 255, 255))
    new_image.paste(image, (0, 0))

    # Initialize ImageDraw
    draw = ImageDraw.Draw(new_image)

    # Load a default font or a specified font with size
    font = ImageFont.load_default()

    # Calculate text position for horizontal centering and padding from the bottom
    _, _, text_width, text_height = draw.textbbox((0, 0), text=text, font=font)

    text_x = width + 10 
    text_y = (height - text_height) / 2 

    # Draw the text
    draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

    return new_image


def visualise_actions_in_single_image(oracle_action_mapping_filepath, control_panel_image_machine_type_dir, visualisation_output_machine_type_dir, machine_id):
    """
    Processes oracle action mapping and visualizes all bounding boxes on a single image with a legend.
    """
    # Load the oracle actions
    with open(oracle_action_mapping_filepath, "r") as f:
        oracle_actions = json.load(f)
    
    # List all files in the control panel image directory
    image_files = [f for f in os.listdir(control_panel_image_machine_type_dir) if f.endswith((".jpg", ".jpeg", ".png"))]
    image_files = [f for f in image_files if f.startswith(machine_id)]
    
    for image_file in image_files:
        annotation_info = []
        image_name = image_file.split(".")[0]
        
        for oracle_action in oracle_actions:
            bboxes = oracle_action["bboxes"]
            action_name = oracle_action["action"]
            for item in bboxes:
                if item["image_name"] == image_name:
                    bbox_list = item["bbox"]
                    for bbox in bbox_list:
                        annotation_info.append({"bbox": bbox, "label": action_name})
        
        # Define paths
        image_path = os.path.join(control_panel_image_machine_type_dir, image_file)
        output_savepath = os.path.join(visualisation_output_machine_type_dir, machine_id, f"{image_name}.jpg")
        os.makedirs(os.path.dirname(output_savepath), exist_ok=True)
        
        # Visualize actions with legend
        if len(annotation_info) > 0:
            visualize_bboxes_with_legend(image_path, annotation_info, output_savepath, "", setting="with_label")
if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    ############################################
    # 
    #  1. evaluation grounding action result
    # 
    ############################################
    proposed_action_to_oracle_action_mapping_dir = os.path.expanduser('~/TextToActions/datasetv2/simulated/_4_visual_grounding/gpt-4o-2024-11-20/_1_action_names/_3_proposed_to_oracle_action_mapping')

    oracle_action_mapping_dir = os.path.expanduser('~/TextToActions/datasetv2/simulated/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping')

    visual_grounding_action_score_dir = os.path.expanduser('~/TextToActions/datasetv2/simulated/_6_results/_1_visual_grounding_action_results')

    proposed_action_to_oracle_action_mapping_filepath = os.path.join(proposed_action_to_oracle_action_mapping_dir, "_1_microwave/0.json")

    oracle_actions_filepath = os.path.join(oracle_action_mapping_dir, "_1_microwave/0.json")


    #batch_evaluate_visual_grounding_action_result(oracle_action_mapping_dir, proposed_action_to_oracle_action_mapping_dir, visual_grounding_action_score_dir)

    ############################################
    # 
    # 2. visualise oracle actions
    # 
    ############################################

    control_panel_images_dir = os.path.expanduser('~/TextToActions/datasetv2/simulated/_2_control_panel_images/_0_raw')
    visualisation_oracle_output_dir = os.path.expanduser('~/TextToActions/datasetv2/simulated/_6_results/_2_visualise_oracle_actions')
    #batch_visualise_actions(oracle_action_mapping_dir, control_panel_images_dir, visualisation_oracle_output_dir)

    ############################################
    #
    # 3. visualise generated actions
    #
    ############################################

    gpt_model_type = "gpt-4o-2024-11-20"
    visualisation_proposed_action_output_dir = os.path.expanduser(f'~/TextToActions/datasetv2/simulated/_6_results/_3_visualise_proposed_actions/{gpt_model_type}/')

    proposed_actions_bbox_dir = os.path.expanduser(f'~/TextToActions/datasetv2/simulated/_4_visual_grounding/{gpt_model_type}/_1_action_names/_2_proposed_world_model_action_bbox')
    batch_visualise_actions(proposed_actions_bbox_dir, control_panel_images_dir, visualisation_proposed_action_output_dir)


