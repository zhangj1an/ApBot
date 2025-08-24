from PIL import Image, ImageDraw
import re
import requests
import base64
from io import BytesIO
import os 
import sys
import json
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.create_or_replace_path import create_or_replace_path
from simulated._13_visualisation_grounding_action_result import batch_evaluate_visual_grounding_action_result
def convert_pil_image_to_base64(image: Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


def extract_points_from_response(text):
    # Check for <points ...> multi-point tag
    multi_matches = re.findall(r'x(\d+)="([\d.]+)" y\1="([\d.]+)"', text)
    if multi_matches:
        points = []
        for _, x,y in multi_matches:
            points.append((round(float(x), 1), round(float(y), 1)))
        return points

    # Check for <point ...> single-point tag
    single_match = re.search(r'<point x="([\d.]+)" y="([\d.]+)"', text)
    if single_match:
        x = round(float(single_match.group(1)))
        y = round(float(single_match.group(2)))
        return [(x, y)]

    return []


def draw_point_on_image(image, points, radius=5, color="red"):
    draw = ImageDraw.Draw(image)
    for x_percent, y_percent in points:
        width, height = image.size
        x = (x_percent / 100) * width
        y = (y_percent / 100) * height
        left_up = (x - radius, y - radius)
        right_down = (x + radius, y + radius)
        draw.ellipse([left_up, right_down], outline=color, width=2)
    return image

def chat(prompt, image, meta_prompt=""):
    base64_image = convert_pil_image_to_base64(image)
    payload = {
        "prompt": meta_prompt + '\n' + prompt,
        "image": base64_image,
        "max_new_tokens": 2048,
        "temperature": 0.0
    }
    response = requests.post(
        "http://crane6.d2.comp.nus.edu.sg:4007/molmo_chat", 
        json=payload,
    ).json()
    return response["text"]

def batch_test_visual_grounding_for_one_appliance(input_action_option_dir, input_image_dir, output_action_coords_dir,output_visualisation_dir ):
    action_option_machine_type_files = os.listdir(input_action_option_dir)
    for action_option_machine_type_file in action_option_machine_type_files:
        # list all files ends with txt
        action_option_machine_id_files = [f for f in os.listdir(os.path.join(input_action_option_dir, action_option_machine_type_file)) if f.endswith(".txt")]
        for action_option_machine_id_file in action_option_machine_id_files:
            machine_id = action_option_machine_id_file.split(".")[0].split("_")[-1]
            input_action_option_filepath = os.path.join(input_action_option_dir, action_option_machine_type_file, action_option_machine_id_file)
            if any(s in input_action_option_filepath for s in ["_6_coffee_machine"]):
            #    print("skipping ", input_action_option_filepath)
                continue 
            if any (s in input_action_option_filepath for s in ["_1_dehumidifier/_1"]) :
                continue
            print(f"processing {action_option_machine_type_file}/{action_option_machine_id_file}", )
            input_images = os.listdir(os.path.join(input_image_dir, action_option_machine_type_file))
            image_filepath = ""
            for input_image in input_images:
                if input_image.split("_")[0] == machine_id:
                    image_filepath = os.path.join(input_image_dir, action_option_machine_type_file, input_image)
            output_action_coords_filepath = os.path.join(output_action_coords_dir, action_option_machine_type_file, machine_id + ".json")
            output_visualisation_specific_dir = os.path.join(output_visualisation_dir, action_option_machine_type_file, machine_id)
            create_or_replace_path(output_visualisation_specific_dir)
            create_or_replace_path(output_action_coords_filepath)
            test_visual_grounding_for_one_appliance(input_action_option_filepath, image_filepath, output_action_coords_filepath, output_visualisation_specific_dir)
            
    
def test_visual_grounding_for_one_appliance(list_of_action_names_file, appliance_image_filepath, output_action_coords_filepath, output_visualisation_dir):

    with open(list_of_action_names_file, "r") as f:
        list_of_action_names = f.read()
        # convert to a list of non-empty lines
        list_of_action_names = [line.strip() for line in list_of_action_names.split("\n") if line.strip()]
    # load image
    image = Image.open(appliance_image_filepath)
    image_name = appliance_image_filepath.split("/")[-1].split(".")[0]
    # for each action, query molmo to get a list of coords 
    grounding_dict = {"image_name": image_name, "actions": {}}
    for action_name in list_of_action_names:
        print(f"processing action: ", action_name)
        prompt = f"point to the button or dial that can achieve this action: {action_name}. If this action requires two buttons or dials, please point to both of them. "
        response = chat(prompt, image)
        #print("response: ", response)
        
        points = extract_points_from_response(response)
        
        if points:
            image_with_point = draw_point_on_image(image.copy(), points)
            output_visualisation_filepath = os.path.join(output_visualisation_dir, f"{action_name}.png")
            create_or_replace_path(output_visualisation_filepath)
            image_with_point.save(output_visualisation_filepath)
        else:
            print(f"No point found in response for action '{action_name}'.")
        
        prompt = f"Please reply in text of the type of this action: {action_name}, choose from one of the following: turn_dial_clockwise, turn_dial_anti_clockwise, press_button, press_and_hold_button. Respond in lower case."
        response = chat(prompt, image)
        #print("response: ", response)
        response = response.lower().strip()
        grounding_dict["actions"][action_name] = {"coord":points, "action_type": response}
        #exit()

    # save the grounding dict to a json file
    grounding_dict_filepath = os.path.join(output_action_coords_filepath)
    create_or_replace_path(grounding_dict_filepath)
    with open(grounding_dict_filepath, "w") as f:
        json.dump(grounding_dict, f, indent=4)
    


        # checking criteria: just check whether each proposed coord can map to any grounded coord. needs the action type also 

    # action name proposal is done by RAG, which cannot be generated in one shot. 
    # effect of grounding action names: 
    # given a list of proposed action names by gpt, 
    # list of 
    pass 

def batch_map_molmo_to_oracle_action(input_action_option_dir, oracle_action_dir, output_molmo_to_oracle_action_dir):
    input_action_machine_types = os.listdir(input_action_option_dir)
    for input_action_machine_type in input_action_machine_types:
        # list all files ends with txt
        input_action_machine_ids = [f for f in os.listdir(os.path.join(input_action_option_dir, input_action_machine_type)) if f.endswith(".json")]
        for input_action_machine_id in input_action_machine_ids:
            print(f"processing {input_action_machine_type}/{input_action_machine_id}", )
            machine_id = input_action_machine_id.split(".")[0]
            input_action_option_filepath = os.path.join(input_action_option_dir, input_action_machine_type, input_action_machine_id)
            oracle_action_filepath = os.path.join(oracle_action_dir, input_action_machine_type, machine_id + ".json")
            output_molmo_to_oracle_action_filepath = os.path.join(output_molmo_to_oracle_action_dir, input_action_machine_type, machine_id + ".json")
            create_or_replace_path(output_molmo_to_oracle_action_filepath)
            map_molmo_to_oracle_action(input_action_option_filepath, oracle_action_filepath, output_molmo_to_oracle_action_filepath)
    pass

def is_center_inside(point, bbox2):
    # Calculate the center of bbox1
    center_x, center_y = point
    center_x = round(center_x/100 ,4)
    center_y = round(center_y /100,4)
    
    # Check if the center of bbox1 is inside bbox2
    if (bbox2[0] <= center_x <= bbox2[2]) and (bbox2[1] <= center_y <= bbox2[3]):
        return True
    else:
        return False

def check_is_center_inside(proposed_point_list, oracle_bbox_list):
    """
    Check if each bbox in proposed_bbox_list has an IoU > threshold with at least one bbox in oracle_bbox_list.
    """
    if len(proposed_point_list) != len(oracle_bbox_list):
        return False
    for proposed_point in proposed_point_list:
        # Track if the current proposed bbox meets the IoU condition with any oracle bbox
        criteria_met = False
        for oracle_bbox in oracle_bbox_list:
            criteria_met = is_center_inside(proposed_point, oracle_bbox)
            if criteria_met:
                break #Stop checking further if one meets the threshold
        if not criteria_met:
            # If any proposed bbox does not meet the condition, return False immediately
            return False
    
    return True

def formalise_action_type(action_type):
    if "press" in action_type and "hold" not in action_type:
        return "press_button"
    elif "hold" in action_type:
        return "press_and_hold_button"
    elif "clockwise" in action_type and "anti" not in action_type:
        return "turn_dial_clockwise"
    elif "anti" in action_type:
        return "turn_dial_anti_clockwise"
    else:
        return ""
def map_molmo_to_oracle_action(molmo_coord_filepath, oracle_action_filepath, output_molmo_to_oracle_action_filepath):
    molmo_coords_data = json.load(open(molmo_coord_filepath, "r"))
    oracle_coords_data = json.load(open(oracle_action_filepath, "r"))
    molmo_image_name = molmo_coords_data["image_name"]
    molmo_actions = molmo_coords_data["actions"]
    molmo_to_oracle_action_mapping_dict = {}

    for molmo_action_name in molmo_actions.keys():
        print(f"processing action: ", molmo_action_name)
        molmo_to_oracle_action_mapping_dict[molmo_action_name] = []
        molmo_coord = molmo_actions[molmo_action_name]["coord"]
        action_type = molmo_actions[molmo_action_name]["action_type"]
        proposed_action_type = formalise_action_type(action_type)
        for oracle_action in oracle_coords_data:
            oracle_coords = oracle_action["bboxes"]
            oracle_action_name = oracle_action["action"]
            oracle_action_type = oracle_action["action_type"]
            target_oracle_coord = None 
            for oracle_coord in oracle_coords:
                # check if the two coords are similar
                if oracle_coord["image_name"] == molmo_image_name:
                    target_oracle_coord = oracle_coord["bbox"]
                    break 
            #print("molmo_coord: ", molmo_coord)
            #print("target_oracle_coord: ", target_oracle_coord)
            is_inside = check_is_center_inside(molmo_coord, target_oracle_coord)#False # check target_oracle_coord (list of bbox) and molmo_coord (list of points), 
            if is_inside and oracle_action_type == proposed_action_type:
                molmo_to_oracle_action_mapping_dict[molmo_action_name] = [oracle_action_name]
    # save the mapping dict to a json file
    with open(output_molmo_to_oracle_action_filepath, "w") as f:
        json.dump(molmo_to_oracle_action_mapping_dict, f, indent=4)
    pass 

if __name__ == "__main__":
    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 

    def test():
        image = Image.open("4_0.jpeg")
        prompt = "point to the express button and the power button"
        response = chat(prompt, image)
        print(response)
        
        point = extract_points_from_response(response)
        print(point)
        if point:
            image_with_point = draw_point_on_image(image, point)
            image_with_point.save("4_0_with_point.png")
            print("Saved image with point as 4_0_with_point.png")
        else:
            print("No point found in response.")
   
    input_action_option_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_4_visual_grounding/gpt-4o-2024-11-20/_1_action_names/_1_proposed_action_names")
    molmo_proposed_action_coords_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_4_visual_grounding/gpt-4o-2024-11-20/_1_action_names/_4_molmo_proposed_action_coords")
    
    input_image_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_2_control_panel_images/_1_selected")
    output_visualisation_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_4_visual_grounding/gpt-4o-2024-11-20/_1_action_names/_5_molmo_proposed_actions_visualisation")
    #batch_test_visual_grounding_for_one_appliance(input_action_option_dir, input_image_dir, molmo_proposed_action_coords_dir, output_visualisation_dir)

    oracle_action_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_3_simulators/_3_oracle_simulator_action_to_bbox_mapping")
    output_molmo_to_oracle_action_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_4_visual_grounding/gpt-4o-2024-11-20/_1_action_names/_6_molmo_proposed_to_oracle_action_mapping")
    
    #batch_map_molmo_to_oracle_action(molmo_proposed_action_coords_dir, oracle_action_dir, output_molmo_to_oracle_action_dir)

    visual_grounding_action_score_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_1_visual_grounding_action_results/molmo")
    batch_evaluate_visual_grounding_action_result(oracle_action_dir, output_molmo_to_oracle_action_dir, visual_grounding_action_score_dir)


    


