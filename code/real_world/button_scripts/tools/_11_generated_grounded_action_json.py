
# prompt: 

# based on the grounded boxes and the actions 
# for each action, generate the following format: 
import os 

import json
import _0_t2a_config
from foundation_models.gpt_4o_model import GPT4O
from utils.create_or_replace_path import create_or_replace_path
from utils.extract_json_code import extract_json_code

def merge_bboxes(data):
    """
    Merges bounding boxes for items with the same image_name across multiple lists.
    
    :param data: A list of lists, where each inner list contains dictionaries with 'image_name' and 'bbox'.
    :return: A dictionary with a single key 'bboxes' containing a list of dictionaries for each image_name and their bboxes.
    """
    from collections import defaultdict
    merged_results = defaultdict(list)

    # Collect all bboxes for each image_name
    for sublist in data:
        for item in sublist:
            merged_results[item["image_name"]].append(item["bbox"])

    # Prepare the final structure
    final_result = []
    for image_name, bboxes in merged_results.items():
        final_result.append({
            "image_name": image_name,
            "bbox": bboxes  # This will be a list of bbox lists
        })

    return final_result

prompt = """

The list of actions available for the appliance is listed as follows. 

xxxxx 

Each action falls into one of the following action types: 

"turn_dial_clockwise", "turn_dial_anti_clockwise", "press_dial", "press_button", "press_and_hold_button", "check_digital_display".

Here is the list of grounded boxes for each control element of the appliance. 

yyyyy 

Please generate the following format for each action:

{
    "action": (one of the actions from the given action list, is a string, e.g. press_max_crisp_button),
    "bbox_label": a list of strings, containing the label of the control element that the action is performed on, e.g. ["max_crisp_button"]. The label must be one of the "element_name" in the grounded boxes list. for the case whereby two buttons need to be pressed and held simulataneously, e.g. when the action is press_and_hold_button1_and_button2, the label should be ["button_1", "button_2"].
    "action_type": (one of the types from the following list: press_button, press_and_hold_button, turn_dial_clockwise, turn_dial_anti_clockwise, press_dial. Judge from the action name. for example, if the action name contains "press_and_hold", the action type should be "press_and_hold_button".)
    
}

The output will be a list. I will save the output as a json file. Please do not output anything other than the list of grounded actions.
"""

def verify_data_format(data):
    data = json.loads(data)
    # Check if data is a list
    if not isinstance(data, list):
        print("Data is not a list.")
        return False

    # Iterate over each item in the list
    for item in data:
        # Check if each item is a dictionary
        if not isinstance(item, dict):
            print("Item is not a dictionary.")
            return False
        
        # Check for the presence of all required keys
        required_keys = {"action", "bbox_label", "action_type"}
        if not required_keys.issubset(item):
            print(f"Missing keys in item: {set(required_keys) - set(item.keys())}")
            return False
    return True


def generate_grounded_actions_for_proposed_world_model(prompt, input_action_option_filepath, input_grounded_element_bboxes_filepath, output_proposed_world_model_action_bboxes_filepath):
    
    action_options = ""
    with open(input_action_option_filepath, "r") as f:
        action_options = f.read()
    grounded_element_bboxes = []
    # load json file 
    with open(input_grounded_element_bboxes_filepath, "r") as f:
        grounded_element_bboxes = json.load(f)
    prompt = prompt.replace("xxxxx", action_options)
    prompt = prompt.replace("yyyyy", str(grounded_element_bboxes))
    response = ""
    satisfied = False 
    while not satisfied:
        print("formatting...")
        model = GPT4O()
        response = model.chat_with_text(prompt)
        response = extract_json_code(response)

        satisfied = verify_data_format(response)
        del model
    
    response_with_bbox_coord = json.loads(response)
    for item in response_with_bbox_coord:
        item["bboxes"] = []
        for element in grounded_element_bboxes:
            if element["element_name"] in item["bbox_label"]:
                item["bboxes"].append(element["grounded_bboxes"])
        item["bboxes"] = merge_bboxes(item["bboxes"])   
    response_string = json.dumps(response_with_bbox_coord, indent=4)
    # save the response to the output file as json
    create_or_replace_path(output_proposed_world_model_action_bboxes_filepath)
    with open(output_proposed_world_model_action_bboxes_filepath, "w") as f:
        f.write(response_string)
    pass 

def batch_generate_grounded_actions_for_proposed_world_model(prompt, input_action_option_dir, input_grounded_element_bboxes_dir, output_proposed_world_model_action_bboxes_dir):
    
    action_option_machine_type_files = os.listdir(input_action_option_dir)
    for action_option_machine_type_file in action_option_machine_type_files:
        # list all files ends with txt
        action_option_machine_id_files = [f for f in os.listdir(os.path.join(input_action_option_dir, action_option_machine_type_file)) if f.endswith(".txt")]
        for action_option_machine_id_file in action_option_machine_id_files:
            machine_id = action_option_machine_id_file.split(".")[0].split("_")[-1]
            input_action_option_filepath = os.path.join(input_action_option_dir, action_option_machine_type_file, action_option_machine_id_file)
            #print(input_action_option_filepath)
            if not any(s in input_action_option_filepath for s in ["_1_microwave/_4"]) :
            #    print("skipping ", input_action_option_filepath)
                continue  
            input_grounded_element_bboxes_filepath = os.path.join(input_grounded_element_bboxes_dir, action_option_machine_type_file, machine_id + ".json")
            output_proposed_world_model_action_bboxes_filepath = os.path.join(output_proposed_world_model_action_bboxes_dir, action_option_machine_type_file, machine_id + ".json")
            print(f"processing {input_action_option_filepath}")
            generate_grounded_actions_for_proposed_world_model(prompt, input_action_option_filepath, input_grounded_element_bboxes_filepath, output_proposed_world_model_action_bboxes_filepath)
    pass
"""
input format:

{"element_name": "max_crisp_button", "bboxes": [{"image_name": "0_2", "bbox_id": [26]}, {"image_name": "0_1", "bbox_id": [5]}, {"image_name": "0_0", "bbox_id": [44]}], "grounded_bboxes": [{"image_name": "0_2", "bbox": [0.29411764705882354, 0.4056372549019608, 0.3872549019607843, 0.4215686274509804]}, {"image_name": "0_1", "bbox": [0.2761437908496732, 0.33578431372549017, 0.36437908496732024, 0.35049019607843135]}, {"image_name": "0_0", "bbox": [0.3194444444444444, 0.39889705882352944, 0.4011437908496732, 0.4111519607843137]}]}

and the list of action options:


"""
"""
target output:

{"action": "press_max_crisp_button", "bbox_label": "max_crisp_button", "action_type": "press_button", "bboxes": [{"image_name": "0_1", "bbox": [0.2679738562091503, 0.32965686274509803, 0.37336601307189543, 0.36519607843137253]}, {"image_name": "0_2", "bbox": [0.27941176470588236, 0.40012254901960786, 0.39950980392156865, 0.43566176470588236]}, {"image_name": "0_0", "bbox": [0.30637254901960786, 0.38848039215686275, 0.4084967320261438, 0.4258578431372549]}]}
"""


if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Output Grounded Actions for All Appliances
    #  = Grounded Entity + Action Type
    #
    #######################################
    
    action_options_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_1_action_names/_1_proposed_action_names')
    grounded_element_bboxes_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_bbox/_3_proposed_control_panel_element_bbox')
    
    output_proposed_world_model_action_bboxes_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_1_action_names/_2_proposed_world_model_action_bbox')
    
    batch_generate_grounded_actions_for_proposed_world_model(prompt, action_options_dir, grounded_element_bboxes_dir, output_proposed_world_model_action_bboxes_dir)

    #######################################
    #
    # Output Grounded Actions for One Appliance
    #  = Grounded Entity + Action Type
    #
    #######################################

    action_options_filepath = os.path.expanduser("~/TextToActions/dataset/_4_visual_grounding/_4_proposed_action_names/4_air_fryer/0.txt")

    grounded_element_bboxes_filepath = os.path.expanduser("~/TextToActions/dataset/_4_visual_grounding/_3_proposed_control_panel_element_bbox/4_air_fryer/0.json")

    output_proposed_world_model_action_bboxes_filepath = os.path.expanduser("~/TextToActions/dataset/_4_visual_grounding/_5_proposed_world_model_action_bbox/1_air_fryer/0.json")

    #generate_grounded_actions_for_proposed_world_model(prompt, action_options_filepath, grounded_element_bboxes_filepath, output_proposed_world_model_action_bboxes_filepath)
    
    