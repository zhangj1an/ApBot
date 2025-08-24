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
from utils.task.visualize_image import visualize_bboxes_with_legend

def visualise_entities(grounded_element_bboxes_filepath, control_panel_image_machine_type_dir, visualisation_image_output_machine_type_dir,  visualisation_legend_output_machine_type_dir, machine_id, setting):
    # setting can be with_label or no_label
    # load the oracle actions
    with open(grounded_element_bboxes_filepath, "r") as f:
        proposed_entities = json.load(f)
    
    # iterate over the images 
    # data structure:
    # { "bbox": [x1, y1, x2, y2], 
    #   "label": "action_name + action_name"
    # }

    # list all files in the control panel image dir
    image_files = [f for f in os.listdir(control_panel_image_machine_type_dir) if f.endswith((".jpg", ".jpeg", ".png"))]
    image_files = [f for f in image_files if f.startswith(machine_id)]

    for image_file in image_files:
        annotation_info = []
        image_name = image_file.split(".")[0]
        
        for proposed_entity in proposed_entities:
            bboxes = proposed_entity["grounded_bboxes"]
            element_name = proposed_entity["element_name"]
            
            for item in bboxes:
                if item["image_name"] == image_name:
                    bbox = item["bbox"]

                    annotation_info.append({"bbox": bbox, "label": element_name})
        
        # Define paths
        image_path = os.path.join(control_panel_image_machine_type_dir, image_file)
        output_image_savepath = os.path.join(visualisation_image_output_machine_type_dir, 
        machine_id, f"{image_name}.jpg")
        output_label_savepath = os.path.join(visualisation_legend_output_machine_type_dir,
        machine_id, f"{image_name}.json") 

        os.makedirs(os.path.dirname(output_image_savepath), exist_ok=True)
        os.makedirs(os.path.dirname(output_label_savepath), exist_ok=True)
        
        # Visualize entities with legend
        if annotation_info:
            image = Image.open(image_path)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            image.save(os.path.join(visualisation_image_output_machine_type_dir, 
        machine_id, f"original.jpg"))
            visualize_bboxes_with_legend(image_path, annotation_info, output_image_savepath, output_label_savepath, setting)
            print(f"Saved visualization{output_image_savepath}")

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

def batch_visualise_elements(grounded_element_bboxes_dir, control_panel_images_dir, visualisation_image_output_dir, visualisation_legend_output_dir, setting = "with_label"):
    machine_type_list = [f for f in os.listdir(grounded_element_bboxes_dir) if os.path.isdir(os.path.join(grounded_element_bboxes_dir, f))]
    for machine_type in machine_type_list:
        machine_id_files = [f for f in os.listdir(os.path.join(grounded_element_bboxes_dir, machine_type)) if f.endswith(".json")]
        for machine_id_file in machine_id_files:
            machine_id = machine_id_file.split(".")[0]
            #if not ("microwave_oven" in machine_type and "1" in machine_id):
            #    continue
            if not any(s in f"{machine_type}/{machine_id}" for s in ["_5_induction_cooker/1"]):
                continue
            grounded_element_bboxes_filepath = os.path.join(grounded_element_bboxes_dir, machine_type, machine_id + ".json")
            control_panel_image_machine_type_dir = os.path.join(control_panel_images_dir, machine_type)
            visualisation_image_output_machine_type_dir = os.path.join(visualisation_image_output_dir, machine_type)
            visualisation_legend_output_machine_type_dir = os.path.join(visualisation_legend_output_dir, machine_type)
            visualise_entities(grounded_element_bboxes_filepath, control_panel_image_machine_type_dir, visualisation_image_output_machine_type_dir, visualisation_legend_output_machine_type_dir, machine_id, setting)
            #exit()
            

if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 
    #######################################
    #
    # visualise grounded entities for testing baseline: M_UR_LP_NV.
    # the generated image should only have index, bounding box and action type. 
    #
    #######################################
    gpt_model_type = "gpt-4o-2024-11-20"
    control_panel_images_dir = os.path.expanduser("~/TextToActions/datasetv2/real_world/_2_control_panel_images/_1_selected")

    grounded_element_bboxes_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_3_proposed_control_panel_element_bbox')

    visualisation_image_with_label_output_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_4_visualised_proposed_control_panel_element_bbox')

    visualisation_image_no_label_output_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_5_visualised_localised_buttons_no_label')

    visualisation_legend_output_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_6_visualised_localised_buttons_legends')

    control_panel_images_dir = os.path.expanduser("~/TextToActions/datasetv2/real_world/_2_control_panel_images/_1_selected")

    # pure for visualisation
    #batch_visualise_elements(grounded_element_bboxes_dir, control_panel_images_dir, visualisation_image_with_label_output_dir,visualisation_legend_output_dir, setting = "with_label")

    # for baseline, CoT input 
    batch_visualise_elements(grounded_element_bboxes_dir, control_panel_images_dir, visualisation_image_no_label_output_dir,visualisation_legend_output_dir, setting = "no_label")

    #######################################
    #
    # visualise grounded entities for one appliance
    #
    #######################################
    machine_type = "_1_microwave"
    machine_id = "4"

    # concatenate with grounded_element_bboxes_dir
    grounded_element_bboxes_filepath = os.path.join(grounded_element_bboxes_dir, machine_type, f"{machine_id}.json")

    control_panel_image_machine_type_dir = os.path.join(control_panel_images_dir, machine_type)

    visualisation_image_with_label_output_machine_type_dir = os.path.join(visualisation_image_with_label_output_dir, machine_type)

    visualisation_image_no_label_output_machine_type_dir = os.path.join(visualisation_image_no_label_output_dir, machine_type)

    visualisation_legend_output_machine_type_dir = os.path.join(visualisation_legend_output_dir, machine_type)
    
    # pure for visulisation, image contains labels
    #visualise_entities(grounded_element_bboxes_filepath, control_panel_image_machine_type_dir, visualisation_image_with_label_output_machine_type_dir, visualisation_legend_output_machine_type_dir, machine_id, setting = "with_label")

    # for baseline, CoT input, image with no labels
    #visualise_entities(grounded_element_bboxes_filepath, control_panel_image_machine_type_dir, visualisation_image_no_label_output_machine_type_dir, visualisation_legend_output_machine_type_dir, machine_id, setting = "with_label")

    