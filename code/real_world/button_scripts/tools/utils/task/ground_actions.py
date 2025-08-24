import os 
import sys
import shutil 
from tools._1_pdf_to_text import convert_pdf_to_images, run_gpt_4o 
from tools._2_extract_control_panel_element_names_from_user_manual import extract_control_panel_elements
from tools._3_detect_bbox_from_photos import process_image, make_query_images
from tools._4_map_control_panel_element_names_to_bbox_indexes import ground_proposed_entities_in_batch, task_prompt as prompt_identify_control_panel_element_index
from tools._5_json_map_control_panel_element_names_to_bbox_indexes import consolidate_mapping_results_simple, meta_prompt as prompt_format_control_panel_element_index
from tools._6_remove_duplicate_bboxes import resolve_duplicate_bbox_id_for_one_instance, user_manual_prompt as remove_duplicate_bboxes_user_manual_prompt, task_prompt as remove_duplicate_bboxes_task_prompt
from tools._7_json_map_control_panel_element_names_to_bbox import map_element_to_bboxes as map_control_panel_element_names_to_bbox
from tools._8_visualise_grounding_control_element_name_result import visualise_entities as visualise_grounded_control_panel_elements
from tools._10_propose_action_names import define_action_names
from tools._11_generated_grounded_action_json import prompt as prompt_map_actions_to_entities, generate_grounded_actions_for_proposed_world_model
# do all the things in one file 

from tools._13_visualisation_grounding_action_result import visualise_actions_in_single_image 


def process_input_files(parameter_dict):
    user_manual_pdf_filepath = os.path.join(parameter_dict["data_output_root_dir"], "_1_user_manual/_0_pdf.pdf") 
    control_panel_image_filepath = os.path.join(parameter_dict["data_output_root_dir"], f"_2_control_panel_images/_0_raw/0.png")
    # Ensure output directories exist
    os.makedirs(os.path.dirname(user_manual_pdf_filepath), exist_ok=True)
    os.makedirs(os.path.dirname(control_panel_image_filepath), exist_ok=True)

    # Scan _0_input directory
    pdf_file = None
    png_file = None
    input_dir = parameter_dict["data_input_root_dir"]
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_file = filename
        elif filename.lower().endswith(".png"):
            png_file = filename

    # Move files to their destinations
    if pdf_file:
        shutil.move(os.path.join(input_dir, pdf_file), user_manual_pdf_filepath)

    if png_file:
        shutil.move(os.path.join(input_dir, png_file), control_panel_image_filepath)

def prepare_directories(root_dir, appliance_type, control_panel_image_index):
    
    data_output_root_dir = os.path.join(root_dir, "data", appliance_type, f"output_{control_panel_image_index}")
    data_input_root_dir = os.path.join(root_dir, "data", appliance_type, "_0_input")

    prompt_root_dir = os.path.join(root_dir, "tools/prompts")
    parameter_dict = {
        "root_dir": root_dir,
        "data_output_root_dir": data_output_root_dir,
        "data_input_root_dir": data_input_root_dir,
        "appliance_type": appliance_type,
        "control_panel_image_index": control_panel_image_index,
        "user_manual_pdf_filepath": os.path.join(data_output_root_dir, "_1_user_manual/_0_pdf.pdf"),
        "user_manual_image_folder_path": os.path.join(data_output_root_dir, "_1_user_manual/_1_images"),
        "user_manual_text_filepath": os.path.join(data_output_root_dir, "_1_user_manual/_2_text.txt"),
        "prompt_propose_control_panel_element_filepath": os.path.join(prompt_root_dir, "_2_extract_control_panel_element.txt"),
        "prompt_filter_control_panel_element_filepath": os.path.join(prompt_root_dir, "_2_filter_control_panel_element.txt"),
        "panel_elements_from_user_manual_filepath": os.path.join(data_output_root_dir, "_1_user_manual/_3_extracted_control_panel_element_names.py"),
        "control_panel_image_filepath": os.path.join(data_output_root_dir, f"_2_control_panel_images/_0_raw/{control_panel_image_index}.png"),
        "bboxes_on_control_panel_filepath": os.path.join(data_output_root_dir, "_2_control_panel_images/_1_ground_control_panel_elements/_2_bboxes_on_control_panel.json"),
        "validity_control_panel_folder": os.path.join(data_output_root_dir, "_2_control_panel_images/_1_ground_control_panel_elements/_1_validity_control_panel"),
        "bboxes_on_control_panel_visualisation_filepath": os.path.join(data_output_root_dir, "_2_control_panel_images/_1_ground_control_panel_elements/_3_bboxes_on_control_panel_visualisation.png"),
        "query_image_to_match_bbox_to_control_element_names_folder": os.path.join(data_output_root_dir, "_2_control_panel_images/_1_ground_control_panel_elements/_4_query_images_bbox_to_name"),
        "propose_action_prompt_filepath": os.path.join(prompt_root_dir, "_10_create_action_names.txt"),
        "filter_action_prompt_filepath": os.path.join(prompt_root_dir, "_10_filter_action_names.txt"),
        "proposed_actions_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_1_action_names/_1_proposed_action_names.txt"),
        "map_bbox_index_to_control_panel_element_name_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_0_control_panel_element_bbox/_0_control_panel_element_index.txt"),
        "map_bbox_index_to_control_panel_element_name_json_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_0_control_panel_element_bbox/_1_control_panel_element_index.json"),
        "map_bbox_index_to_control_panel_unique_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_0_control_panel_element_bbox/_2_control_panel_element_index_unique.json"),
        "query_images_to_match_control_element_names_to_unique_bbox_id_folder": os.path.join(data_output_root_dir, "_2_control_panel_images/_1_ground_control_panel_elements/_5_query_images_unique_bbox_id"),
        "proposed_control_element_bbox_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_0_control_panel_element_bbox/_3_proposed_control_panel_element_bbox.json"),
        "visualised_proposed_control_panel_element_bbox_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_0_control_panel_element_bbox/_4_visualised_proposed_control_panel_element_bbox.png"),
        "proposed_actions_bbox_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_1_action_names/_2_proposed_action_bbox.json"),
        "visualised_proposed_actions_filepath": os.path.join(data_output_root_dir, "_3_visual_grounding/_1_action_names/_3_visualised_proposed_actions.png"),
       
    }
    return parameter_dict 

def extract_control_panel_element_names(parameter_dict):

    print("Converting user manual pdf to images")
    convert_pdf_to_images(parameter_dict["user_manual_pdf_filepath"], parameter_dict["user_manual_image_folder_path"])
    print("results saved in ", parameter_dict["user_manual_image_folder_path"], "\n")
    
    # run gpt-4o to extract text from user manual images
    print("Running GPT-4o to extract text from user manual images")
    run_gpt_4o(parameter_dict["user_manual_image_folder_path"], parameter_dict["user_manual_text_filepath"])
    print("results saved in ", parameter_dict["user_manual_text_filepath"], "\n")

    print("Extracting control panel elements from user manual")
    extract_control_panel_elements(parameter_dict["user_manual_text_filepath"], parameter_dict["panel_elements_from_user_manual_filepath"], parameter_dict["prompt_propose_control_panel_element_filepath"], parameter_dict["prompt_filter_control_panel_element_filepath"], parameter_dict["control_panel_image_filepath"])
    print("results saved in ", parameter_dict["panel_elements_from_user_manual_filepath"], "\n")
    
    pass


def ground_action_names(parameter_dict):

    print("Defining action names")
    define_action_names(parameter_dict["user_manual_text_filepath"], parameter_dict["proposed_control_element_bbox_filepath"], parameter_dict["propose_action_prompt_filepath"], parameter_dict["filter_action_prompt_filepath"], parameter_dict["proposed_actions_filepath"])
    print("results saved in ", parameter_dict["proposed_actions_filepath"], "\n")

    print("grounding action names to bboxes")
    generate_grounded_actions_for_proposed_world_model(prompt_map_actions_to_entities, parameter_dict["proposed_actions_filepath"], parameter_dict["proposed_control_element_bbox_filepath"], parameter_dict["proposed_actions_bbox_filepath"])
    print("results saved in ", parameter_dict["proposed_actions_bbox_filepath"], "\n")
    

    print("visualise grounded actions")
    visualise_actions_in_single_image(parameter_dict["proposed_actions_bbox_filepath"], parameter_dict["control_panel_image_filepath"], parameter_dict["visualised_proposed_actions_filepath"], "")
    print("results saved in ", parameter_dict["visualised_proposed_actions_filepath"], "\n")




def ground_control_panel_elements(parameter_dict):
    print("Detecting bboxes from control panel image")
    process_image(image_path = parameter_dict["control_panel_image_filepath"], bbox_savepath = parameter_dict["bboxes_on_control_panel_filepath"], detected_image_path=parameter_dict["bboxes_on_control_panel_visualisation_filepath"], validity_save_path=parameter_dict["validity_control_panel_folder"])
    print("results saved in ", parameter_dict["bboxes_on_control_panel_filepath"], "\n")
    
    print("Making query images for GPT to match entity to control panel names..")
    make_query_images(image_path=parameter_dict["control_panel_image_filepath"], bbox_savepath = parameter_dict["bboxes_on_control_panel_filepath"], query_image_root_dir = parameter_dict["query_image_to_match_bbox_to_control_element_names_folder"])
    print("results saved in ", parameter_dict["query_image_to_match_bbox_to_control_element_names_folder"], "\n")
    

    print("Map each bbox to possible control panel element names...")
    ground_proposed_entities_in_batch(query_image_dir = parameter_dict["query_image_to_match_bbox_to_control_element_names_folder"], control_panel_elements_from_user_manual = parameter_dict["panel_elements_from_user_manual_filepath"], meta_prompt = prompt_identify_control_panel_element_index, visual_grounding_result_filepath=parameter_dict["map_bbox_index_to_control_panel_element_name_filepath"], raw_image_filepath = parameter_dict["control_panel_image_filepath"])
    print("results saved in ", parameter_dict["map_bbox_index_to_control_panel_element_name_filepath"], "\n")
    

    print("Jsonify the results of mapping control panel element names to bbox indexes...")
    consolidate_mapping_results_simple(parameter_dict["map_bbox_index_to_control_panel_element_name_filepath"], parameter_dict["map_bbox_index_to_control_panel_element_name_json_filepath"], prompt_format_control_panel_element_index, parameter_dict["control_panel_image_index"])
    print("results saved in ", parameter_dict["map_bbox_index_to_control_panel_element_name_json_filepath"], "\n")
    

    print("Map control panel element names to unique bbox indexes...")
    resolve_duplicate_bbox_id_for_one_instance(input_json_filepath=parameter_dict["map_bbox_index_to_control_panel_element_name_json_filepath"], output_json_filepath=parameter_dict["map_bbox_index_to_control_panel_unique_filepath"], raw_image_filepath=parameter_dict["control_panel_image_filepath"], query_image_save_filepath=parameter_dict["query_images_to_match_control_element_names_to_unique_bbox_id_folder"], machine_type = parameter_dict["appliance_type"], bbox_input_root_dir = parameter_dict["bboxes_on_control_panel_filepath"], user_manual_filepath = parameter_dict["user_manual_text_filepath"], task_prompt = remove_duplicate_bboxes_task_prompt, user_manual_prompt = remove_duplicate_bboxes_user_manual_prompt)
    print("results saved in ", parameter_dict["map_bbox_index_to_control_panel_unique_filepath"], "\n")

    print("Map control panel element names to bbox coords...")
    map_control_panel_element_names_to_bbox(index_mapping_filepath=parameter_dict["map_bbox_index_to_control_panel_unique_filepath"], located_bboxes_dir=parameter_dict["bboxes_on_control_panel_filepath"], output_filepath=parameter_dict["proposed_control_element_bbox_filepath"])
    print("results saved in ", parameter_dict["proposed_control_element_bbox_filepath"], "\n")

    print("Visualising grounded control panel elements...")
    visualise_grounded_control_panel_elements(grounded_element_bboxes_filepath= parameter_dict["proposed_control_element_bbox_filepath"], control_panel_image_path= parameter_dict["control_panel_image_filepath"], output_savepath = parameter_dict["visualised_proposed_control_panel_element_bbox_filepath"])
    print("results saved in ", parameter_dict["visualised_proposed_control_panel_element_bbox_filepath"], "\n")
    pass

if __name__ == "__main__":

    #srun -u -o "log.out" -w crane2 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 
    root_dir = os.path.expanduser("~/button_scripts")
    appliance_type = "water_dispenser"
    control_panel_image_index = "0"
    
    # process inputs 
    parameter_dict = prepare_directories(root_dir, appliance_type, control_panel_image_index)
    process_input_files(parameter_dict)
    extract_control_panel_element_names(parameter_dict)
    ground_control_panel_elements(parameter_dict)
    ground_action_names(parameter_dict)