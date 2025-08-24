# general commands regards a type of appliance.
# can generate all 15 types all at once;
# about 20 commands per type 
# metric: as long as can reach terminal state of the appliance, or declare failure, and reach reasonable goal states, declare success.

# next, generate instance specific commands. 
# about 20 commands per instance. 
# then, write the ground truth answers too. 

# then, for the instruction following task 
# give user manual, as well as the internal world model, see how the result works out. 


# then, test baseline against the entire pipeline. 
# this requires labelling of the visual grounding also.
import sys 
import os
sys.path.append("/data/home/jian/RLS_microwave/utils")
from foundation_models.gpt_4o_model import GPT4O
from utils.create_or_replace_path import create_or_replace_path


def generate_machine_instance_commands_with_all_variable_sizes(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_dir, machine_type, machine_id, variable_size):

    
    output_filepath = os.path.join(output_dir, f"{machine_type}/{machine_id}.txt")
    create_or_replace_path(output_filepath)
    generate_machine_instance_commands_with_one_variable_size(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_filepath, machine_type, variable_size)
    print(f"generated commands for {machine_type}, {machine_id}, {variable_size} variables at {output_filepath}")
        
    pass 

def generate_machine_instance_commands_with_one_variable_size(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_filepath, machine_type, variable_size):
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
    prompt = prompt.replace("yyyyy", str(variable_size))

    prompt = prompt + user_manual_text + code_environment_text + oracle_world_model_text

    response = model.chat_with_text(prompt)

    with open(output_filepath, "w") as f:
        f.write(response)
    print(f"saved commands at {output_filepath}")

def generate_machine_instance_commands_with_one_action_size(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_filepath, machine_type, action_size):
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
    prompt = prompt.replace("yyyyy", str(action_size))

    prompt = prompt + user_manual_text + code_environment_text + oracle_world_model_text

    response = model.chat_with_text(prompt)

    with open(output_filepath, "w") as f:
        f.write(response)
    print(f"saved commands at {output_filepath}")


def generate_machine_instance_commands_with_all_action_sizes(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_dir, machine_type, machine_id):

    
    for i in range(2, 14, 2):
        output_filepath = f"{output_dir}/_{i}/{machine_type}/{machine_id}.txt"
        create_or_replace_path(output_filepath)
        generate_machine_instance_commands_with_one_action_size(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_filepath, machine_type, str(i))
        print(f"generated commands for {machine_type}, {machine_id}, {i} variables at {output_filepath}")
        
        
    pass 



def batch_generate_machine_instance_commands_with_all_action_sizes(user_manual_dir, oracle_world_model_dir, code_environment_filepath, prompt_filepath, output_dir, machine_types):

    
    for machine_type in machine_types:
        user_manual_subdir = f"{user_manual_dir}/{machine_type}"
        oracle_world_model_subdir = f"{oracle_world_model_dir}/{machine_type}"

        # list all txt files in user manual directory 
        user_manual_files = os.listdir(user_manual_subdir)

        for user_manual_file in user_manual_files:
            user_manual_filepath = f"{user_manual_subdir}/{user_manual_file}"

            oracle_world_model_filename = user_manual_file.replace("txt","py")
            machine_id = user_manual_file.split(".")[0]
            oracle_world_model_filepath = f"{oracle_world_model_subdir}/{oracle_world_model_filename}"

            print(f"processing {oracle_world_model_filepath}")
            #if all(s not in oracle_world_model_filepath for s in ["_1_microwave"]) :
            #    print("skipping", oracle_world_model_filepath)
            #    continue  
            
            
            
            #output_filepath = f"{output_dir}/{machine_type}/{user_manual_file}"
            #create_or_replace_path(output_filepath)

            generate_machine_instance_commands_with_all_action_sizes(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_dir, machine_type, machine_id)

            print("Generated commands for", machine_type, user_manual_file)
            #exit()
    pass 


def batch_generate_machine_instance_commands_with_all_variable_sizes(user_manual_dir, oracle_world_model_dir, code_environment_filepath, prompt_filepath, output_dir, machine_types):

    
    for machine_type in machine_types:
        user_manual_subdir = f"{user_manual_dir}/{machine_type}"
        oracle_world_model_subdir = f"{oracle_world_model_dir}/{machine_type}"

        # list all txt files in user manual directory 
        user_manual_files = os.listdir(user_manual_subdir)

        for user_manual_file in user_manual_files:
            user_manual_filepath = f"{user_manual_subdir}/{user_manual_file}"

            oracle_world_model_filename = user_manual_file.replace("txt","py")
            machine_id = user_manual_file.split(".")[0]
            print("machine type", machine_type)
            print("machine id", machine_id)
            #if machine_type == "_2_bottle_washer" and not any(s in machine_id for s in ["1", "4"]):
            #    continue 

            #if machine_type == "_4_microwave_oven" and not any(s in machine_id for s in ["2"]):
            #    continue
            if (machine_type in ["_1_washing_machine", "_2_rice_cooker"]):
                continue
            oracle_world_model_filepath = f"{oracle_world_model_subdir}/{oracle_world_model_filename}"

            print(f"processing {oracle_world_model_filepath}")
            #if all(s not in oracle_world_model_filepath for s in ["_1_microwave"]) :
            #    print("skipping", oracle_world_model_filepath)
            #    continue  
            
            
            
            #output_filepath = f"{output_dir}/{machine_type}/{user_manual_file}"
            #create_or_replace_path(output_filepath)
            variable_size = machine_type.split("_")[1]
            if machine_type == "_3_blender":
                variable_size = "1"
            elif machine_type == "_4_water_dispenser":
                variable_size = "3"
            elif machine_type == "_5_induction_cooker": 
                variable_size = "3"
            generate_machine_instance_commands_with_all_variable_sizes(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, prompt_filepath, output_dir, machine_type, machine_id, variable_size)

            print("Generated commands for", machine_type, user_manual_file)
            #exit()
    pass 

if __name__ == "__main__":

    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #############################################
    #
    #   Generate commands with all variable sizes
    #
    #############################################

    user_manual_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text')
    oracle_world_model_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display')
    code_environment_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_0_logic_units.py')
    machine_types = ["_1_washing_machine", "_2_rice_cooker", "_3_blender", "_4_water_dispenser", "_5_induction_cooker"]#["_1_dehumidifier","_2_bottle_washer", "_3_rice_cooker", "_4_microwave_oven", "_5_bread_maker", "_6_washing_machine"]

    variable_size_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_17_testcase_v2/_1_generate_test_command_variable_size.txt')

    variable_size_output_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_5_testcases/_1_testcases_var_raw')

    batch_generate_machine_instance_commands_with_all_variable_sizes(user_manual_dir, oracle_world_model_dir, code_environment_filepath, variable_size_prompt_filepath, variable_size_output_dir, machine_types)


    user_manual_filepath = os.path.expanduser('~/TextToActions/dataset/_1_user_manual/_2_text/_2_washing_machine/_0.txt')
    oracle_world_model_filepath = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_simulators_with_states_and_display/_2_washing_machine/_0.py')
    
    output_filepath = os.path.expanduser('~/TextToActions/dataset/_7_testcases_v2/_0_variable_size/_1/_2_washing_machine/_0.txt')
    #generate_machine_instance_commands_with_one_variable_size(user_manual_filepath, oracle_world_model_filepath, code_environment_filepath, variable_size_prompt_filepath, output_filepath, "_2_washing_machine", "1")

    #############################################
    #
    #   Generate commands with all action sizes
    #
    #############################################

    action_size_prompt_filepath=os.path.expanduser('~/TextToActions/code/src/_0_cleaned_code/prompts/_17_testcase_v2/_0_generate_test_command_action_size.txt')
    action_size_output_dir=os.path.expanduser('~/TextToActions/dataset/_7_testcases_v2/_1_0_action_size_questions')

    #batch_generate_machine_instance_commands_with_all_action_sizes(user_manual_dir, oracle_world_model_dir, code_environment_filepath, action_size_prompt_filepath, action_size_output_dir, machine_types)

    """
    # only testing:
    # Washing machine: 0, 2, 3
    # Rice cooker: 0, 2, 4
    # Air purifier: 1, 2, 3
    """

    