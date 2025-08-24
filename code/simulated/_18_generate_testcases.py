import sys 
import os
sys.path.append("/data/home/jian/RLS_microwave/utils")
from foundation_models.gpt_4o_model import GPT4O
from utils.create_or_replace_path import create_or_replace_path

def generate_machine_type_commands(user_manual_subdir, oracle_world_model_subdir, code_environment_filepath, prompt_filepath, output_dir, machine_type):
    context_text = ""

    user_manual_files = os.listdir(user_manual_subdir)
    for user_manual_file in user_manual_files:
        user_manual_filepath = f"{user_manual_subdir}/{user_manual_file}"

        oracle_world_model_filename = user_manual_file.replace("txt","py")
        oracle_world_model_filepath = f"{oracle_world_model_subdir}/{oracle_world_model_filename}"

        user_manual_text = ""
        with open(user_manual_filepath, "r") as f:
            user_manual_text = f.read()

        context_text += user_manual_text

    output_filepath = f"{output_dir}/{machine_type}.txt"
    create_or_replace_path(output_filepath)
    print(f"processing {machine_type}")
    prompt = ""
    with open(prompt_filepath, "r") as f:
        prompt = f.read()
    model = GPT4O()
    prompt = prompt.replace("xxxxx", machine_type)
    prompt = prompt.replace("yyyyy", context_text)
    response = model.chat_with_text(prompt)
    with open(output_filepath, "w") as f:
        f.write(response)
    print(f"saved commands at {output_filepath}")
    pass

def batch_generate_machine_type_commands(user_manual_dir, oracle_world_model_dir, code_environment_filepath, prompt_filepath, output_dir, machine_types):

    for machine_type in machine_types:
        user_manual_subdir = f"{user_manual_dir}/{machine_type}"
        oracle_world_model_subdir = f"{oracle_world_model_dir}/{machine_type}"

        # list all txt files in user manual directory 

        generate_machine_type_commands(user_manual_subdir, oracle_world_model_subdir, code_environment_filepath, prompt_filepath, output_dir, machine_type)

        print("Generated commands for", machine_type)


def generate_machine_instance_commands(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_filepath, machine_type):
    # get user manual, world model, code environment, 
    # generate command that this appliance can specfically execute and can be tested by our simulator.
    user_manual_text = ""
    with open(user_manual_filepath, "r") as f:
        user_manual_text = f.read()
    code_environment_text = ""
    with open(code_environment_filepath, "r") as f:
        code_environment_text = f.read()
    oracle_world_model_text = ""
    with open(oracle_world_model_filepath, "r") as f:
        oracle_world_model_text = f.read()
    
    model = GPT4O()
    prompt = ""
    with open(prompt_filepath, "r") as f:
        prompt = f.read()
    
    prompt = prompt.replace("xxxxx", machine_type)

    prompt = prompt + user_manual_text + code_environment_text + oracle_world_model_text

    response = model.chat_with_text(prompt)

    with open(output_filepath, "w") as f:
        f.write(response)
    print(f"saved commands at {output_filepath}")

def batch_generate_machine_instance_commands(user_manual_dir, oracle_world_model_dir, code_environment_filepath, prompt_filepath, output_dir, machine_types):

    
    for machine_type in machine_types:
        user_manual_subdir = f"{user_manual_dir}/{machine_type}"
        oracle_world_model_subdir = f"{oracle_world_model_dir}/{machine_type}"

        # list all txt files in user manual directory 
        user_manual_files = os.listdir(user_manual_subdir)

        for user_manual_file in user_manual_files:
            user_manual_filepath = f"{user_manual_subdir}/{user_manual_file}"

            oracle_world_model_filename = user_manual_file.replace("txt","py")
            oracle_world_model_filepath = f"{oracle_world_model_subdir}/{oracle_world_model_filename}"

            print(f"processing {oracle_world_model_filepath}")
            #if all(s not in oracle_world_model_filepath for s in ["_1_microwave"]) :
            #    print("skipping", oracle_world_model_filepath)
            #    continue  

            output_filepath = f"{output_dir}/{machine_type}/{user_manual_file}"
            create_or_replace_path(output_filepath)

            generate_machine_instance_commands(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_filepath, machine_type)

            print("Generated commands for", machine_type, user_manual_file)
            #exit()
    pass 

if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Generate User Instruction specific to appliance instance and has explicit target values, and is easy
    #
    #######################################
    user_manual_dir = os.path.expanduser('~/TextToActions/dataset/_1_user_manual/_2_text')
    oracle_world_model_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_3_simulators_with_states_and_display')
    code_environment_filepath = os.path.expanduser('~/TextToActions/code/src/_0_logic_units.py')
    machine_types = ["_1_microwave", "_2_washing_machine", "_3_rice_cooker", "_4_air_purifier"]
    
    specific_output_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_4_testcases_specific')
    
    specific_prompt_filepath = os.path.expanduser('~/TextToActions/code/src/prompts/_14_generate_test_command_specific.txt')



    #batch_generate_machine_instance_commands(user_manual_dir, oracle_world_model_dir, code_environment_filepath, specific_prompt_filepath, specific_output_dir, machine_types)

    #######################################
    #
    # Generate User Instruction specific to appliance instance and has explicit target values, and is hard due to multiple adjusting variables
    #
    #######################################

    compound_prompt_filepath = os.path.expanduser('~/TextToActions/code/src/prompts/_14_generate_test_command_compound.txt')

    compound_output_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_1_testcases_compound')

    batch_generate_machine_instance_commands(user_manual_dir, oracle_world_model_dir, code_environment_filepath, compound_prompt_filepath, compound_output_dir, machine_types)

    #######################################
    #
    # Generate User Instruction regarding an appliance type and has ambiguous target values
    #
    #######################################
    general_prompt_filepath = os.path.expanduser('~/TextToActions/code/src/prompts/_14_generate_test_command_general.txt')
    general_output_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_3_testcases_unified')
    #batch_generate_machine_type_commands(user_manual_dir, oracle_world_model_dir, code_environment_filepath,  general_prompt_filepath, general_output_dir, machine_types)
    