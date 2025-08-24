import os
import sys
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.extract_python_code import extract_python_code

from simulated.utils.create_or_replace_path import create_or_replace_path
from foundation_models.gpt_4o_model import GPT4O
import io
import contextlib

def extract_control_panel_labels(gpt_model_type,observations_folderpath, machine_type, machine_id, label_filepath, control_panel_names_filepath, use_history = True):

    # if there is already such a file, directly return. 
    if use_history and os.path.exists(label_filepath):
        #print(f"extracting control panel labels files available {label_filepath}")
        return 
    prompt = """
    Attached is the list of control panel elements of the yyyyy.

    xxxxx

    Attached are photos containing different perspective of an appliance. The main purpose is to identify available variable parameters and value range of the variables represented by each control panel element. Therefore, only pay attention to control panel elements that are already listed. 
    
    For example, if the image contains dials with available variable values, please list all the legitimate values of that dial besides the dial name. An example output is :
    
    temperature dial available values: 0, 20, 40, 60, 80. 

    The image may take photo of the same dial, please condense and post-process the information to remove duplicate dials. Please note that there is usually an off / 0 option on the dial gradings, and do not miss that option. 
    
    If the image contain any buttons with a symbolic button, describe that symbol briefly besides the button name. For example: 
    
    power button - a circle with a triangle inside.
    
    Otherwise, output \"The control panel elements can be described using texts\" beside the element. 

    
    """
    print("extracting control panel labels...")
    control_panel_names = ""
    with open(control_panel_names_filepath, "r") as f:
        control_panel_names = f.read()
    prompt = prompt.replace("yyyyy", machine_type)
    prompt = prompt.replace("xxxxx", control_panel_names)
    #image_dir = os.path.join(observations_folderpath, machine_type)
    image_dir = observations_folderpath
    images = []
    # list all images in the directory
    for image in os.listdir(image_dir):
        if image.split("_")[0] == machine_id:
            images.append(os.path.join(image_dir, image))
    #print(f"images: {images}")
    
    model = GPT4O()
    response = model.chat_with_multiple_images(prompt, [images[0]], gpt_model_type)
    create_or_replace_path(label_filepath)
    
    with open(label_filepath, "w") as file:
        file.write(response)
    print(f"Control panel details saved to: {label_filepath}")
    

def batch_extract_control_panel_labels(observations_folderpath, label_folderpath, control_panel_elements_folderpath):
    os.makedirs(label_folderpath, exist_ok=True)
    def group_files_by_digit(dir_path):
        # List all files in the directory
        files = os.listdir(dir_path)
        
        # Dictionary to hold the grouped files
        digits = set()
        
        # Iterate through each file in the directory
        for file in files:
            # Split the file name at the underscore
            digit = file.split('_')[0]
            if digit.isdigit():
                digits.add(digit)
        sorted_digits = sorted(list(digits))
        return sorted_digits
    
    for root, dirs, files in os.walk(observations_folderpath):
        for machine_type in dirs:
            dir_path = os.path.join(root, machine_type)
            print(f"Directory: {dir_path}")
            digits = group_files_by_digit(dir_path)
            for machine_id in digits:
                #print(f"  Machine ID: {machine_id}")
                if not(machine_type == "_3_rice_cooker" and machine_id == "2"):
                    continue
                control_panel_elements_filepath = os.path.join(control_panel_elements_folderpath, machine_type, f"_{machine_id}.py")
                label_filepath = os.path.join(os.path.join(label_folderpath, f"{machine_type}"), f"{machine_id}.txt")
                create_or_replace_path(label_filepath)
                extract_control_panel_labels(root, machine_type, machine_id, label_filepath, control_panel_elements_filepath)
                print(f"  Panel details saved to: {label_folderpath}/{machine_type}/{machine_id}")
                
    pass 


def check_variable_format(input_string):
    # Check if the string contains "= InputString()"
    if "= InputString()" in input_string:
        return False  # Invalid
    return True  # Valid

def define_variables(gpt_model_type,proposed_actions_filepath, user_manual_filepath, observed_labels_filepath, define_variable_task_prompt_filepath, code_template_filepath, variable_list_filepath, command_string, use_history = True):
    
    if use_history and os.path.exists(variable_list_filepath):
        print("variable list files available")
        return 
    
    print("defining variables...")
    prompt = ""
    
    with open(define_variable_task_prompt_filepath, "r") as f:
        prompt = f.read()

    with open(proposed_actions_filepath, "r") as f:
        list_of_actions = f.read()
    prompt = prompt.replace("xxxxx", list_of_actions)

    with open(user_manual_filepath, "r") as f:
        user_manual = f.read()
    prompt = prompt.replace("yyyyy", user_manual)

    with open(observed_labels_filepath, "r") as f:
        observed_control_panel_info = f.read()
    prompt = prompt.replace("hhhhh", observed_control_panel_info)

    with open(code_template_filepath, "r") as f:
        code_template = f.read()
    prompt = prompt.replace("zzzzz", code_template)
    prompt = prompt.replace("uuuuu", command_string)
    
    # load prompt from file

    with open("temp_define_variable_prompt.txt", "w") as f:
        f.write(prompt)
    
    error_msg = ""
    for i in range(5):
        model = GPT4O()
        print("attempt: ", i)
        updated_prompt = prompt + "\n" + error_msg + "Please make sure your code does not have the afore mentioned errors. " +  "\n"
        variable_code = model.chat_with_text(updated_prompt, temperature=1, top_p=1, gpt_model_type = gpt_model_type)
        with open("temp.txt", "w") as f:
            f.write(updated_prompt)
        variable_code = extract_python_code(variable_code)
        #print("generated variable code: ", variable_code)

        try:
            # Combine all code into a single string
            all_code = code_template + "\n" + variable_code

            with open("test.py", "w") as f:
                f.write(all_code)

            stdout_capture = io.StringIO()
            stderr_capture = io.StringIO()

            # Redirect stdout and stderr to capture outputs
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                exec(all_code, globals())  # Execute the code

            # Write the goal state code to a file after successful execution
            create_or_replace_path(variable_list_filepath)
            with open(variable_list_filepath, "w") as f:
                f.write(variable_code)
            break
        except KeyError as ke:
            print(f"KeyError: {ke}")
            error_msg = f"Your previous response is:\n {variable_code}\n" + "KeyError: " + str(ke)
        except ValueError as ve:
            print(f"ValueError: {ve}")
            error_msg = "Your previous response is:\n {variable_code}\n" + "ValueError: " + str(ve)
        except Exception as e:
            print(f"Error occurred during execution: {e}")
            print("Stderr from exec():")
            error_msg = "Your previous response is:\n {variable_code}\n" + "Error occurred during execution: " + str(e) + "\n" 
            print(stderr_capture.getvalue())
            #exit()
    #exit()
    
    

def batch_define_variables(proposed_actions_dir = "", user_manual_dir = "", observed_labels_dir="",  variable_list_dir = "", define_variable_task_prompt_filepath = "", code_template_filepath="", have_prefix = True):   
    machine_type_dirs = [os.path.join(user_manual_dir, d) for d in os.listdir(user_manual_dir) if os.path.isdir(os.path.join(user_manual_dir, d))]
    # Washing machine: 0, 2, 3
    # Rice cooker: 0, 2, 4
    # Air purifier: 1, 2, 3
    # micorwave: 1, 2, 3
    for dir1 in machine_type_dirs:
        # List all subdirectories in each level one directory
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith(('.txt'))]
        for dir2 in machine_id_dirs:
            
            #if not ("_1_microwave" in dir1 and any(s in dir2 for s in [ "1.txt", ])): #
            #        continue
            #print("processing: ", dir2)
            # /data/home/jian/TextToActions/dataset/simulated/_1_user_manual/_2_text/_1_microwave, /data/home/jian/TextToActions/dataset/simulated/_1_user_manual/_2_text/_1_microwave/_4.txt
            machine_type = dir1.split("/")[-1]
            machine_id = dir2.split("/")[-1].split(".")[0].split("_")[-1]
            print(f"passing by: {machine_type}, {machine_id}")
            
            if machine_type == "_1_microwave" and not any(s in machine_id for s in ["1", "2", "3"]): # "0", "2", "3"
                continue
            if machine_type == "_2_washing_machine" and not any(s in machine_id for s in ["0", "2", "3"]): # "0", "2", "3"
                continue
            if machine_type == "_3_rice_cooker" and not any(s in machine_id for s in ["0", "2", "4"]): 
                continue
            if machine_type == "_4_air_purifier" and not any(s in machine_id for s in ["1", "2", "3"]):
                continue

            relative_path = os.path.relpath(dir2, user_manual_dir).replace(".txt", ".py")
            relative_path_last_file_have_prefix = relative_path.split("/")[-1]
            relative_path_last_file_no_prefix = relative_path.split("/")[-1].split("_")[1]

            relative_path_dir = "/".join(relative_path.split("/")[:-1])

            if have_prefix:
                proposed_actions_filepath = os.path.join(proposed_actions_dir, relative_path_dir, relative_path_last_file_have_prefix).replace(".py", ".txt")
                save_variable_list_filepath = os.path.join(variable_list_dir, relative_path_dir, relative_path_last_file_have_prefix)
                
            else:
                proposed_actions_filepath = os.path.join(proposed_actions_dir, relative_path_dir, relative_path_last_file_no_prefix) 
            
                save_variable_list_filepath = os.path.join(variable_list_dir, relative_path_dir, relative_path_last_file_no_prefix)
            observed_labels_filepath = os.path.join(observed_labels_dir, relative_path_dir, relative_path_last_file_no_prefix).replace(".py", ".txt")
            create_or_replace_path(save_variable_list_filepath)
            define_variables(proposed_actions_filepath, dir2,observed_labels_filepath, define_variable_task_prompt_filepath, code_template_filepath, save_variable_list_filepath )




if __name__ == "__main__":

    # srun -u -o "log.out" -w crane1 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Extract variable details by observing control panel images
    #
    #######################################

    control_panel_elements_folderpath = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_3_extracted_control_panel_element_names')

    observations_folderpath = os.path.expanduser('~/TextToActions/dataset/simulated/_2_control_panel_images/_0_raw')
    
    observed_labels_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_7_extracted_control_panel_labels')
    
    #batch_extract_control_panel_labels(observations_folderpath, observed_labels_dir, control_panel_elements_folderpath)

    #########################################
    #
    # Define Variables given Oracle Actions
    #
    #########################################

    code_template_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_1_variables.py')

    oracle_actions_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_3_simulators/_1_oracle_available_actions')

    user_manual_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_2_text')

    define_variable_task_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_14_define_variables.txt')

    variable_list_for_oracle_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_0_proposed_variables_for_oracle_grounding')

    # define variables for oracle grounding
    #batch_define_variables(oracle_actions_dir, user_manual_dir, observed_labels_dir, variable_list_for_oracle_grounding_dir, define_variable_task_prompt_filepath, code_template_filepath, have_prefix= True)

    #########################################
    #
    # Define Variables given Proposed Actions
    #
    #########################################

    #proposed_actions_filepath = os.path.expanduser('~/TextToActions/dataset/_4_proposed_action_names/1_air_fryer/0.txt")
    #user_manual_filepath = os.path.expanduser('~/TextToActions/dataset/_1_user_manual/_2_text/1_air_fryer/0.txt")
    #observed_labels_filepath = os.path.expanduser('~/TextToActions/dataset/control_panel_images_extracted_labels/1_air_fryer/0.txt")

    variable_list_for_proposed_grounding_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_5_reasoning/_1_proposed_variables_for_proposed_grounding')

    proposed_actions_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_1_action_names/_1_proposed_action_names')

    # define variables for proposed grounding
    batch_define_variables(proposed_actions_dir, user_manual_dir, observed_labels_dir, variable_list_for_proposed_grounding_dir, define_variable_task_prompt_filepath, code_template_filepath)
    
    

    