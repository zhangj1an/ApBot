
# based on mapping result, summarise the list of grounded elements:
# out of all picture files, must be at least mapped once. 
# if yes, create a json list as following :
# {
#    "element_name": "start",
#   "bbox": [x1, y1, x2, y2]
#   "image_id": image_id }
# also, generate a list of grounded elements. 


# todo and not impt yet
import os 
import sys 
import re
import shutil
import json
sys.path.append("/data/home/jian/RLS_microwave/utils")
from foundation_models.gpt_4o_model import GPT4O
from utils.create_or_replace_path import create_or_replace_path
from utils.extract_json_code import extract_json_code   
meta_prompt = """

Provided are documents containing control panel elements of an appliance that can be mapped to a detected, indexed bounding boxes. If an element has been mapped at least once, add it to a json list in the following format: 
# {
#    "element_name": "xxx_button" / "xxx_dial" (the control panel element name, but in snake_case format. Please do not leave out any keyword in the main name for easier understanding.),
    "bboxes": [
        {"image_name": "image_name_1" (the image name provided at the beginning of each file), "bbox_id": [x1, x2,..] (an list of integer, each integer is the index of the bounding box.)},
        {"image_name": "image_name_2", "bbox_id": [x3, x4, ..]},
        ....
    ]
# }


"""

# map action to bbox and action type


## # change the format to:
# {button name; options: [{"image_name", "bbox_id"}]}

# and then output a actual python file that adds an additional bbox_coord to each option.

# here need to consolidate, 
# target output is each proposed action -> mapped to a bbox of a certain image name. output a python list. 


def batch_format_json_code(consolidated_results_rootdir):
    # copy this dir to another dir
    try:
        target_dir = consolidated_results_rootdir + "_copy"
        shutil.copytree(consolidated_results_rootdir,  target_dir)
        print(f"Directory copied from {consolidated_results_rootdir} to {target_dir}")
    except FileExistsError as e:
        print(f"Destination directory {target_dir} already exists.")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    # list all directories in mapping_results_root_dir
    machine_type_dirs = [os.path.join(consolidated_results_rootdir, d) for d in os.listdir(consolidated_results_rootdir) ]
    for dir1 in machine_type_dirs:
        machine_id_filepaths = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith(('.json'))]
        for dir2 in machine_id_filepaths:
            # list all json files in the dir
            if "_2_washing_machine/3" not in dir2:
                continue
            with open(dir2, "r") as f:
                content = f.read()
                content = extract_json_code(content)
                with open(dir2, "w") as f:
                    f.write(content)
    pass
    

def satisfy_generated_format(answer):
    # Check if answer is a list
    answer = json.loads(answer)
    if not isinstance(answer, list):
        print("not a list")
        return False
    
    # Iterate over each item in the list
    for item in answer:
        # Check if each item is a dictionary with specific keys
        if not isinstance(item, dict) or 'element_name' not in item or 'bboxes' not in item:
            print("not a dict for answer items")
            return False
        
        # Check if 'bboxes' is a list and each entry in 'bboxes' has the correct structure
        if not isinstance(item['bboxes'], list):
            print("not a list for bboxes")
            return False
        for bbox in item['bboxes']:
            if not isinstance(bbox, dict) or 'image_name' not in bbox or 'bbox_id' not in bbox:
                print("not a dict for bbox")
                return False
            
    return True

def consolidate_mapping_results_simple(mapping_results_filepath, consolidated_results_filepath, meta_prompt, image_id):
    # list all documents in mapping_results_root_dir
    mapping_result_prompt = ""
    mapping_result_prompt += f"\n\nThe following document are from image with id: {image_id}:\n"
    with open(mapping_results_filepath, 'r') as f:
        mapping_result_prompt += f.read()
    
    prompt = meta_prompt + mapping_result_prompt 

    
    satisfied = False 
    while not satisfied:
        print("formatting...")
        model = GPT4O()
        answer = model.chat_with_text(prompt)
        answer = extract_json_code(answer)
        #print(answer)

        satisfied = satisfy_generated_format(answer)
        #print("\n ############result: ", satisfied)
        del model

    # verify format to see if it matches
    
    with open(consolidated_results_filepath, 'w') as f:
        f.write(answer)
        #print(f"consolidated results saved to {consolidated_results_filepath}")
    pass 

def consolidate_mapping_results(mapping_results_dir, consolidated_results_filepath, meta_prompt):
    # list all documents in mapping_results_root_dir
    machine_id = mapping_results_dir.split("/")[-1]
    mapping_results_files = [os.path.join(mapping_results_dir, f) for f in os.listdir(mapping_results_dir) if f.endswith(".txt")]
    mapping_result_prompt = ""
    for file in mapping_results_files:
        file_name = file.split("/")[-1].split(".")[0]
        mapping_result_prompt += f"\n\nThe following document are from image with id: {machine_id}_{file_name}:\n"
        with open(file, 'r') as f:
            mapping_result_prompt += f.read()
    
    prompt = meta_prompt + mapping_result_prompt 

    
    satisfied = False 
    while not satisfied:
        print("formatting...")
        model = GPT4O()
        answer = model.chat_with_text(prompt)
        answer = extract_json_code(answer)
        #print(answer)

        satisfied = satisfy_generated_format(answer)
        #print("\n ############result: ", satisfied)
        del model

    # verify format to see if it matches
    
    with open(consolidated_results_filepath, 'w') as f:
        f.write(answer)
        #print(f"consolidated results saved to {consolidated_results_filepath}")
    pass 

def batch_consolidate_mapping_results(mapping_results_root_dir, consolidated_results_root_dir, meta_prompt):
    # list all directories in mapping_results_root_dir
    machine_type_dirs = [os.path.join(mapping_results_root_dir, d) for d in os.listdir(mapping_results_root_dir) if os.path.isdir(os.path.join(mapping_results_root_dir, d))]
    for dir1 in machine_type_dirs:
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if os.path.isdir(os.path.join(dir1, d))]
        # sort 
        machine_id_dirs.sort()
        for dir2 in machine_id_dirs:
            
            machine_type, machine_id = dir2.split("/")[-2:]

            consolidated_results_filepath = os.path.join(consolidated_results_root_dir, f"{machine_type}/{machine_id}.json")
            if "_2_washing_machine/3" not in dir2:
                continue    
            #if any(substring in consolidated_results_filepath for substring in ["_1_microwave/0", ]):
            #    continue
            print("processing ", dir2)
            create_or_replace_path(consolidated_results_filepath)
            consolidate_mapping_results(dir2, consolidated_results_filepath, meta_prompt)

            #exit()
    pass


if __name__ == "__main__":

   
    mapping_results_root_dir =  os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_index')
    
    consolidate_results_root_dir =os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_1_control_panel_element_index_json')
    
    batch_consolidate_mapping_results(mapping_results_root_dir, consolidate_results_root_dir, meta_prompt)

    # not needed because already extracted json code inside
    #batch_format_json_code(consolidate_results_root_dir)