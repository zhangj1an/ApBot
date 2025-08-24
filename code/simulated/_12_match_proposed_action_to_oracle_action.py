import importlib.util
import sys
import os 
import ast
import json

sys.path.append(os.path.expanduser("~/RLS_microwave/utils"))
from foundation_models.gpt_4o_model import GPT4O
from utils.create_or_replace_path import create_or_replace_path
from utils.load_string_from_file import load_string_from_file
from utils.extract_list_from_file import extract_list_from_file

def batch_match_simulator_actions_to_bboxes(coco_annotation_root_dir, oracle_appliance_label_dir, output_dir):
    # for each appliance
    # list all dir in the oracle appliance label dir
    machine_type_dir = os.listdir(oracle_appliance_label_dir)
    # list all files in this dir that ends with py 
    for machine_type in machine_type_dir:
        machine_id_files = [f for f in os.listdir(os.path.join(oracle_appliance_label_dir, machine_type)) if f.endswith(".py")]
        coco_annotation_dir = os.path.join(coco_annotation_root_dir, machine_type)
        for machine_id_file in machine_id_files:
            oracle_appliance_label_filepath = os.path.join(oracle_appliance_label_dir, machine_type, machine_id_file)
            oracle_simulator_mapping_output_filepath = os.path.join(output_dir, machine_type, machine_id_file.split(".")[0] + ".json")
            match_simulator_actions_to_bboxes(coco_annotation_dir, oracle_appliance_label_filepath, oracle_simulator_mapping_output_filepath)
            #exit()

    # find its coco annotation dir
    # find its output filepath
    pass 

# given coco annotations, given oracle simulator action to coco label mapping, map simulator actions to coco bboxes from all images 
def match_simulator_actions_to_bboxes(coco_annotation_dir, oracle_appliance_label_filepath, oracle_simulator_mapping_output_filepath):
    
    oracle_simulator_action_to_coco_label_list = extract_list_from_file(oracle_appliance_label_filepath)

    machine_type = oracle_appliance_label_filepath.split("/")[-2]
    machine_id = oracle_appliance_label_filepath.split("/")[-1].split(".")[0]

    # list all files in the coco annotation dir that ends with json and start with machine_id
    coco_annotation_files = [f for f in os.listdir(coco_annotation_dir) if f.endswith(".json") and f.split("_")[0] == machine_id]
    test = [f for f in os.listdir(coco_annotation_dir) if f.endswith(".json")]
    #print("coco_annotation_files: ", coco_annotation_files)
    #print("test: ", test)
    
    # for each file, load the json, and extract the bbox of the label that matches the oracle simulator action
    for oracle_simulator_action_to_coco_label in oracle_simulator_action_to_coco_label_list:
            
        action = oracle_simulator_action_to_coco_label["action"]
        #print("processing action: ", action)
        bbox_labels = oracle_simulator_action_to_coco_label["bbox_label"]
        action_type = oracle_simulator_action_to_coco_label["action_type"]

        oracle_simulator_action_to_coco_label["bboxes"] = []
        
        for coco_annotation_file in coco_annotation_files:
            #print("processing file: ", coco_annotation_file)
            image_name = coco_annotation_file.split(".")[0]
            coco_annotation_filepath = os.path.join(coco_annotation_dir, coco_annotation_file)

            with open(coco_annotation_filepath, "r") as f:
                coco_annotation = json.load(f)
            
            categories = coco_annotation["categories"]
            image_width = coco_annotation["images"][0]["width"]
            image_height = coco_annotation["images"][0]["height"]
            # for each action in the oracle simulator action list, extract the bbox of the label that matches the action
        
            
            data_dict = {}
            data_dict["image_name"] = image_name
            data_dict["bbox"] = []
            # extract the bbox of the label that matches the action
            for annotation in coco_annotation["annotations"]:
                annotation_label = next((item for item in categories if item['id'] == annotation["category_id"]), None)["name"]
                
                #print("bbox_label: ", bbox_label)
                

                if  annotation_label in bbox_labels:
                    #print(f"annotation_label: {annotation_label}, bbox_labels: {bbox_labels}")
                    bbox = annotation["bbox"]
                    
                    # save the output to a file in the output dir

                    x_min = bbox[0]
                    y_min = bbox[1]
                    x_max = bbox[0] + bbox[2]
                    y_max = bbox[1] + bbox[3]
                    final_bbox = [
                            x_min / image_width, y_min / image_height,
                            x_max / image_width, y_max / image_height
                        ],
                    final_bbox = final_bbox[0]
                    data_dict["bbox"].append(final_bbox)
                    #print("data_dict: ", data_dict)
                    #oracle_simulator_action_to_coco_label["bboxes"].append({"image_name": image_name, "bbox": final_bbox})
            oracle_simulator_action_to_coco_label["bboxes"].append(data_dict)
                    
                    


    create_or_replace_path(oracle_simulator_mapping_output_filepath)
    # save the output as a json file
    with open(oracle_simulator_mapping_output_filepath, "w") as f:
        json.dump(oracle_simulator_action_to_coco_label_list, f, indent=4)
    # save the output to a file in the output dir
    # desired output : oracle simulator action, appending  a list of dict {img name, bbox in 0, 1 format} too
    pass 

def check_is_center_inside(proposed_bbox_list, oracle_bbox_list):
    """
    Check if each bbox in proposed_bbox_list has an IoU > threshold with at least one bbox in oracle_bbox_list.
    """
    if len(proposed_bbox_list) != len(oracle_bbox_list):
        return False
    for proposed_bbox in proposed_bbox_list:
        # Track if the current proposed bbox meets the IoU condition with any oracle bbox
        criteria_met = False
        for oracle_bbox in oracle_bbox_list:
            criteria_met = is_center_inside(proposed_bbox, oracle_bbox)
            if criteria_met:
                break #Stop checking further if one meets the threshold
        if not criteria_met:
            # If any proposed bbox does not meet the condition, return False immediately
            return False
    
    return True

def check_iou_threshold(proposed_bbox_list, oracle_bbox_list, threshold=0.2):
    """
    Check if each bbox in proposed_bbox_list has an IoU > threshold with at least one bbox in oracle_bbox_list.
    """
    if len(proposed_bbox_list) != len(oracle_bbox_list):
        return False
    for proposed_bbox in proposed_bbox_list:
        # Track if the current proposed bbox meets the IoU condition with any oracle bbox
        iou_met = False
        for oracle_bbox in oracle_bbox_list:
            iou = calculate_iou(proposed_bbox, oracle_bbox)
            if iou > threshold:
                iou_met = True
                break  # Stop checking further if one meets the threshold
        if not iou_met:
            # If any proposed bbox does not meet the condition, return False immediately
            return False
    
    return True

def calculate_iou(bbox1, bbox2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.
    Bounding boxes are in the format [xmin, ymin, xmax, ymax] with normalized coordinates.
    """
    x1_min, y1_min, x1_max, y1_max = bbox1
    x2_min, y2_min, x2_max, y2_max = bbox2
    
    # Calculate intersection coordinates
    inter_xmin = max(x1_min, x2_min)
    inter_ymin = max(y1_min, y2_min)
    inter_xmax = min(x1_max, x2_max)
    inter_ymax = min(y1_max, y2_max)
    
    # Calculate intersection area
    inter_width = max(0, inter_xmax - inter_xmin)
    inter_height = max(0, inter_ymax - inter_ymin)
    inter_area = inter_width * inter_height
    
    # Calculate union area
    area1 = (x1_max - x1_min) * (y1_max - y1_min)
    area2 = (x2_max - x2_min) * (y2_max - y2_min)
    union_area = area1 + area2 - inter_area
    
    # Calculate IoU
    iou = inter_area / union_area
    return iou

def is_center_inside(bbox1, bbox2):
    # Calculate the center of bbox1
    center_x = (bbox1[0] + bbox1[2]) / 2
    center_y = (bbox1[1] + bbox1[3]) / 2
    
    # Check if the center of bbox1 is inside bbox2
    if (bbox2[0] <= center_x <= bbox2[2]) and (bbox2[1] <= center_y <= bbox2[3]):
        return True
    else:
        return False

def convert_actions_from_proposed_to_oracle(proposed_actions_filepath, oracle_actions_filepath, output_filepath):

    # load json file 
    with open(proposed_actions_filepath, "r") as f:
        proposed_actions = json.load(f)
    with open(oracle_actions_filepath, "r") as f:
        oracle_actions = json.load(f)
    
    action_mappings = {}
    # The mapping direction is: proposed action -> oracle action
    # for each proposed action, find the corresponding oracle action
    for proposed_action in proposed_actions:
        
        #proposed_bbox_label = proposed_action["bbox_label"]
        proposed_bboxes = proposed_action["bboxes"]
        proposed_action_name = proposed_action["action"]
        proposed_action_type = proposed_action["action_type"]
        #print("processing action: ", proposed_action_name )
        action_mappings[proposed_action_name] = set()
        # find the corresponding oracle action
        for oracle_action in oracle_actions:
            
            #oracle_bbox_label = oracle_action["bbox_label"]
            oracle_action_name = oracle_action["action"]
            oracle_action_type = oracle_action["action_type"]
            oracle_bboxes = oracle_action["bboxes"]
            if oracle_action_type != proposed_action_type:
                continue
            
            for proposed_bbox in proposed_bboxes:
                proposed_bbox_image_name = proposed_bbox["image_name"]
                proposed_bbox_bbox = proposed_bbox["bbox"]
                for oracle_bbox in oracle_bboxes:
                    oracle_bbox_image_name = oracle_bbox["image_name"]
                    oracle_bbox_bbox = oracle_bbox["bbox"]
                    if proposed_bbox_image_name == oracle_bbox_image_name:
                        
                        # the bbox may have length 1 or length 2 
                        if check_is_center_inside(proposed_bbox_bbox, oracle_bbox_bbox):
                            action_mappings[proposed_action_name].add(oracle_action_name)
                        else:
                            pass
                        """
                        threshold = 0.2
                        threshold_met = check_iou_threshold(proposed_bbox_bbox, oracle_bbox_bbox, threshold)
                        if threshold_met:
                            action_mappings[proposed_action_name].add(oracle_action_name)
                        """
        action_mappings[proposed_action_name] = list(action_mappings[proposed_action_name])
    # save the dict into a json file 

    create_or_replace_path(output_filepath)
    with open(output_filepath, "w") as f:
        json.dump(action_mappings, f)
    """
    input:
     {
        "action": "turn_power_selector_dial_clockwise",
        "bbox_label": [
            "power_selector_dial"
        ],
        "action_type": "turn_dial",
        "bboxes": [
            {
                "image_name": "0_2",
                "bbox": [
                    [
                        0.6681855916976929,
                        0.20386625826358795,
                        0.7526972889900208,
                        0.3188038766384125
                    ]
                ]
            },
        ]
    }
    """
    """
    oracle:

    {
        "action": "turn_power_selector_dial_clockwise",
        "bbox_label": [
            "0_power_dial"
        ],
        "action_type": "turn_dial",
        "bboxes": [
            {
                "image_name": "0_1",
                "bbox": [
                    [
                        0.4,
                        0.2843501326259947,
                        0.6613207547169812,
                        0.41750663129973475
                    ]
                ]
            },
        ]
    } 
    """
    pass 

def batch_convert_actions_from_proposed_to_oracle(proposed_actions_dir, oracle_actions_dir, output_dir):
    # list all dir in proposed_actions 
    proposed_actions_machine_type_dir = os.listdir(proposed_actions_dir)
    # list all files in this dir that ends with json
    for proposed_actions_machine_type in proposed_actions_machine_type_dir:
        proposed_actions_machine_id_files = [f for f in os.listdir(os.path.join(proposed_actions_dir, proposed_actions_machine_type)) if f.endswith(".json")]
        
        # for each file, perform the conversion
        for proposed_actions_machine_id_file in proposed_actions_machine_id_files:
            proposed_actions_filepath = os.path.join(proposed_actions_dir, proposed_actions_machine_type, proposed_actions_machine_id_file)
            oracle_actions_filepath = os.path.join(oracle_actions_dir, proposed_actions_machine_type, proposed_actions_machine_id_file)
            output_filepath = os.path.join(output_dir, proposed_actions_machine_type, proposed_actions_machine_id_file)
            convert_actions_from_proposed_to_oracle(proposed_actions_filepath, oracle_actions_filepath, output_filepath)
    pass 



    """
    {"press_max_crisp_button": "press_max_crisp_button", "press_air_fry_button": "press_air_fry_button", "press_air_roast_button": "press_air_broil_button", "press_air_broil_button": "press_dehydrate_button", "press_bake_button": "press_bake_button", "press_reheat_button": "press_reheat_button",}
    """



def batch_match_simulator_buttons_bbox_index_to_oracle_actions(proposed_button_bbox_dir = "TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_bbox/_6_visualised_localised_buttons_legends/", oracle_action_bbox_dir ="TextToActions/dataset/simulated/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping/", output_dir = "TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_bbox/_7_proposed_buttons_to_oracle_action_mapping"):
    # used for CoT input ground truth: match action type and bbox index to ground truth actions, if any.
    
    proposed_buttons_machine_type_dir = os.listdir(proposed_button_bbox_dir)
    for proposed_buttons_machine_type in proposed_buttons_machine_type_dir:
        proposed_actions_machine_id_dir = [f for f in os.listdir(os.path.join(proposed_button_bbox_dir, proposed_buttons_machine_type))]
        for proposed_actions_machine_id in proposed_actions_machine_id_dir:
            proposed_actions_machine_id_filenames = os.listdir(os.path.join(proposed_button_bbox_dir, proposed_buttons_machine_type, proposed_actions_machine_id))
            oracle_action_bbox_filepath = os.path.join(oracle_action_bbox_dir, proposed_buttons_machine_type, proposed_actions_machine_id + ".json")
            for proposed_actions_machine_id_filename in proposed_actions_machine_id_filenames:
                proposed_actions_machine_id_filepath = os.path.join(proposed_button_bbox_dir, proposed_buttons_machine_type, proposed_actions_machine_id, proposed_actions_machine_id_filename)
                output_filepath = os.path.join(output_dir, proposed_buttons_machine_type, proposed_actions_machine_id, proposed_actions_machine_id_filename)
                match_simulator_buttons_bbox_index_to_oracle_actions(proposed_actions_machine_id_filepath, oracle_action_bbox_filepath, output_filepath)
                #exit()
                

    pass 

def match_simulator_buttons_bbox_index_to_oracle_actions(proposed_button_bbox_filepath="TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_bbox/_6_visualised_localised_buttons_legends/_1_microwave/0/label.json", oracle_action_bbox_filepath="TextToActions/dataset/simulated/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping/_1_microwave/0.json", output_filepath="TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_bbox/_7_proposed_buttons_to_oracle_action_mapping"):
    # firstly match a single button index to actinos 
    # the match pair button indexs to actions 
    oracle_simulator_action_to_coco_label_list = extract_list_from_file(oracle_action_bbox_filepath)
    proposed_buttons_bboxes = ""
    with open(proposed_button_bbox_filepath, "r") as f:
        proposed_buttons_bboxes = json.load(f)
    image_name = proposed_button_bbox_filepath.split("/")[-1].split(".")[0]
    output_proposed_bbox_index_to_action_mapping= {}
    # iterate over a single proposed buttons bboxes dict key
    for button_bbox_index in proposed_buttons_bboxes.keys():
        button_bbox_coord = proposed_buttons_bboxes[button_bbox_index] 
        for action_dict in oracle_simulator_action_to_coco_label_list:
            action_bbox_list = action_dict["bboxes"]
            for action_bbox_dict in action_bbox_list:
                if action_bbox_dict["image_name"] == image_name:
                    oracle_action_bbox = action_bbox_dict["bbox"]
                    if len(oracle_action_bbox) == 1 and is_center_inside(button_bbox_coord, oracle_action_bbox[0]):
                        action_type = action_dict["action_type"]
                        action_name = action_dict["action"]

                        # firstly check if output dict has the key. if not, create it 
                        if button_bbox_index not in output_proposed_bbox_index_to_action_mapping.keys():
                            output_dict = {}
                            output_dict["bbox"] = [button_bbox_coord]
                            output_dict["actions"] = {}
                            output_dict["actions"][action_type] = action_name
                            output_proposed_bbox_index_to_action_mapping[button_bbox_index] = output_dict
                        else:
                            output_proposed_bbox_index_to_action_mapping[button_bbox_index]["actions"][action_type] = action_name
    
    # now consider bbox index pairs 
    for button_bbox_index_1 in proposed_buttons_bboxes.keys():
        for button_bbox_index_2 in proposed_buttons_bboxes.keys():
            if button_bbox_index_1 == button_bbox_index_2:
                continue 
            button_bbox_coord_1 = proposed_buttons_bboxes[button_bbox_index_1]
            button_bbox_coord_2 = proposed_buttons_bboxes[button_bbox_index_2] 

            for action_dict in oracle_simulator_action_to_coco_label_list:
                action_bbox_list = action_dict["bboxes"]
                for action_bbox_dict in action_bbox_list:
                    if action_bbox_dict["image_name"] == image_name:
                        oracle_action_bbox_list = action_bbox_dict["bbox"]
                        if len(oracle_action_bbox_list) == 2 and check_is_center_inside([button_bbox_coord_1, button_bbox_coord_2], oracle_action_bbox_list):
                            action_type = action_dict["action_type"]
                            action_name = action_dict["action"]

                            # firstly check if output dict has the key. if not, create it 
                            if f"{button_bbox_index_1}_{button_bbox_index_2}" not in output_proposed_bbox_index_to_action_mapping.keys():
                                output_dict = {}
                                output_dict["bbox"] = [button_bbox_coord_1, button_bbox_coord_2]
                                output_dict["actions"] = {}
                                output_dict["actions"][action_type] = action_name
                                output_proposed_bbox_index_to_action_mapping[f"{button_bbox_index_1}_{button_bbox_index_2}"] = output_dict
                            else:
                                output_proposed_bbox_index_to_action_mapping[f"{button_bbox_index_1}_{button_bbox_index_2}"]["actions"][action_type] = action_name
    create_or_replace_path(output_filepath)
    with open(output_filepath, "w") as f:
        json.dump(output_proposed_bbox_index_to_action_mapping, f, indent=4)

    pass 


if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    # comparison criteria: as long as the center of the proposed bbox falls into the oracle bbox, it is considered grounded correctly 

    #######################################
    # For our method: 
    # Map Simulator Actions to BBox
    #
    #######################################
    
    coco_annotation_root_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_0_control_panel_images_groundtruth_annotation' )
    oracle_appliance_label_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_2_map_oracle_action_to_annotation_label')
    oracle_simulator_mapping_output_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping')

    coco_annotation_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_0_control_panel_images_groundtruth_annotation/_3_rice_cooker' )
    oracle_appliance_label_filepath = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_2_map_oracle_action_to_annotation_label/_3_rice_cooker/0.py')
    oracle_simulator_mapping_output_filepath = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping/_3_rice_cooker/0.json')

    #match_simulator_actions_to_bboxes(coco_annotation_dir, oracle_appliance_label_filepath, oracle_simulator_mapping_output_filepath)

    #batch_match_simulator_actions_to_bboxes(coco_annotation_root_dir, oracle_appliance_label_dir, oracle_simulator_mapping_output_dir)


    #######################################
    # For our method:
    # Map Grounded Actions to Simulator Actions
    #
    #######################################
    gpt_model_type= "gpt-4o-2024-11-20"

    proposed_actions_filepath = os.path.expanduser(f'~/TextToActions/dataset/_4_visual_grounding/{gpt_model_type}/_4_proposed_world_model_action_bbox/_1_microwave/0.json')
    oracle_actions_filepath = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping/_1_microwave/0.json')
    convert_actions_from_proposed_to_oracle_filepath = os.path.expanduser('~/TextToActions/dataset/_4_visual_grounding/_5_proposed_to_oracle_action_mapping/_1_microwave/0.json')

    proposed_actions_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_1_action_names/_2_proposed_world_model_action_bbox')
    oracle_actions_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping')
    convert_actions_from_proposed_to_oracle_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_1_action_names/_3_proposed_to_oracle_action_mapping')
    #batch_convert_actions_from_proposed_to_oracle(proposed_actions_dir, oracle_actions_dir, convert_actions_from_proposed_to_oracle_dir)
    #convert_actions_from_proposed_to_oracle(proposed_actions_filepath, oracle_actions_filepath, convert_actions_from_proposed_to_oracle_filepath)


    ###############################################
    #
    # For CoT method: match (bbox, action_type) to oracle actions 
    #
    ###############################################

    proposed_button_bbox_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_6_visualised_localised_buttons_legends')
    oracle_action_bbox_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping')
    output_bbox_to_action_name_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_7_proposed_buttons_to_oracle_action_mapping')
    batch_match_simulator_buttons_bbox_index_to_oracle_actions(proposed_button_bbox_dir, oracle_action_bbox_dir, output_bbox_to_action_name_dir)
    #match_simulator_buttons_bbox_index_to_oracle_actions(os.path.join(proposed_button_bbox_dir, "_2_washing_machine", "3", "3_0.json"), os.path.join(oracle_action_bbox_dir, "_2_washing_machine", "3.json"), os.path.join(output_bbox_to_action_name_dir, "_2_washing_machine", "3", "3_0.json"))