## target: fix the model generation part so the generated model is perfect and no need close loop calibration. the model should be specific to the command.

import os 
import sys
import shutil
import time 
sys.path.append(os.path.expanduser("~/TextToActions/code/"))
sys.path.append(os.path.expanduser("~/TextToActions/code/real_world/button_scripts/tools"))
import copy
import json
from PIL import Image
from real_world.button_scripts.tools._1_pdf_to_text import convert_pdf_to_images, run_gpt_4o 
from real_world.button_scripts.tools._2_extract_control_panel_element_names_from_user_manual import extract_control_panel_elements
from real_world.button_scripts.tools.utils.task.propose_variables import define_variables
from real_world.button_scripts.tools.utils.task.propose_feature_list import define_feature_list 
from real_world.button_scripts.tools.utils.task.propose_world_model_agnostic_to_command import define_world_model
from real_world.button_scripts.tools.utils.task.propose_goal_state import generate_goal_state
from real_world.button_scripts.tools.utils.task.propose_world_model_specific_to_command import generate_world_model_specific_to_command
from real_world.button_scripts.tools.utils.task.replace_placeholder_in_filepaths import replace_placeholder_in_filepaths
from real_world.button_scripts.tools.utils.task.propose_goal_state import generate_goal_state
from real_world.button_scripts.tools.utils.task.prepare_simulator import prepare_oracle_simulator, prepare_generated_simulator, load_generated_and_goal_simulator, load_generated_code
from real_world.button_scripts.tools._3_detect_bbox_from_photos import process_image, make_query_images
from real_world.button_scripts.tools._4_map_control_panel_element_names_to_bbox_indexes import ground_proposed_entities_in_batch, task_prompt as prompt_identify_control_panel_element_index
from real_world.button_scripts.tools._5_json_map_control_panel_element_names_to_bbox_indexes import consolidate_mapping_results_simple, meta_prompt as prompt_format_control_panel_element_index
from real_world.button_scripts.tools._6_remove_duplicate_bboxes import resolve_duplicate_bbox_id_for_one_instance, user_manual_prompt as remove_duplicate_bboxes_user_manual_prompt, task_prompt as remove_duplicate_bboxes_task_prompt
from real_world.button_scripts.tools._7_json_map_control_panel_element_names_to_bbox import map_element_to_bboxes as map_control_panel_element_names_to_bbox
from real_world.button_scripts.tools._8_visualise_grounding_control_element_name_result import visualise_entities as visualise_grounded_control_panel_elements
from real_world.button_scripts.tools._10_propose_action_names import define_action_names
from real_world.button_scripts.tools.utils.extract_list_from_file import extract_list_from_file
from real_world.button_scripts.tools._11_generated_grounded_action_json import prompt as prompt_map_actions_to_entities, generate_grounded_actions_for_proposed_world_model
from simulated.utils.create_or_replace_path import create_or_replace_path


# do all the things in one file 

from real_world.button_scripts.tools._13_visualisation_grounding_action_result import visualise_actions_in_single_image 
from datetime import datetime



# assumes taking in an png image object 
def save_robot_img(parameter_dict, image, appliance_type, image_filename = "3034"):
    assert image.mode == "RGB", f"Image mode is {image.mode}, expected RGB"

    # Get current time
    now = datetime.now()

    # Format it as "MMSS" (minutes and seconds)
    #image_filename = now.strftime("%M%S")
    parameter_dict = prepare_directories_online(appliance_type, image_filename,"ours_oracle_model", parameter_dict)
    #user_manual_pdf_filepath = os.path.join(parameter_dict["data_output_root_dir"], "_1_user_manual/_0_pdf.pdf") 
    control_panel_image_filepath = parameter_dict["control_panel_image_filepath"]
    # Ensure output directories exist
    #os.makedirs(os.path.dirname(user_manual_pdf_filepath), exist_ok=True)
    os.makedirs(os.path.dirname(control_panel_image_filepath), exist_ok=True)
    # save image to that dir
    image.save(control_panel_image_filepath)
    return parameter_dict
    """
    # Scan _0_input directory
    pdf_file = None
    png_file = None
    input_dir = parameter_dict["data_input_root_dir"]
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_file = filename
        elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
            png_file = filename

    # Move files to their destinations
    #if pdf_file:
    #    shutil.move(os.path.join(input_dir, pdf_file), user_manual_pdf_filepath)

    if png_file:
        shutil.move(os.path.join(input_dir, png_file), control_panel_image_filepath)
    """

def prepare_directories_online(appliance_type, control_panel_image_name, method_name, parameter_dict):
    # the image name must contain extensions like jpg, png, etc.
    root_dir = os.path.expanduser("~/TextToActions/code/real_world/button_scripts")
    data_output_root_dir = os.path.join(root_dir, "data", appliance_type)
    prompt_root_dir = os.path.join(root_dir, "tools/prompts")
    prompt_model_dir = os.path.join(prompt_root_dir, "paper_exp/baselines_v1/_4_HV_M_SR_MA_agnostic")
    results_root_dir = os.path.join(data_output_root_dir, f"_5_results/{method_name}/{appliance_type}")
    updated_dict =  {
        # changes with each image
        "control_panel_image_index": control_panel_image_name,
        "control_panel_image_filepath": os.path.join(data_output_root_dir, f"_2_control_panel_images/_0_raw/{control_panel_image_name}.png"),
        "bboxes_on_control_panel_filepath": os.path.join(data_output_root_dir, f"_2_control_panel_images/{control_panel_image_name}/_1_ground_control_panel_elements/_2_bboxes_on_control_panel.json"),
        "validity_control_panel_folder": os.path.join(data_output_root_dir, f"_2_control_panel_images/{control_panel_image_name}/_1_ground_control_panel_elements/_1_validity_control_panel"),
        "bboxes_on_control_panel_visualisation_filepath": os.path.join(data_output_root_dir, f"_2_control_panel_images/{control_panel_image_name}/_1_ground_control_panel_elements/_3_bboxes_on_control_panel_visualisation.png"),
        "query_image_to_match_bbox_to_control_element_names_folder": os.path.join(data_output_root_dir, f"_2_control_panel_images/{control_panel_image_name}/_1_ground_control_panel_elements/_4_query_images_bbox_to_name"),
        
        
        "map_bbox_index_to_control_panel_element_name_filepath": os.path.join(data_output_root_dir, f"_3_visual_grounding/{control_panel_image_name}/_0_control_panel_element_bbox/_0_control_panel_element_index.txt"),
        "map_bbox_index_to_control_panel_element_name_json_filepath": os.path.join(data_output_root_dir, f"_3_visual_grounding/{control_panel_image_name}/_0_control_panel_element_bbox/_1_control_panel_element_index.json"),
        "map_bbox_index_to_control_panel_unique_filepath": os.path.join(data_output_root_dir, f"_3_visual_grounding/{control_panel_image_name}/_0_control_panel_element_bbox/_2_control_panel_element_index_unique.json"),
        "query_images_to_match_control_element_names_to_unique_bbox_id_folder": os.path.join(data_output_root_dir, f"_2_control_panel_images/{control_panel_image_name}/_1_ground_control_panel_elements/_5_query_images_unique_bbox_id"),
        "proposed_control_element_bbox_filepath": os.path.join(data_output_root_dir, f"_3_visual_grounding/{control_panel_image_name}/_0_control_panel_element_bbox/_3_proposed_control_panel_element_bbox.json"),
        "visualised_proposed_control_panel_element_bbox_filepath": os.path.join(data_output_root_dir, f"_3_visual_grounding/{control_panel_image_name}/_0_control_panel_element_bbox/_4_visualised_proposed_control_panel_element_bbox.png"),
        "proposed_actions_bbox_filepath": os.path.join(data_output_root_dir, f"_3_visual_grounding/{control_panel_image_name}/_1_action_names/_2_proposed_action_bbox.json"),
        "visualised_proposed_actions_filepath": os.path.join(data_output_root_dir, f"_3_visual_grounding/{control_panel_image_name}/_1_action_names/_3_visualised_proposed_actions.png"),

    }
    """
    create_or_replace_path(updated_dict["control_panel_image_filepath"])
    create_or_replace_path(updated_dict["bboxes_on_control_panel_filepath"])
    create_or_replace_path(updated_dict["validity_control_panel_folder"])
    create_or_replace_path(updated_dict["bboxes_on_control_panel_visualisation_filepath"])
    create_or_replace_path(updated_dict["query_image_to_match_bbox_to_control_element_names_folder"])
    create_or_replace_path(updated_dict["map_bbox_index_to_control_panel_element_name_filepath"])
    create_or_replace_path(updated_dict["map_bbox_index_to_control_panel_element_name_json_filepath"])
    create_or_replace_path(updated_dict["map_bbox_index_to_control_panel_unique_filepath"])
    create_or_replace_path(updated_dict["query_images_to_match_control_element_names_to_unique_bbox_id_folder"])
    create_or_replace_path(updated_dict["proposed_control_element_bbox_filepath"])
    create_or_replace_path(updated_dict["visualised_proposed_control_panel_element_bbox_filepath"])
    create_or_replace_path(updated_dict["proposed_actions_bbox_filepath"])
    create_or_replace_path(updated_dict["visualised_proposed_actions_filepath"])
    """
    combined = {**updated_dict, **parameter_dict}
    combined["open_loop_bbox"] = combined["open_loop_bbox"].replace("yyyyy", control_panel_image_name)
    return combined

def prepare_directories_offline(appliance_type, method_name):
    # the image name must contain extensions like jpg, png, etc.
    root_dir = os.path.expanduser("~/TextToActions/code/real_world/button_scripts")
    data_output_root_dir = os.path.join(root_dir, "data", appliance_type)
    prompt_root_dir = os.path.join(root_dir, "tools/prompts")
    prompt_model_dir = os.path.join(prompt_root_dir, "paper_exp/baselines_v1/_4_HV_M_SR_MA_agnostic")
    results_root_dir = os.path.join(data_output_root_dir, f"_5_results/{method_name}/")

    template_code_root = os.path.join(root_dir, "samples")
    template_code_filepaths = [os.path.join(template_code_root, f) for f in ["_0_search.py", "_1_variables.py", "_2_features.py", "_3_actions.py"]]

    parameter_dict = {
        "control_panel_image_filepath": os.path.join(data_output_root_dir, f"_0_input/1.png"),
        "appliance_type": appliance_type,
        "testcase_input_filepath": os.path.join(data_output_root_dir ,  "_4_testcases/1.py"),
        "user_manual_pdf_filepath": os.path.join(data_output_root_dir, "_1_user_manual/0.pdf"),
        "user_manual_image_folder_path": os.path.join(data_output_root_dir, "_1_user_manual/_1_images"),
        "user_manual_text_filepath": os.path.join(data_output_root_dir, "_1_user_manual/_2_text.txt"),
        "user_manual_legend_folderpath": os.path.join(data_output_root_dir, "_1_user_manual/_2_legends"),
        "template_code_filepaths": template_code_filepaths,

        # prompts
        
        "prompt_propose_control_panel_element_filepath": os.path.join(prompt_root_dir, "_2_extract_control_panel_element.txt"),
        "prompt_filter_control_panel_element_filepath": os.path.join(prompt_root_dir, "_2_filter_control_panel_element.txt"),

        "prompt_propose_action_filepath": os.path.join(prompt_root_dir, "_10_create_action_names.txt"),
        "prompt_filter_action_filepath": os.path.join(prompt_root_dir, "_10_filter_action_names.txt"),

        "define_variables": os.path.join(prompt_model_dir, "_0_define_variables.txt"),
        "define_feature_list": os.path.join(prompt_model_dir, "_1_define_feature_list.txt"),
        "prompt_verify_feature_list": os.path.join(prompt_model_dir, "_2_verify_feature_list.txt"),
        "prompt_verify_meta_actions": os.path.join(prompt_model_dir, "_3_verify_meta_actions.txt"),
        "define_world_model": os.path.join(prompt_model_dir, "_4_define_world_model.txt"),
        "make_world_model_specific_to_command": os.path.join(prompt_model_dir, "_5_regenerate_model.txt"),
        "generate_goal_state": os.path.join(prompt_model_dir, "_6_generate_goal_state.txt"),
        

        # build appliance model 
        "control_panel_label_details": os.path.join(results_root_dir, "_0_reasoning/_1_control_panel_label_details.txt"),
        "proposed_variables": os.path.join(results_root_dir, "_0_reasoning/_2_proposed_variables.py"),
        "proposed_features": os.path.join(results_root_dir, "_0_reasoning/_3_proposed_feature_list.py"),
        "proposed_world_model": os.path.join(results_root_dir, "_0_reasoning/_4_proposed_world_model.py"),
        
        # ground actions
        "panel_elements_from_user_manual_filepath": os.path.join(data_output_root_dir, "_1_user_manual/_3_extracted_control_panel_element_names.py"),
        "proposed_actions_filepath": os.path.join(data_output_root_dir, f"_1_user_manual/_1_proposed_action_names.txt"),

        # results 
        "world_model_specific_to_command": os.path.join(results_root_dir, "_1_commands/xxxxx/_1_world_model_specific_to_command.py"),
        "goal_state": os.path.join(results_root_dir, "_1_commands/xxxxx/_2_goal_state.py"),
        "log_record": os.path.join(results_root_dir, "_1_commands/xxxxx/_3_log_record.json"),
        "raw_output": os.path.join(results_root_dir, "_1_commands/xxxxx/_4_raw_output.txt"),
        "open_loop_policy": os.path.join(results_root_dir, "_1_commands/xxxxx/_5_open_loop_policy.json"),
        "open_loop_bbox": os.path.join(results_root_dir, "_1_commands/xxxxx/_6_open_loop_bbox_on_image_yyyyy.json"),

    }
    return parameter_dict 

def extract_control_panel_element_names(parameter_dict):

    if not os.path.exists(parameter_dict["user_manual_image_folder_path"]):
        print("Converting user manual pdf to images")
        convert_pdf_to_images(parameter_dict["user_manual_pdf_filepath"], parameter_dict["user_manual_image_folder_path"])
        print("results saved in ", parameter_dict["user_manual_image_folder_path"], "\n")
    
    if not os.path.exists(parameter_dict["user_manual_text_filepath"]):
        # run gpt-4o to extract text from user manual images
        print("Running GPT-4o to extract text from user manual images")
        run_gpt_4o(parameter_dict["user_manual_image_folder_path"], parameter_dict["user_manual_text_filepath"])
        print("results saved in ", parameter_dict["user_manual_text_filepath"], "\n")

    if not os.path.exists(parameter_dict["panel_elements_from_user_manual_filepath"]):
        # run gpt-4o to extract control panel elements from user manual text
        print("Running GPT-4o to extract control panel elements from user manual text")
        extract_control_panel_elements(parameter_dict["user_manual_text_filepath"], parameter_dict["panel_elements_from_user_manual_filepath"], parameter_dict["prompt_propose_control_panel_element_filepath"], parameter_dict["prompt_filter_control_panel_element_filepath"], parameter_dict["control_panel_image_filepath"])
        print("results saved in ", parameter_dict["panel_elements_from_user_manual_filepath"], "\n")

    
    pass


def ground_action_names(parameter_dict):

    

    print("grounding action names to bboxes")
    generate_grounded_actions_for_proposed_world_model(prompt_map_actions_to_entities, parameter_dict["proposed_actions_filepath"], parameter_dict["proposed_control_element_bbox_filepath"], parameter_dict["proposed_actions_bbox_filepath"])
    print("results saved in ", parameter_dict["proposed_actions_bbox_filepath"], "\n")
    

    print("visualise grounded actions")
    visualise_actions_in_single_image(parameter_dict["proposed_actions_bbox_filepath"], parameter_dict["control_panel_image_filepath"], parameter_dict["visualised_proposed_actions_filepath"], "")
    print("results saved in ", parameter_dict["visualised_proposed_actions_filepath"], "\n")




def ground_control_panel_elements(parameter_dict, appliance_type, image_filename = "1"):
    print("Detecting bboxes from control panel image")
    # # blender: 0.08
    # dispenser: 0.12
    owl_conf = 0.2 
    require_ocr = False
    require_sam = False
    if appliance_type == "blender":
        owl_conf = 0.1
        #require_sam = True
    elif appliance_type == "water_dispenser":
        owl_conf = 0.1
        #require_ocr = True
    elif appliance_type == "induction_cooker":
        owl_conf = 0.1
    process_image(image_path = parameter_dict["control_panel_image_filepath"], bbox_savepath = parameter_dict["bboxes_on_control_panel_filepath"], detected_image_path=parameter_dict["bboxes_on_control_panel_visualisation_filepath"], validity_save_path=parameter_dict["validity_control_panel_folder"], require_ocr=require_ocr, require_sam=require_sam, owl_conf = owl_conf, )
    print("results saved in ", parameter_dict["bboxes_on_control_panel_filepath"], "\n" )
    
    print("Making query images for GPT to match entity to control panel names..")
    make_query_images(image_path=parameter_dict["control_panel_image_filepath"], bbox_savepath = parameter_dict["bboxes_on_control_panel_filepath"], query_image_root_dir = parameter_dict["query_image_to_match_bbox_to_control_element_names_folder"])
    print("results saved in ", parameter_dict["query_image_to_match_bbox_to_control_element_names_folder"], "\n")
    

    print("Map each bbox to possible control panel element names...")
    model_type = "gpt"
    #if appliance_type == "blender":
    #    model_type = "claude"
    ground_proposed_entities_in_batch(query_image_dir = parameter_dict["query_image_to_match_bbox_to_control_element_names_folder"], control_panel_elements_from_user_manual = parameter_dict["panel_elements_from_user_manual_filepath"], meta_prompt = prompt_identify_control_panel_element_index, visual_grounding_result_filepath=parameter_dict["map_bbox_index_to_control_panel_element_name_filepath"], raw_image_filepath = parameter_dict["control_panel_image_filepath"], user_manual_legend_folderpath = parameter_dict["user_manual_legend_folderpath"], model_type = model_type)
    print("results saved in ", parameter_dict["map_bbox_index_to_control_panel_element_name_filepath"], "\n")
    

    print("Jsonify the results of mapping control panel element names to bbox indexes...")
    consolidate_mapping_results_simple(parameter_dict["map_bbox_index_to_control_panel_element_name_filepath"], parameter_dict["map_bbox_index_to_control_panel_element_name_json_filepath"], prompt_format_control_panel_element_index, image_filename)
    print("results saved in ", parameter_dict["map_bbox_index_to_control_panel_element_name_json_filepath"], "\n")
    

    print("Map control panel element names to unique bbox indexes...")
    resolve_duplicate_bbox_id_for_one_instance(input_json_filepath=parameter_dict["map_bbox_index_to_control_panel_element_name_json_filepath"], output_json_filepath=parameter_dict["map_bbox_index_to_control_panel_unique_filepath"], raw_image_filepath=parameter_dict["control_panel_image_filepath"], query_image_save_filepath=parameter_dict["query_images_to_match_control_element_names_to_unique_bbox_id_folder"], machine_type = parameter_dict["appliance_type"], bbox_input_root_dir = parameter_dict["bboxes_on_control_panel_filepath"], user_manual_filepath = parameter_dict["user_manual_text_filepath"], task_prompt = remove_duplicate_bboxes_task_prompt, user_manual_prompt = remove_duplicate_bboxes_user_manual_prompt, user_manual_legends_folder_path = parameter_dict["user_manual_legend_folderpath"], )
    print("results saved in ", parameter_dict["map_bbox_index_to_control_panel_unique_filepath"], "\n")

    print("Map control panel element names to bbox coords...")
    map_control_panel_element_names_to_bbox(index_mapping_filepath=parameter_dict["map_bbox_index_to_control_panel_unique_filepath"], located_bboxes_dir=parameter_dict["bboxes_on_control_panel_filepath"], output_filepath=parameter_dict["proposed_control_element_bbox_filepath"])
    print("results saved in ", parameter_dict["proposed_control_element_bbox_filepath"], "\n")

    print("Visualising grounded control panel elements...")
    visualise_grounded_control_panel_elements(grounded_element_bboxes_filepath= parameter_dict["proposed_control_element_bbox_filepath"], control_panel_image_path= parameter_dict["control_panel_image_filepath"], output_savepath = parameter_dict["visualised_proposed_control_panel_element_bbox_filepath"])
    print("results saved in ", parameter_dict["visualised_proposed_control_panel_element_bbox_filepath"], "\n")
    pass

def build_model_and_prepare_command(appliance_type, method_name, gpt_model_type):
    
    
    extract_control_panel_element_names(parameter_dict)
    # propose variables, features and world models.
    # takes in a command, generate symbolic policy.

    print("Defining action names")
    # check if this file dont exist, then execute. 
    if not os.path.exists(parameter_dict["proposed_actions_filepath"]):
        define_action_names(parameter_dict["user_manual_text_filepath"], parameter_dict["panel_elements_from_user_manual_filepath"], parameter_dict["prompt_propose_action_filepath"], parameter_dict["prompt_filter_action_filepath"], parameter_dict["proposed_actions_filepath"])
        print("results saved in ", parameter_dict["proposed_actions_filepath"], "\n")

    print("defining variables")
    if not os.path.exists(parameter_dict["proposed_variables"]):
    # check if this file dont exist, then execute. 
        define_variables(gpt_model_type,parameter_dict["proposed_actions_filepath"], parameter_dict["user_manual_text_filepath"], parameter_dict["panel_elements_from_user_manual_filepath"], parameter_dict["define_variables"], parameter_dict["template_code_filepaths"][1], parameter_dict["proposed_variables"], "", use_history = True)
        print("finished defining variables")

    print("defining features")
    if not os.path.exists(parameter_dict["proposed_features"]):
    # check if this file dont exist, then execute. 
        define_feature_list(gpt_model_type, parameter_dict["proposed_actions_filepath"], parameter_dict["proposed_variables"], parameter_dict["user_manual_text_filepath"],  parameter_dict["define_feature_list"], parameter_dict["proposed_features"], parameter_dict["template_code_filepaths"][2], parameter_dict["prompt_verify_feature_list"], parameter_dict["prompt_verify_meta_actions"], "", verbose=False, use_history = True)
    
    print("defining world model")
    if not os.path.exists(parameter_dict["proposed_world_model"]):
    # define world model agnostic to the command. 
    # check if this file dont exist, then execute. 
        define_world_model(gpt_model_type, parameter_dict["proposed_actions_filepath"], parameter_dict["proposed_variables"], parameter_dict["proposed_features"], parameter_dict["user_manual_text_filepath"], parameter_dict["define_world_model"], parameter_dict["proposed_world_model"], parameter_dict["template_code_filepaths"][1], parameter_dict["template_code_filepaths"][2], parameter_dict["template_code_filepaths"][3], "", use_history = True)

    # for each command, generate the goal state. 
    testcases = extract_list_from_file(parameter_dict["testcase_input_filepath"])
    for id, testcase in enumerate(testcases):
        if not (appliance_type == "induction_cooker" and id in [0, 1, 2]):
            continue
        command_string = testcase 
        # 
        parameter_dict_copy = copy.deepcopy(parameter_dict)
        # for every value in the dict, replace the xxxxx with the command string id.
        for key, value in parameter_dict_copy.items():
            if key in ["world_model_specific_to_command", "goal_state", "log_record", "raw_output", "open_loop_policy", "open_loop_bbox"]:
                parameter_dict_copy[key] = value.replace("xxxxx", str(id))

        if not os.path.exists(parameter_dict_copy["world_model_specific_to_command"]):
            generate_world_model_specific_to_command(gpt_model_type, parameter_dict, parameter_dict["proposed_actions_filepath"], parameter_dict, parameter_dict["template_code_filepaths"][1:], parameter_dict_copy, parameter_dict["user_manual_text_filepath"], command_string, use_history = True)

        generated_code_filepaths = [parameter_dict_copy["proposed_variables"], parameter_dict_copy["proposed_features"], parameter_dict_copy["proposed_world_model"]]
        if not os.path.exists(parameter_dict_copy["goal_state"]):
            generate_goal_state(gpt_model_type, parameter_dict_copy["generate_goal_state"], parameter_dict_copy["goal_state"], parameter_dict["template_code_filepaths"][1:], generated_code_filepaths, command_string, parameter_dict["user_manual_text_filepath"], parameter_dict_copy["world_model_specific_to_command"], use_history = True)

        generated_appliance_code, generated_files = prepare_generated_simulator(parameter_dict["template_code_filepaths"][0], generated_code_filepaths, parameter_dict_copy) 

        generated_appliance_code = load_generated_code(generated_files[:3])
        generated_goal_code = load_generated_code(generated_files) 

        current_state_simulator, goal_state_simulator, feature_sequence, AStarSearch = load_generated_and_goal_simulator(generated_appliance_code, generated_goal_code)

        print(f"\ncurrent_state_simulator when it is just created: \n\n {current_state_simulator}")
        print("generated_appliance_code saved in")
        with open("temp.txt", "w") as f:
            f.write(generated_appliance_code)
        print("\ngoal state: ", goal_state_simulator)

        actions = [action for action in dir(current_state_simulator) if action.startswith(('press_', 'turn_')) and callable(getattr(current_state_simulator, action))]
        print("current_state_simulator: ", current_state_simulator.feature.feature_list, flush=True)
        feature_list = current_state_simulator.feature.feature_list 

        has_error = False  
        output_policy = []
        for feature_progress_index in range(len(feature_sequence)):
            if has_error == True:
                break 
            current_feature = feature_sequence[feature_progress_index]
            print("current feature: ", current_feature)
            current_feature_info = feature_list[current_feature]

            subgoal_simulator = copy.deepcopy(current_state_simulator)
            feedbacks = []
            
            for step_info in current_feature_info:
                if has_error:
                    break 
                print("step_info: ", step_info)
                current_action = step_info["actions"][0]
                #current_action = (current_action, 1)
                # if it is a number action, skip this step 
                #if (not hasattr(current_state_simulator, "meta_actions_dict")) or (current_action[0] not in current_state_simulator.meta_actions_dict.values()):
                #    print(f"executing action: {current_action}")
                #    output_policy.append(current_action)
                    
                    
                # if at the step the goal is already fulfilled, then should still execute the action because the step is not skippable. 
                if "variable" not in step_info:
                    output_policy.append(current_action)
                    continue 

                
                variable_name = step_info["variable"]
                subgoal_variable = goal_state_simulator.get_variable_by_name(variable_name)
                subgoal_variable_value = goal_state_simulator.get_variable_value(variable_name)
                goal_state_string = f"We want to have the variable: {variable_name} to have a value of {subgoal_variable_value}. "
                print("goal state string: ", goal_state_string)
                setattr(subgoal_simulator, variable_name, subgoal_variable)

                if subgoal_variable is None:
                    print(f"variable {variable_name} is not in the simulator attributes, this should not happen, code has bug, return error")
                    break

                actions = step_info["actions"]

                # here check for mismatch. other places do not need to check for mismatch.
                reached_goal = None 

                print(f"goal_state_simulator: {subgoal_simulator}")
                print(f"current_state_simulator: {current_state_simulator}")
                print(f"variable_name: {variable_name}")
                print(f"actions: {actions}")
                print(f"astarsearch: {AStarSearch}")
                astar = AStarSearch(current_state_simulator, subgoal_simulator, actions, [variable_name], current_feature, verbose=False)
                planning_result = astar.search()
                
                print("planning_result: ", planning_result)

    
                if len(planning_result) > 0:
                    for current_action in planning_result: 
                        output_policy.append(current_action)
                                           
                    
                
            open_loop_policy_filepath = parameter_dict_copy["open_loop_policy"]
            create_or_replace_path(open_loop_policy_filepath)
            with open(open_loop_policy_filepath, "w") as f:
                json.dump(output_policy, f, indent=4)
            
            shutil.copyfile("log.out", parameter_dict_copy["raw_output"])
        

    pass 

def get_bbox_for_action(action_name, json_path):
    # Load the JSON file
    with open(json_path, "r") as f:
        data = json.load(f)
    
    # Search for the action
    for item in data:
        if item["action"] == action_name:
            # Return the first bbox (assuming one per action)
            return item["bboxes"][0]["bbox"][0]
    
    # If not found
    raise ValueError(f"Action '{action_name}' not found in {json_path}")

def ground_open_loop_policy(appliance_type,  image, parameter_dict, image_filename = "3034"):
    parameter_dict = save_robot_img(parameter_dict, image, appliance_type, image_filename)

    if not os.path.exists(parameter_dict["proposed_actions_bbox_filepath"]):
        ground_control_panel_elements(parameter_dict, appliance_type, image_filename)
        ground_action_names(parameter_dict)
    commands = extract_list_from_file(parameter_dict["testcase_input_filepath"])
    all_results = []
    for policy_id in range(3):
        for key, value in parameter_dict.items():
            if key in ["world_model_specific_to_command", "goal_state", "log_record", "raw_output", "open_loop_policy", "open_loop_bbox"]:
                parameter_dict[key] = value.replace("xxxxx", str(command_id))
        # load the open loop policy file, 
        open_loop_coords = []
        with open(parameter_dict["open_loop_policy"], "r") as f:
            open_loop_policy = json.load(f)
        
        for action in open_loop_policy:
            action_name = action[0] 
            action_duration = action[1]
            action_bbox = get_bbox_for_action(action_name, parameter_dict["proposed_actions_bbox_filepath"])
            # get the bbox for the action
            open_loop_coords.append((action_name, action_bbox, action_duration))

             # Save in the desired format
            final_result = {
                "task": commands[policy_id],
                "policy": open_loop_coords,
            }
            create_or_replace_path(parameter_dict["open_loop_bbox"])
            with open(parameter_dict["open_loop_bbox"], "w") as f:
                json.dump(final_result, f, indent=4)
            all_results.append(final_result)

   
    return all_results

if __name__ == "__main__":

    #srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 

    appliance_type = "water_dispenser" #"induction_cooker" #"blender"# "water_dispenser" # 
    control_panel_image_name = "0.png"
    method_name = "ours_oracle_model"
    gpt_model_type = "gpt-4o"
    command_id = 0 # can be 0, 1, 2
    parameter_dict = prepare_directories_offline(appliance_type, method_name)
    #build_model_and_prepare_command(appliance_type, method_name, gpt_model_type)

    
    # process inputs 
    
    # one off: (done before demo)

    
    image_filepath = parameter_dict["control_panel_image_filepath"]
    # load a test image from a filepath
    image = Image.open(image_filepath).convert("RGB")
    # server side: 

    #open_loop_coords = ground_open_loop_policy(appliance_type, image, parameter_dict, "1")

    #with open(f"{appliance_type}_task_coords.json", "w") as f:
    #    json.dump(open_loop_coords, f, indent=4)

    # then load the policy file, 
    # and convert the output policy to a list of (action name, bbox coord, duration)


    # firstly takes in an image.
    # command id is pregiven. then output a list of tuples, (action name, bbox coord).


    # as for CoT-image, would require input of image at every single step. do tmr. 

    # for now, just implement the perfect model. 
    # tmr, implement the CoT-image version; extract one step, observes the state, decides on the next step. needs to buy light.
    # next week, implement the close loop version whereby model can be updated, and make instruction harder. 