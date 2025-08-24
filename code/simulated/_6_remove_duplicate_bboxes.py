# import file is the formatted json file
# sample: 
import json
import _0_t2a_config

from foundation_models.owlv2_crane5_query import visualize_image
from foundation_models.gpt_4o_model import GPT4O
from foundation_models.claude_sonnet_model import ClaudeSonnet
from utils.create_or_replace_path import create_or_replace_path
from _3_detect_bbox_from_photos import  group_boxes_within_distance, get_union_bbox, crop_image_to_focus_on_bbox
from utils.extract_python_code import extract_python_code
from utils.load_string_from_file import load_string_from_file
from PIL import Image
import time
import os
import copy

user_manual_prompt = """

Attached is the user manual of a particular xxxxx.

zzzzz

"""
task_prompt = """

The appliance of type xxxxx has an control element called yyyyy. Control panel elements are responsible for the operation and feedback of the appliance's control panel. Examples include buttons, dials, soft pads, switches and digital displays. We ignore indicators.

I will firstly input a photo of the appliance. The sequential set of images will display some bounding box options that circles out this element: yyyyy. Please select one and only one bounding box that best fits this element. Each bounding box has an index on its right bottom corner. If none of the bounding boxes fit the element, please return -1. 

Please firstly review the photo of the appliance to identify the control element: yyyyy. If it is a dial, identify its knob. If it is a button, identify the pressing area. If there is no visible button or dial related to this element, just label, even it appears to be not interactive, identify it as a soft pad.

The choosing criteria is as follows:
1. Dial Selection Criteria: Choose the bounding box that primarily covers the dial knob. Ignore bounding boxes that only encompass the labeling around the dial.

2. Button Selection Criteria: 
    a) Label on the Button: The bounding box may select either the label or the entire physical button, as both are valid. Even if it only captures a partial section of the button or the label, as long as the circled area falls in to the button region or label region. 
    
    b) Label Outside the Button: For physical buttons, if the button is extruded from the surface, select the bounding box that encompasses the extruded area. Bounding boxes that only include the label area (without capturing the physical button) are considered invalid. For soft pads, prioritize bounding boxes that selects the  symbols and icons first. If these are not available, then select the labels.

3. Soft Pad Selection criteria: The label text is the execution area. Choose a bounding box that includes any part of the label text. Any bounding boxes that partially or fully capture the text are valid.

Please return a python variable called response_index that contains the bounding box index as a digit without anything else. For example, if you choose the bounding box with index 3, just return response_index = 3. If none of the proposed bounding boxes fit the criteria, please return response_index = -1.

Then in the next line, briefly explain your reason, and store it in response_reason as strings. If the response_index is -1, describe the visual attributes of the area that you think should be circled.



"""

def make_query_images(image_path, data, query_image_root_dir):
    # load image 
    raw_image = Image.open(image_path)
    
    bbox_group = group_boxes_within_distance(data, distance_threshold=0.3)
    
    query_images = []
    
    for i, group in enumerate(bbox_group):

        annotated_image = visualize_image(raw_image, bboxes = [obj["bbox"] for obj in group], return_img=True, labels=[obj["id"] for obj in group], show=False, rect_color="red", alpha=1)

        # crop the image to focus on the bbox
        union_bbox = get_union_bbox(group)
        cropped_image, cropped_coord = crop_image_to_focus_on_bbox(annotated_image, union_bbox, 5)
        query_image_save_path = os.path.join(query_image_root_dir, f"{i}.png")
        create_or_replace_path(query_image_save_path)
        cropped_image.save(query_image_save_path)
        query_images.append(query_image_save_path)
    return query_images

def resolve_duplicate_bbox_id_for_all_appliances(input_json_root_dir, output_json_root_dir, raw_image_root_dir, query_image_save_root_dir, bbox_input_root_dir, user_manual_dir, gpt_model_type):
    # list all dir in input_json_root_dir
    machine_types = [os.path.join(input_json_root_dir, d) for d in os.listdir(input_json_root_dir)]
    # iterate through each dir
    for machine_type in machine_types:
        machine_type_name = machine_type.split("/")[-1]
        # list all files in the dir
        json_files = [os.path.join(machine_type, f) for f in os.listdir(machine_type)]
        json_files.sort()
        # iterate through each file
        for input_json_filepath in json_files:
            if not any(substring in input_json_filepath for substring in ["_5_induction_cooker/1"]):
                continue
            machine_id = input_json_filepath.split("/")[-1].split(".")[0]
            print(f"processing {machine_type_name} {machine_id}")
            output_json_filepath = os.path.join(output_json_root_dir, machine_type_name, f"{machine_id}.json")
            user_manual_filepath = os.path.join(user_manual_dir, machine_type_name, f"_{machine_id}.txt")
            raw_image_machine_type_dir = os.path.join(raw_image_root_dir, machine_type_name)
            query_image_save_machine_instance_dir = os.path.join(query_image_save_root_dir, machine_type_name, machine_id)
            bbox_input_machine_instance_dir = os.path.join(bbox_input_root_dir, machine_type_name, machine_id)
            # select the file that starts with the machine_id
            raw_image_filepath = os.path.join(raw_image_machine_type_dir, [f for f in os.listdir(raw_image_machine_type_dir) if f.split("_")[0] == machine_id][0])
            resolve_duplicate_bbox_id_for_one_instance(input_json_filepath, output_json_filepath, raw_image_filepath, query_image_save_machine_instance_dir, machine_type_name, bbox_input_machine_instance_dir, user_manual_filepath, task_prompt, user_manual_prompt, gpt_model_type, model_type="gpt")

def resolve_duplicate_bbox_id_for_one_instance(input_json_filepath, output_json_filepath, raw_image_filepath, query_image_save_filepath, machine_type, bbox_input_root_dir, user_manual_filepath, task_prompt, user_manual_prompt, gpt_model_type, model_type="gpt"):
    if len(machine_type.split("_")) >= 2 and machine_type.split("_")[0].isdigit():
        machine_type = " ".join(machine_type.split("_")[1:])
    with open(input_json_filepath, "r") as f:
        element_list = json.load(f)
    user_manual_text = load_string_from_file(user_manual_filepath)
    output_list = []
    for element_dict in element_list:
        output_dict = dict()
        element_name = element_dict["element_name"]
        #if element_name!="power_button":
        #    continue
        output_dict["element_name"] = element_name
        output_dict["bboxes"] = []
        bboxes = element_dict["bboxes"]
        print(f"processing {element_name}")
        # for each image, 
        """
        [
            {
                "element_name": "power_selector_dial",
                "bboxes": [
                    {"image_name": "0_1", "bbox_id": [0, 5]}
                ]
            },
            {
                "element_name": "timer_selector_dial",
                "bboxes": [
                    {"image_name": "0_1", "bbox_id": [1, 2, 3, 4]}
                ]
            }
        ]
        """

        for bbox_dict in bboxes:
            image_name = bbox_dict["image_name"]
            if len(image_name.split("_")) == 2:
                machine_id = image_name.split("_")[0]
                pic_id = image_name.split("_")[1]
            else:
                machine_id = ""
                pic_id = image_name
            bbox_ids = bbox_dict["bbox_id"]
            
            

            query_image_folder_of_a_control_element = os.path.join(query_image_save_filepath, element_name.replace(" ", "_").replace("/", "_"))

            query_image_folder_of_a_control_element_and_a_pic = os.path.join(query_image_folder_of_a_control_element, pic_id)

            create_or_replace_path(query_image_folder_of_a_control_element_and_a_pic)
            bbox_data = []

            # if bbox_input_root_dir is a folder:
            if os.path.isdir(bbox_input_root_dir):
                bbox_savepath = os.path.join(bbox_input_root_dir, f"{pic_id}.json")
            # if bbox_input_root_dir is a file:
            elif os.path.isfile(bbox_input_root_dir):
                bbox_savepath = bbox_input_root_dir

            # load bboxes from json file
            with open(bbox_savepath, 'r') as json_file:
                bbox_data = json.load(json_file)
            bbox_data = [bbox for bbox in bbox_data if bbox["id"] in bbox_ids]

            """
            raw_image_filename = [f for f in os.listdir(raw_image_root_dir) if f.split(".")[0] ==image_name][0]

            raw_image_filepath = os.path.join(raw_image_root_dir, raw_image_filename)
            """
            # list all files and find the one that matches the image name
            query_image_filepaths = make_query_images(raw_image_filepath, bbox_data, query_image_folder_of_a_control_element_and_a_pic)

            # ask claude to pick one single bbox id from the query images
            # the returned response must be a single digit, or else, should just be empty 

            satisfied = False 
            times = 0 
            my_prompt = task_prompt.replace("xxxxx", machine_type).replace("yyyyy", element_name)
            context_prompt = user_manual_prompt.replace("xxxxx", machine_type).replace("zzzzz", user_manual_text) + "\n" + my_prompt
            error_msg = ""
            #print(my_prompt)
            #exit()
            while not satisfied and times < 1:

                if model_type == "gpt":
                    model = GPT4O()
                    response = model.chat_with_multiple_images(my_prompt + "\n" + error_msg, [raw_image_filepath] + query_image_filepaths, gpt_model_type, temperature = 1, top_p = 1)
                    
                elif model_type == "claude":
                    model = ClaudeSonnet()
                    response = model.chat_with_multiple_images([raw_image_filepath] + query_image_filepaths, my_prompt ) 
                response = extract_python_code(response)
                print("response", response)
                current_namespace = {}
                try:
                    exec(response, current_namespace)
                    response_index = current_namespace["response_index"]
                    response_reason = current_namespace["response_reason"]
                    
                    # response_index should be type digit
                    satisfied = isinstance(response_index, int)
                    times +=1 
                    break
                    del model 
                except Exception as e:
                    error_msg = f"In you previous attempt, the error message is {e}. Please try again and avoid the error."

                
            
            if satisfied and int(response_index) != -1:
                output_dict["bboxes"].append({"image_name": image_name, "bbox_id": [int(response_index)], "reason": response_reason})

            elif satisfied and int(response_index) == -1:
                # add user manual and try again 
                satisfied = False
                times = 0
                while not satisfied and times < 3:
                    model = GPT4O()
                    response = model.chat_with_multiple_images(context_prompt, [raw_image_filepath] + query_image_filepaths, gpt_model_type)
                    response = extract_python_code(response)
                    times += 1
                    print("response", response)
                    try: 
                        exec(response, current_namespace)
                        response_index = current_namespace["response_index"]
                        response_reason = current_namespace["response_reason"]
                        satisfied = isinstance(response_index, int)
                        break
                    except Exception as e:
                        error_msg = f"In you previous attempt, the error message is {e}. Please try again and avoid the error."
                        continue
                if int(response_index) != -1:
                    output_dict["bboxes"].append({"image_name": image_name, "bbox_id": [int(response_index)], "reason": response_reason})
                else:
                    output_dict["bboxes"].append({"image_name": image_name, "bbox_id": [], "reason": response_reason})
               
                # ask to select one and only option, and output the result in visual_grounding/_2_control_panel_element_index_unique
                pass
        # save the result dict to output_list
        output_list.append(output_dict)
    # save the output_list to output_json_filepath
    create_or_replace_path(output_json_filepath)
    with open(output_json_filepath, "w") as f:
        json.dump(output_list, f, indent=4)

   





# 
if __name__ == "__main__":
    
    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Ground Entities for one appliance. For each name and multiple bbox, choose the best bbox
    #
    #######################################
    machine_type = "_6_coffee_machine"
    machine_id = "0"
    input_json_filepath = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/_1_control_panel_element_index_json/{machine_type}/{machine_id}.json')
    output_json_filepath = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/_2_control_panel_element_index_json_unique/{machine_type}/{machine_id}.json')
    raw_image_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_1_selected/{machine_type}')
    query_image_save_filepath = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_6_query_images_unique_bbox_id/{machine_type}/{machine_id}')
    user_manual_filepath = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text/{machine_type}/_{machine_id}.txt')
    bbox_input_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_3_bboxes_on_control_panel/{machine_type}/{machine_id}')
    #resolve_duplicate_bbox_id_for_one_instance(input_json_filepath, output_json_filepath, raw_image_root_dir, query_image_save_filepath, machine_type, bbox_input_root_dir, user_manual_filepath)

    #######################################
    #
    # Ground Entities for all appliances. For each name and multiple bbox, choose the best bbox
    #
    #######################################
    gpt_model_type = "gpt-4o-2024-11-20"

    input_json_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_1_control_panel_element_index_json')
    output_json_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_2_control_panel_element_index_json_unique')
    raw_image_root_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_2_control_panel_images/_1_selected')
    query_image_save_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_2_ground_control_panel_elements/{gpt_model_type}/_5_query_images_unique_bbox_id')
    bbox_input_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_2_ground_control_panel_elements/{gpt_model_type}/_2_bboxes_on_control_panel')
    user_manual_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text')
    resolve_duplicate_bbox_id_for_all_appliances(input_json_root_dir, output_json_root_dir, raw_image_root_dir, query_image_save_root_dir, bbox_input_root_dir, user_manual_dir, gpt_model_type)
