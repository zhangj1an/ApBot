# visualie the button at the raw images 
import sys
import os 
sys.path.append(os.path.expanduser("~/RLS_microwave/utils")) 

from foundation_models.owlv2_crane5_query import OWLViT, visualize_image


import os 
import _0_t2a_config
from utils.create_or_replace_path import create_or_replace_path
import json
from PIL import Image
from foundation_models.owlv2_crane5_query import  visualize_image




def visualise_entities(grounded_element_bboxes_filepath, control_panel_image_path, output_savepath):
    # specific to each machine instance 

    # load the oracle actions
    with open(grounded_element_bboxes_filepath, "r") as f:
        proposed_entities = json.load(f)
    
    # iterate over the images 
    # data structure:
    # { "bbox": [x1, y1, x2, y2], 
    #   "label": "action_name + action_name"
    # }

    # list all files in the control panel image dir
    #image_files = [f for f in os.listdir(control_panel_image_machine_type_dir) if f.endswith((".jpg", ".jpeg", ".png"))]
    #image_files = [f for f in image_files if f.startswith(machine_id)]

    #for image_file in image_files:

    #image_name = image_file.split(".")[0]

    #image_path = os.path.join(control_panel_image_machine_type_dir, image_file)
    image = Image.open(control_panel_image_path)
    

    bbox_list = []
    labels_list = []
    for proposed_entity in proposed_entities:
        #print("proposed_entity: ", proposed_entity)
        bboxes = proposed_entity["grounded_bboxes"]
        element_name = proposed_entity["element_name"]
        #action_name = proposed_entity["action"]
        for item in bboxes:
            #if item["image_name"] == image_name:
            bbox_list.append(item["bbox"])
            labels_list.append(element_name)
    annotated_image = visualize_image(image, bboxes = bbox_list, labels = labels_list, show=False, return_img= True, rect_color="green", text_color="green", alpha=0.5)
    print(f"finish {control_panel_image_path}")
                        
    if len(bbox_list) != 0:
        #output_savepath = os.path.join(visualisation_output_machine_type_dir,machine_id, image_file.split(".")[0] +  "." + image_file.split(".")[1])
        create_or_replace_path(output_savepath)
        print("output_savepath: ", output_savepath)
        annotated_image.convert('RGB').save(output_savepath)

    """
    example oracle file: a list of items below:
    {
        "action": "turn_power_selector_dial_clockwise",
        "bbox_label": [
            "0_power_dial"
        ],
        "action_type": "turn_dial_clockwise",
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
    #exit()

def batch_visualise_elements(grounded_element_bboxes_dir, control_panel_images_dir, visualisation_output_dir):
    machine_type_list = [f for f in os.listdir(grounded_element_bboxes_dir) if os.path.isdir(os.path.join(grounded_element_bboxes_dir, f))]
    for machine_type in machine_type_list:
        machine_id_files = [f for f in os.listdir(os.path.join(grounded_element_bboxes_dir, machine_type)) if f.endswith(".json")]
        for machine_id_file in machine_id_files:
            machine_id = machine_id_file.split(".")[0]
            grounded_element_bboxes_filepath = os.path.join(grounded_element_bboxes_dir, machine_type, machine_id + ".json")
            control_panel_image_machine_type_dir = os.path.join(control_panel_images_dir, machine_type)
            visualisation_output_machine_type_dir = os.path.join(visualisation_output_dir, machine_type)
            visualise_entities(grounded_element_bboxes_filepath, control_panel_image_machine_type_dir, visualisation_output_machine_type_dir, machine_id)

if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # visualise grounded entities.
    #
    #######################################

    grounded_element_bboxes_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_3_proposed_control_panel_element_bbox')

    visualisation_output_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_8_visualised_proposed_control_panel_element_bbox')

    control_panel_images_dir = os.path.expanduser("~/TextToActions/dataset/simulated/_2_control_panel_images/_1_selected")
    #batch_visualise_elements(grounded_element_bboxes_dir, control_panel_images_dir, visualisation_output_dir)

    #######################################
    #
    # visualise grounded entities for one appliance
    #
    #######################################
    machine_type = "_2_washing_machine"
    machine_id = "3"

    grounded_element_bboxes_filepath = os.path.expanduser(f'~/TextToActions/dataset/simulated/_4_visual_grounding/_3_proposed_control_panel_element_bbox/{machine_type}/{machine_id}.json')

    control_panel_image_machine_type_dir = os.path.expanduser(f"~/TextToActions/dataset/simulated/_2_control_panel_images/_1_selected/{machine_type}")
    
    visualisation_output_machine_type_dir = os.path.expanduser(f'~/TextToActions/dataset/simulated/_4_visual_grounding/_8_visualised_proposed_control_panel_element_bbox/{machine_type}')

    
    visualise_entities(grounded_element_bboxes_filepath, control_panel_image_machine_type_dir, visualisation_output_machine_type_dir, machine_id)

    