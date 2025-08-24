from openai import OpenAI
import os
import re
import _0_t2a_config
from utils.create_or_replace_path import create_or_replace_path
from foundation_models.gpt_4o_model import GPT4O 
from utils.load_string_from_file import load_string_from_file
from utils.extract_python_code import extract_python_code


# save text to a text file
def save_text(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)


def format_control_element_names(input_string):
    """
    Validates the format of each line in the given multiline string.
    Requirements:
    - Each line must contain an underscore "_", lowercase alphabets, and numbers only.
    - Each line must end with "_button" or "_dial".
    
    Args:
        input_string (str): The multiline string to validate.
    
    Returns:
        None: If all lines pass validation.
    
    Raises:
        ValueError: With an error message indicating the failed line and reason.
    """
    # Split input string into lines, strip empty lines and trailing spaces
    lines = [line.strip() for line in input_string.splitlines() if line.strip()]
    
    # Regular expression to validate each line
    pattern = re.compile(r"^[a-z0-9_]+_(button|dial)$")
    
    for i, line in enumerate(lines, start=1):
        if not pattern.match(line):
            raise ValueError(f"'{line}' does not match the required format: the name can only contain lower case alphabet, numbers and the underscore '_' symbol. The name must either end with '_button' or '_dial'.")
    
    return "All lines are valid!"

def extract_control_panel_elements(user_manual_file, control_panel_elements_file,  propose_control_panel_prompt_filepath, filter_control_panel_prompt_filepath, image_filepath, gpt_model_type):
    user_manual_text = load_string_from_file(user_manual_file)


    propose_control_panel_prompt = load_string_from_file(propose_control_panel_prompt_filepath)

    filter_control_panel_prompt = load_string_from_file(filter_control_panel_prompt_filepath)
    #print(user_manual_text, flush=True)
    #print(propose_control_panel_prompt, flush=True)
    #exit()
    error_msg = ""
    answer = ""
    for i in range(3):
        try:
            model = GPT4O()
            updated_prompt = user_manual_text + "\n" + propose_control_panel_prompt + "\n" + error_msg
            #if i == 0:
            #    print(updated_prompt, flush=True)
            answer = model.chat(updated_prompt, image_filepath, temperature=0, top_p=1,gpt_model_type=gpt_model_type)
            
            #format_control_element_names(answer)
            # check format, each line must all have underscore, alphabet and number only; each line must end with button or dial.
            break
        except Exception as e: 
            error_msg = "In your previous attempt, the following error was found: " + str(e) + '\n' +  "Please correct the error and try again."
            print(error_msg, flush=True)
            pass 


    print("Answer: ", answer, flush=True)
    #filter_control_panel_prompt = filter_control_panel_prompt.replace("xxxxx", user_manual_text)
    #filter_control_panel_prompt = filter_control_panel_prompt.replace("yyyyy", answer)
    #model = GPT4O()
    #answer = model.chat(filter_control_panel_prompt, image_filepath)
    answer = extract_python_code(answer)
    #print(f"after filtering: \n{answer}\n", flush=True)


    save_text(control_panel_elements_file, answer)

def batch_process_extract_control_panel_elements(user_manual_folder_path, panel_elements_from_user_manual_path, propose_control_panel_prompt_filepath, filter_control_panel_prompt_filepath, control_panel_image_folder_path, gpt_model_type):
    machine_type_dirs = [os.path.join(user_manual_folder_path, d) for d in os.listdir(user_manual_folder_path) if os.path.isdir(os.path.join(user_manual_folder_path, d))]
    

    for dir1 in machine_type_dirs:
        
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith(".txt")]
        machine_type = dir1.split("/")[-1]
        for dir2 in machine_id_dirs:
            print("Processing: ", dir1 , flush=True)
            if any(item in dir1 for item in ["_1_washing_machine", "_2_rice_cooker"]):
                continue
            #if not any(item in dir2 for item in ["_2_bottle_washer/_1.txt", "_2_bottle_washer/_4.txt", "_4_microwave_oven/_2.txt"]):
            #    continue
            print("Processing: ", dir2 , flush=True)
            machine_id = dir2.split("/")[-1].split(".")[0].split("_")[-1]
            relative_path = os.path.relpath(dir2, user_manual_folder_path)
            save_text_dir = os.path.join(panel_elements_from_user_manual_path, relative_path).replace(".txt", ".py")
            
            image_folder = os.path.join(control_panel_image_folder_path, machine_type)
            # image path is the file in the folder that starts with {machine_id}
            
            a = [os.path.join(image_folder, f) for f in os.listdir(image_folder)]
            
            image_filepath = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.startswith(machine_id)][0]
            create_or_replace_path(save_text_dir)
            extract_control_panel_elements(dir2, save_text_dir,  propose_control_panel_prompt_filepath, filter_control_panel_prompt_filepath, image_filepath, gpt_model_type)
            

if __name__ == "__main__":

     # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Extract Control Panel Element Names
    #
    #######################################

    propose_control_panel_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_2_extract_control_panel_element.txt')
    filter_control_panel_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_2_filter_control_panel_element.txt')

    gpt_model_type = "gpt-4o-2024-11-20"
    user_manual_folder_path = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text')
    panel_elements_from_user_manual_path = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_1_user_manual/_3_extracted_control_panel_element_names/{gpt_model_type}')
    control_panel_image_folder_path = os.path.expanduser('~/TextToActions/datasetv2/real_world/_2_control_panel_images/_1_selected')
    batch_process_extract_control_panel_elements(user_manual_folder_path, panel_elements_from_user_manual_path, propose_control_panel_prompt_filepath, filter_control_panel_prompt_filepath, control_panel_image_folder_path, gpt_model_type)