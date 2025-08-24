# ask llava about which button is which
import json
import _0_t2a_config

from foundation_models.owlv2_crane5_query import visualize_image
from foundation_models.gpt_4o_model import GPT4O
from foundation_models.claude_sonnet_model import ClaudeSonnet
from utils.create_or_replace_path import create_or_replace_path
from _3_detect_bbox_from_photos import sort_raw_image_key
from PIL import Image
import time
import os

task_prompt = """
The elements listed above are responsible for the operation and feedback of the appliance's control panel. They represent names of buttons, dials, switches and digital displays. Please ignore the indicators.

I will input three images of the control panel, with a bounding box index: xxxxx. 

The first image is the original photo. The second image contains a zoomed in version of a certain part of the appliance, and contain red bounding box and some green bounding boxes. The third image represents the same zoomed in region, but contains no bounding boxes. I may also attach some user manual legends that explains the layout of the appliance. I want to firstly ask a question: whether the red bounding box circles out an object mentioned in the above list. If the answer is yes, then I want to ask a second question. If any green bounding box is selecting the same object as the red bounding box, then compared to the green bounding boxes, is the red bounding box a good choice to represent the object of your choice? As long as the red bounding box is a better choice than the green bounding boxes, then the answer is yes. It is okay for the red boxes to only circle out partial of the object.

As the photo is taken from a robot arm, every bottom area of the photo contains a robot gripper. Please only choose bounding boxes that circles out regions on the appliance, and ignore the regions on the robot grippers.

The choosing criteria is as follows: For dials, only select the bounding box that covers the dial knob, and ignore bounding boxes that select the labellings. For buttons, if the button consists of a physical button (a executable region, probably with symbols and text on it) and a label located outside of it, choose the bounding box that circles out the physical button. If the bounding box only selects the label area, it is invalid.

If both answer is yes, then output the control panel name, followed by the bounding box index: xxxxx. Note that the control panel name must have the exact same spelling as the given names. The format is:
<control_element_name> : <index>

For example, if an element called "time_button" is circled by the red bounding box, and the index is 0, then the output should be:

time_button : 0

Always check the entire list to see if the red bounding box can be mapped to multiple element names. As long as the bounding box circled matches the examined element name, the matched name should be included. Then output like this:
<control_element_name> : <index>
<control_element_name> : <index>
...

Please copy the control element name exactly as listed.

Otherwise, reply "None". As long as the red bounding box contains a label, a symbol or a control panel element, be lenient and try to match it to a number. Avoid using "None" as much as possible.

Please do not return anything else.


"""

gpt_model = GPT4O()
claude_model = ClaudeSonnet()

def extract_digit(filepath):
    filename = filepath.split('/')[-1]
    return int(filename.split('.')[0])

def group_and_sort_image_files(file_list):
    """Group files into pairs based on their names and sort them."""
    # Create a dictionary to store pairs
    pairs_dict = {}

    for file_name in file_list:
        # Split the file name into parts
        parts = file_name.split("/")[-1].split('_')
        key = int(parts[0])  # The first digit is the key

        # Add the file name to the dictionary under the appropriate key
        if key not in pairs_dict:
            pairs_dict[key] = [file_name]
        else:
            pairs_dict[key].append(file_name)

    # Sort each pair and convert the dictionary to a sorted list of lists
    sorted_pairs_list = [sorted(pairs_dict[key]) for key in sorted(pairs_dict.keys())]

    return sorted_pairs_list



def ground_proposed_entities_in_batch(query_image_dir = "/data/home/jian/RLS_microwave/benchmark_2/control_panel_images_query_images/1_air_fryer/0/0", control_panel_elements_from_user_manual = "/data/home/jian/RLS_microwave/benchmark_2/panel_elements_from_user_manual/1_air_fryer/0.txt", meta_prompt = task_prompt, user_manual_filepath = "/data/home/jian/RLS_microwave/benchmark_2/user_manuals/1_air_fryer/0.txt", visual_grounding_result_filepath = "/data/home/jian/RLS_microwave/benchmark_2/visual_grounding_results/1_air_fryer/0/0.txt", user_manual_legend_folderpath = "",raw_image_filepath = "", machine_type = "", machine_id = "", pic_id = "", model_type = "gpt"):
    
    
    print("query_image_dir", query_image_dir)
    control_panel_elements = ""
    with open(control_panel_elements_from_user_manual, 'r') as file:
        control_panel_elements = file.read()
    # load as a multi-line string 
    namespace = {}
    exec(control_panel_elements, namespace)  # Executes the file content, populating `namespace`

    # Access the list variable
    my_list = namespace["names_list"]

    # Convert the list to a multiline string
    control_panel_elements = "\n".join(my_list)
    prompt = control_panel_elements + meta_prompt 

    # list all images in the query image directory
    image_filepaths = [f for f in os.listdir(query_image_dir) if f.endswith((".jpg", ".png", ".jpeg"))]

    user_manual_legend_filepaths = []
    if user_manual_legend_folderpath != "":
        user_manual_legend_filepaths = [f for f in os.listdir(user_manual_legend_folderpath) if f.endswith((".jpg", ".png", ".jpeg"))]
        # filter out files that have "backup" in the name
        user_manual_legend_filepaths = [f for f in user_manual_legend_filepaths if "backup" not in os.path.basename(f)]
        # sort the files using your sort_raw_image_key
        user_manual_legend_filepaths = sorted(user_manual_legend_filepaths, key=sort_raw_image_key)
        user_manual_legend_filepaths = [os.path.join(user_manual_legend_folderpath, f) for f in user_manual_legend_filepaths]
        
    # First, filter out files that have "backup" in the name
    image_filepaths = [f for f in image_filepaths if "backup" not in os.path.basename(f)]

    # Then, sort the remaining files using your sort_raw_image_key
    image_filepaths = sorted(image_filepaths, key=sort_raw_image_key)


    image_filepaths = [os.path.join(query_image_dir, f) for f in image_filepaths]

    query_image_pairs = group_and_sort_image_files(image_filepaths)
    # save the response to a file
    create_or_replace_path(visual_grounding_result_filepath)

    for image_pairs in query_image_pairs:
        image_index = image_pairs[0].split("/")[-1].split("_")[0]
        
        #if image_index != "17":
        #    continue
        my_prompt = prompt.replace("xxxxx", image_index)
        if model_type == "gpt":
            model = GPT4O()
            response = model.chat_with_multiple_images(my_prompt, [raw_image_filepath] + image_pairs + user_manual_legend_filepaths)
        elif model_type == "claude":
            model = ClaudeSonnet()
            response = model.chat_with_multiple_images([raw_image_filepath] + image_pairs + user_manual_legend_filepaths, my_prompt)
        del model

        with open(visual_grounding_result_filepath, 'a') as file:
            file.write(response + "\n")
    #exit()
    pass 

def batch_ground_proposed_entities(query_image_root_dir = "/data/home/jian/RLS_microwave/benchmark_2/control_panel_images_query_images", control_panel_elements_from_user_manual_root_dir = "/data/home/jian/RLS_microwave/benchmark_2/panel_elements_from_user_manual", meta_prompt = task_prompt, user_manual_root_dir = "/data/home/jian/RLS_microwave/benchmark_2/user_manuals", visual_grounding_result_root_dir = "/data/home/jian/RLS_microwave/benchmark_2/visual_grounding_results", raw_image_dir = "/data/home/jian/RLS_microwave/benchmark_2/control_panel_images_selected"):
    machine_type_dirs = [os.path.join(query_image_root_dir, d) for d in os.listdir(query_image_root_dir) if os.path.isdir(os.path.join(query_image_root_dir, d))]
    machine_type_dirs.sort()
    for dir1 in machine_type_dirs:
        machine_type = dir1.split("/")[-1]
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if os.path.isdir(os.path.join(dir1, d))]

        machine_id_dirs.sort()
        for dir2 in machine_id_dirs:
            pic_id_dirs = [os.path.join(dir2, f) for f in os.listdir(dir2) if os.path.isdir(os.path.join(dir2, f))]
            pic_id_dirs.sort()
            for pic_id_dir in pic_id_dirs:
                if not any(substring in pic_id_dir for substring in ["_2_washing_machine/3"]): #not
                    continue
                pic_id = pic_id_dir.split("/")[-1]
                print(f"processing {pic_id_dir}")
                query_image_dir = pic_id_dir 
                machine_type, machine_id, pic_id = query_image_dir.split("/")[-3:]
                control_panel_elements_from_user_manual_filepath = os.path.join(control_panel_elements_from_user_manual_root_dir, f"{machine_type}/_{machine_id}.py")
                user_manual_filepath = os.path.join(user_manual_root_dir, f"{machine_type}/_{machine_id}.txt")
                raw_image_files = [f for f in os.listdir(os.path.join(raw_image_dir, machine_type)) if f.endswith((".jpg", ".png", ".jpeg"))]
                raw_image_filepath = [f for f in raw_image_files if f"{machine_id}_{pic_id}" in f][0]
                raw_image_filepath = os.path.join(raw_image_dir, machine_type, raw_image_filepath)
                
                visual_grounding_result_filepath = os.path.join(visual_grounding_result_root_dir, f"{machine_type}/{machine_id}/{pic_id}.txt")
                create_or_replace_path(visual_grounding_result_filepath)
                ground_proposed_entities_in_batch(query_image_dir = query_image_dir, control_panel_elements_from_user_manual = control_panel_elements_from_user_manual_filepath, meta_prompt = meta_prompt, user_manual_filepath = user_manual_filepath, visual_grounding_result_filepath = visual_grounding_result_filepath, raw_image_filepath = raw_image_filepath, machine_type = machine_type, machine_id = machine_id, pic_id = pic_id, model_type="gpt")
                #exit()

if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Map Each Bounding Box to a Control Panel Element Name
    #
    #######################################
    query_image_root_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_2_control_panel_images/_5_query_images_bbox_to_name/')
    control_panel_elements_from_user_manual_root_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_3_extracted_control_panel_element_names')
    meta_prompt = task_prompt   
    user_manual_root_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_2_text')
    visual_grounding_result_root_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_index')
    raw_image_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_2_control_panel_images/_1_selected')
    
    batch_ground_proposed_entities(query_image_root_dir, control_panel_elements_from_user_manual_root_dir, meta_prompt, user_manual_root_dir, visual_grounding_result_root_dir, raw_image_dir)

    #ground_proposed_entities_in_batch(query_image_dir = "/data/home/jian/TextToActions/dataset/simulated/_2_control_panel_images/_5_query_images_bbox_to_name/_6_coffee_machine/0/0", control_panel_elements_from_user_manual = "/data/home/jian/TextToActions/dataset/simulated/_1_user_manual/_3_extracted_control_panel_element_names/_6_coffee_machine/_0.txt", meta_prompt = task_prompt, user_manual_filepath = "", visual_grounding_result_filepath = "/data/home/jian/TextToActions/dataset/simulated/_4_visual_grounding/_0_control_panel_element_index/_6_coffee_machine/0/0.txt", raw_image_filepath = "/data/home/jian/TextToActions/dataset/simulated/_2_control_panel_images/_1_selected/_6_coffee_machine/0_0.jpg", machine_type = "coffee machine", machine_id = "0", pic_id = "0", model_type = "claude")

    
   