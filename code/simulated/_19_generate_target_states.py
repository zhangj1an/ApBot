import _0_t2a_config
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code
import os 
from utils.create_or_replace_path import create_or_replace_path
import re 

def add_appliance_state(original_code_filepath, updated_code_filepath, prompt_filepath):
    prompt  = ""
    with open(prompt_filepath, "r") as f:
        prompt = f.read()
    raw_code = ""
    with open(original_code_filepath, "r") as f:
        raw_code = f.read()
    model = GPT4O()
    prompt = prompt + raw_code
    response = model.chat_with_text(prompt)
    response = extract_python_code(response)
    with open(updated_code_filepath, "w") as f:
        f.write(response)
        print(f"Updated code saved to {updated_code_filepath}")



def batch_add_appliance_state(original_code_dir, updated_code_dir, prompt_filepath):
    machine_type_dirs = [os.path.join(original_code_dir, d) for d in os.listdir(original_code_dir) if os.path.isdir(os.path.join(original_code_dir, d))]
    for machine_type_dir in machine_type_dirs:
        # list all the files in the directory
        machine_id_filepaths = [os.path.join(machine_type_dir, f) for f in os.listdir(machine_type_dir) if f.endswith(".py")]
        for machine_id_filepath in machine_id_filepaths:
            print("Processing: ", machine_id_filepath)
            relative_path = os.path.relpath(machine_id_filepath, original_code_dir)
            updated_machine_id_filepath = os.path.join(updated_code_dir, relative_path)
            create_or_replace_path(updated_machine_id_filepath)
            add_appliance_state(machine_id_filepath, updated_machine_id_filepath, prompt_filepath)
            #exit()
    pass


def generate_target_state(prompt_filepath, command_filepath, simulator_code_filepath, output_filepath, code_environment_filepath):
    prompt = ""
    with open(prompt_filepath, "r") as f:
        prompt = f.read()
    command = ""
    with open(command_filepath, "r") as f:
        command = f.read()
    simulator_code = ""
    with open(simulator_code_filepath, "r") as f:
        simulator_code = f.read()
    
    environment_code = ""
    with open(code_environment_filepath, "r") as f:
        environment_code = f.read()
    prompt = prompt.replace("xxxxx", command)
    prompt = prompt.replace("yyyyy", simulator_code)
    prompt = prompt.replace("zzzzz", environment_code)
    
    
    model = GPT4O()
    response = model.chat_with_text(prompt)
    with open(output_filepath, "w") as f:
        f.write(response)
        
        print(f"Target state saved to {output_filepath}")

    pass 

def batch_generate_instance_specific_commands_target_state(prompt_filepath, command_dir, simulator_code_dir, output_dir, code_environment_filepath):
    # list all the directories in the command directory
    command_machine_type_dir = [os.path.join(command_dir, d) for d in os.listdir(command_dir) if os.path.isdir(os.path.join(command_dir, d))]
    for machine_type_dir in command_machine_type_dir:
        # list all the files in the directory
        command_machine_id_filepaths = [os.path.join(machine_type_dir, f) for f in os.listdir(machine_type_dir) if f.endswith(".txt")]
        for command_machine_id_filepath in command_machine_id_filepaths:
            if all(s in command_machine_id_filepath for s in ["_1_washing_machine","_2_rice_cooker/_1.txt",  ]) :
                
                continue 
            if all (s not in command_machine_id_filepath for s in ["_1.txt"]):
                continue 

            print("Processing: ", command_machine_id_filepath)
            relative_path = os.path.relpath(command_machine_id_filepath, command_dir)
            
            simulator_machine_id_filepath = os.path.join(simulator_code_dir, relative_path)
            simulator_machine_id_filepath = re.sub(r'(_\d+)\.txt$', r'\1.py' ,simulator_machine_id_filepath)

            output_machine_id_filepath = os.path.join(output_dir, relative_path)
            
            create_or_replace_path(output_machine_id_filepath)
            generate_target_state(prompt_filepath, command_machine_id_filepath, simulator_machine_id_filepath, output_machine_id_filepath, code_environment_filepath)

    pass 


def batch_generate_unified_commands_target_state(prompt_filepath, command_dir, simulator_code_dir, output_dir, code_environment_filepath):
    # list all the directories in the command directory
    command_filepaths = [os.path.join(command_dir, d) for d in os.listdir(command_dir) if d.endswith(".txt")]
    #print("all options: ", command_filepaths)
    for command_filepath in command_filepaths:
        # list all the files in the directory
        relative_path = os.path.relpath(command_filepath, command_dir)

        # if >4, ignore 
        #if int(relative_path.split("_")[0]) > 3:
        #    continue
        simulator_machine_type_dir = os.path.join(simulator_code_dir, relative_path)
        simulator_machine_type_dir = simulator_machine_type_dir.replace(".txt", "")
        
        print("Processing simulator dir: ", simulator_machine_type_dir)
        # list all the files in the directory
        simulator_machine_id_filepaths = [os.path.join(simulator_machine_type_dir, f) for f in os.listdir(simulator_machine_type_dir) if f.endswith(".py")]

        for simulator_machine_id_filepath in simulator_machine_id_filepaths:
            print("Processing: ", simulator_machine_id_filepath)
            relative_path = os.path.relpath(simulator_machine_id_filepath,simulator_code_dir)
            output_machine_id_filepath = os.path.join(output_dir, relative_path)

            # replace the "_1.py" with "1.txt"
            output_machine_id_filepath = re.sub(r'(_\d+)\.py$', r'/\1.txt', output_machine_id_filepath)

            create_or_replace_path(output_machine_id_filepath)
            print("Output: ", output_machine_id_filepath)
            #exit()
            generate_target_state(prompt_filepath, command_filepath, simulator_machine_id_filepath, output_machine_id_filepath, code_environment_filepath)
            #exit()
            
        
    pass 

def format_testcases(command_filepath, target_state_filepath, output_filepath, prompt_filepath):
    # reformat the command into dictionaries
    # command_id:, command_text: target_state: important_target_state:
    # and then only retain the important variables 
    #  
    prompt = ""
    with open(prompt_filepath, "r") as f:
        prompt = f.read()
    command = ""
    with open(command_filepath, "r") as f:
        command = f.read()
    target_state = ""
    with open(target_state_filepath, "r") as f:
        target_state = f.read()
    
    prompt = prompt.replace("xxxxx", command)
    prompt = prompt.replace("yyyyy", target_state)
    #print(prompt)
    model = GPT4O()
    response = model.chat_with_text(prompt)
    response = extract_python_code(response)
    #print(response)
    with open(output_filepath, "w") as f:
        f.write(response)
        print(f"Output saved to {output_filepath}")
    

def batch_format_instance_specific_testcases(command_dir, target_state_dir, output_dir, prompt_filepath):
    # list all the directories in the command directory
    command_machine_type_dir = [os.path.join(command_dir, d) for d in os.listdir(command_dir) if os.path.isdir(os.path.join(command_dir, d))]
    for machine_type_dir in command_machine_type_dir:
        # list all the files in the directory
        command_machine_id_filepaths = [os.path.join(machine_type_dir, f) for f in os.listdir(machine_type_dir) if f.endswith(".txt")]
        for command_machine_id_filepath in command_machine_id_filepaths:
            #if "_2_washing_machine/2.txt" in command_machine_id_filepath:
            #    continue

            if all(s not in command_machine_id_filepath for s in 
            ["_1.txt"]) : # "_2_washing_machine/_1.txt"
                
                continue  

            print("Processing: ", command_machine_id_filepath)

            relative_path = os.path.relpath(command_machine_id_filepath, command_dir)
            
            target_state_machine_id_filepath = os.path.join(target_state_dir, relative_path)
            output_machine_id_filepath = os.path.join(output_dir, relative_path)
            output_machine_id_filepath = output_machine_id_filepath.replace(".txt", ".py")
            create_or_replace_path(output_machine_id_filepath)
            format_testcases(command_machine_id_filepath, target_state_machine_id_filepath, output_machine_id_filepath, prompt_filepath)
            #exit()
    pass

def batch_format_general_testcases(command_dir, target_state_dir, output_dir, prompt_filepath):
    # list all the directories in the target state directory
    target_state_machine_type_dir = [os.path.join(target_state_dir, d) for d in os.listdir(target_state_dir) if os.path.isdir(os.path.join(target_state_dir, d))]
    for machine_type_dir in target_state_machine_type_dir:
        # list all the files in the directory
        target_state_machine_id_filepaths = [os.path.join(machine_type_dir, f) for f in os.listdir(machine_type_dir) if f.endswith(".txt")]
       
        for target_state_machine_id_filepath in target_state_machine_id_filepaths:
            
            relative_path = os.path.relpath(target_state_machine_id_filepath, target_state_dir)
            
            
            command_machine_id_filepath = os.path.join(command_dir, relative_path.split("/")[0] + ".txt")

            
            #if all(s not in target_state_machine_id_filepath for s in ["_1_microwave/4"]) :
            #    continue
            
            print("Processing: ", target_state_machine_id_filepath)

            

            output_machine_id_filepath = os.path.join(output_dir, relative_path)
            output_machine_id_filepath = output_machine_id_filepath.replace(".txt", ".py")
            create_or_replace_path(output_machine_id_filepath)
            format_testcases(command_machine_id_filepath, target_state_machine_id_filepath, output_machine_id_filepath, prompt_filepath)
            #exit()
    pass




if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Generate Target States for easy testcases that are specific to an appliance instance 
    #
    #######################################
    code_environment_filepath = os.path.expanduser('~/TextToActions/code/simulated/samples/_0_logic_units.py')

    #prompt_filepath = os.path.expanduser('~/TextToActions/code/src/_6_interact_with_simulators/prompt/add_simulator_states.txt')

    prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_19_generate_target_states.txt')
    
    generate_target_state_prompt_filepath =os.path.expanduser('~/TextToActions/code/simulated/prompts/_19_generate_target_states.txt')
    format_testcases_prompt_filepath = os.path.expanduser('~/TextToActions/code/simulated/prompts/_18_format_instance_specific_testcases.txt')

    #specific_command_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_4_testcases_specific')
    specific_command_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_5_testcases/_2_testcases_var')

    simulator_code_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display')

    #specific_target_states_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_5_testcases_specific_with_target_states')

    specific_target_states_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_5_testcases/_3_testcases_var_with_target_states')
    
    #instance_specific_formatted_testcases_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_6_testcases_specific_formatted')
    instance_specific_formatted_testcases_dir = os.path.expanduser('~/TextToActions/datasetv2/real_world/_3_simulators/_5_testcases/_4_testcases_var_formatted')
    
    #batch_generate_instance_specific_commands_target_state(generate_target_state_prompt_filepath, specific_command_dir, simulator_code_dir, specific_target_states_dir, code_environment_filepath)

    batch_format_instance_specific_testcases(specific_command_dir, specific_target_states_dir, instance_specific_formatted_testcases_dir, format_testcases_prompt_filepath)
    


    #generate_target_state(prompt_filepath, "/data/home/jian/RLS_microwave/benchmark_2/metrics/command/testcases/instance_specific/2_air_purifier/2.txt", "/data/home/jian/RLS_microwave/benchmark_2/metrics/command/simulators_with_display_and_state/2_air_purifier/_2.py", "/data/home/jian/RLS_microwave/benchmark_2/metrics/command/testcases/instance_specific_target_states/2_air_purifier/2.txt")

    #######################################
    #
    # Generate Target States for HARD testcases that are specific to an appliance instance 
    #
    #######################################

    compound_command_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_1_testcases_compound')
    compound_target_states_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_2_testcases_compound_with_target_states')
    compound_formatted_testcases_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_9_testcases_compound_formatted')
    #batch_generate_instance_specific_commands_target_state(generate_target_state_prompt_filepath, compound_command_dir, simulator_code_dir, compound_target_states_dir, code_environment_filepath)

    #batch_format_instance_specific_testcases(compound_command_dir, compound_target_states_dir, compound_formatted_testcases_dir, format_testcases_prompt_filepath)



    #######################################
    #
    # Generate Target States for testcases for an appliance type
    #
    #######################################

    general_target_states_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_7_testcases_unified_with_target_states')
    general_command_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_3_testcases_unified')
    general_formatted_testcases_dir = os.path.expanduser('~/TextToActions/dataset/_3_simulators/_4_testcases/_8_testcases_unified_formatted')

    #batch_generate_unified_commands_target_state(generate_target_state_prompt_filepath, general_command_dir, simulator_code_dir, general_target_states_dir, code_environment_filepath)

    #batch_format_general_testcases(general_command_dir, general_target_states_dir, general_formatted_testcases_dir, format_testcases_prompt_filepath)
