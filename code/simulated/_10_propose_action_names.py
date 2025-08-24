
import os 
import json
import _0_t2a_config
#from foundation_models.llamaindex_llama3 import load_model, load_documents, make_inference
from foundation_models.gpt_4o_model import GPT4O
from utils.create_or_replace_path import create_or_replace_path
from utils.load_string_from_file import load_string_from_file
import re 

def convert_action_string_to_set(multiline_string):
    """
    Converts a multiline string into a set of unique action strings,
    removing any content inside parentheses along with surrounding spaces.
    
    Args:
        multiline_string (str): The input multiline string.
        
    Returns:
        set: A set of unique action strings without bracketed content.
    """
    def clean_line(line):
        return re.sub(r"\s*\(.*?\)", "", line).strip()  # Remove brackets + trim spaces
    
    return {clean_line(line) for line in multiline_string.split("\n") if line.strip()}


def define_action_names(user_manual_filepath, visually_grounded_elements_filepath, propose_action_prompt_filepath, filter_action_prompt_filepath,proposed_actions_filepath, gpt_model_type):
    # load user manual file 
    user_manual_text = load_string_from_file(user_manual_filepath)

    # load grounded elements from filepath
    with open(visually_grounded_elements_filepath, "r") as f:
        json_list = json.load(f)
    # read all the element names from this list 
    grounded_element_prompt = [item['element_name'] for item in json_list]
    grounded_element_prompt = ", ".join(grounded_element_prompt) + "\n"

    propose_action_prompt = load_string_from_file(propose_action_prompt_filepath)

    first_round_prompt = grounded_element_prompt + propose_action_prompt + user_manual_text

    action_set = set()
    for i in range(5):
        model = GPT4O()
        response = model.chat_with_text(first_round_prompt, gpt_model_type=gpt_model_type)
        action_set.update(convert_action_string_to_set(response))
        print(f"current action set: {action_set}\n")
        del model
    
    # model update with the given action set 
    model = GPT4O()
    consolidation_prompt = first_round_prompt + "\n Currently, the available options are as follows: \n" + "\n".join(action_set) + "\n Some of it might be duplicates. Please consolidate the actions into a single list." 
    response = model.chat_with_text(consolidation_prompt, gpt_model_type=gpt_model_type)

    """
    # the effect of filtering redundant actions is minimal. Error is mostly caused by redundant element names. 
    model = GPT4O()
    filter_action_prompt = load_string_from_file(filter_action_prompt_filepath)
    filter_action_prompt = filter_action_prompt.replace("xxxxx", response)
    filter_action_prompt = filter_action_prompt.replace("yyyyy", user_manual_text)
    filter_action_prompt = filter_action_prompt.replace("zzzzz", grounded_element_prompt)
    response = model.chat_with_text(filter_action_prompt)
    """
    # save response into designated filepath
    #with open("temp.txt", "w") as f:
    #    f.write(first_round_prompt)
    with open(proposed_actions_filepath, "w") as f:
        f.write(response)
        print(f"Executable actions saved to {proposed_actions_filepath}")
    
    return response 


def batch_define_action_names(user_manual_root_dir, visually_grounded_elements_root_dir, propose_action_prompt_filepath, filter_action_prompt_filepath, proposed_actions_root_dir, gpt_model_type):
    # list all files in the user manual root dir
    machine_type_dirs = [os.path.join(user_manual_root_dir, d) for d in os.listdir(user_manual_root_dir) if os.path.isdir(os.path.join(user_manual_root_dir, d))]

    for dir1 in machine_type_dirs:
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith(".txt")]
        
        
        for user_manual_filepath in machine_id_dirs:
            if any(substring in user_manual_filepath for substring in ["_1_washing_machine/_1.txt", "_2_rice_cooker/_1.txt"]):
                continue
            print("processing: ", user_manual_filepath)
            machine_type, machine_id = user_manual_filepath.split("/")[-2:]
            machine_id = machine_id.split(".")[0].split("_")[-1]
            visually_grounded_elements_filepath = os.path.join(visually_grounded_elements_root_dir, f"{machine_type}/{machine_id}.json")
            proposed_actions_filepath = os.path.join(proposed_actions_root_dir, f"{machine_type}/_{machine_id}.txt")
            create_or_replace_path(proposed_actions_filepath)
            define_action_names(user_manual_filepath, visually_grounded_elements_filepath, propose_action_prompt_filepath, filter_action_prompt_filepath, proposed_actions_filepath, gpt_model_type)
            #exit()
    pass

if __name__ == "__main__":

    # srun -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name "vlm" python3

    #######################################
    #
    # Extract Action Names from User Manual
    #
    #######################################
    user_manual_filepath = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text')

    gpt_model_type = "gpt-4o-2024-11-20"

    visually_ground_elements_filepath = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_0_control_panel_element_bbox/_3_proposed_control_panel_element_bbox')

    propose_action_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_10_create_action_names.txt')

    filter_action_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_10_filter_action_names.txt')

    proposed_actions_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_4_visual_grounding/{gpt_model_type}/_1_action_names/_1_proposed_action_names')

    batch_define_action_names(user_manual_filepath, visually_ground_elements_filepath, propose_action_prompt_filepath, filter_action_prompt_filepath, proposed_actions_root_dir, gpt_model_type)

    #######################################
    # generate ground truth action bbox for CoT baselines 
    #######################################
    # # given a list of ground truth actions, map it to a tuple of ([bbox index], action type) 
    proposed_actions_root_dir = ""
