import os
import sys
import re
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.load_string_from_file import load_string_from_file, load_string_from_files
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code


def check_state_reached(gpt_model_type,mismatch_prompt_filepath, model_code_filepaths, distill_prompt_filepath, goal_state_string, real_world_feedback, command_string, verbose = False ):
    print(f"check state....")
    model = GPT4O()
    distill_prompt = load_string_from_file(distill_prompt_filepath)
    model_code = load_string_from_files(model_code_filepaths)
    distill_prompt = distill_prompt.replace("xxxxx", model_code)
    distill_prompt = distill_prompt.replace("hhhhh", real_world_feedback)
    distill_prompt = distill_prompt.replace("wwwww", goal_state_string)
    distill_prompt = distill_prompt.replace("yyyyy", command_string)
    response = model.chat_with_text(distill_prompt, temperature=0, top_p=1, gpt_model_type = gpt_model_type)
    response = response.lower()

    print(f"Feedback Variable: \n\n {response} \n\n")
    #with open("temp.txt", "w") as f:
    #    f.write(distill_prompt)
    #if 'steam' in real_world_feedback:
    #    exit()

    goal_code = load_string_from_file("temp_goal.py")

    
    mismatch_prompt = load_string_from_file(mismatch_prompt_filepath)
    mismatch_prompt = mismatch_prompt.replace("wwwww", goal_state_string)
    mismatch_prompt = mismatch_prompt.replace("hhhhh", response)
    mismatch_prompt = mismatch_prompt.replace("yyyyy", goal_code)
    #mismatch_prompt = mismatch_prompt.replace("yyyyy", generated_variable_code)

    with open("temp_check_mismatch.txt", "w") as f:
        f.write(mismatch_prompt)
    #if "steam" in response:
    #    exit()
    MAX_RETRIES = 3
    attempt = 0
    mismatch_ns = {}

    while attempt < MAX_RETRIES:
        try:
            model = GPT4O()
            response = model.chat_with_text(mismatch_prompt, temperature=0.5, top_p=1, gpt_model_type = gpt_model_type)
            response = extract_python_code(response)
            
            print(f"Comparison result: \n\n {response} \n\n")
            #exit()
            exec(response, mismatch_ns)  # Attempt execution
            
            goal_reached = mismatch_ns.get('goal_reached', None)
            reason = mismatch_ns.get('reason', None)
            
            if goal_reached != False and goal_reached != True:
                raise Exception("no meaningful goal_reached answer returned")
            # If execution is successful, break out of the loop
            break  
        except Exception as e:
            print(f"Execution failed on attempt {attempt + 1}: {e}")
            attempt += 1
            mismatch_ns = {}  # Reset namespace before retrying

    if attempt == MAX_RETRIES:
        print("Failed after 3 attempts.")
        return False, "Failed to check whether state reached, GPT cannot generate valid response"

    if verbose: 
        print(f"prompt: \n\n {mismatch_prompt} \n\n")
        print(f"response: \n\n {response} \n\n")

    with open("temp_check_mismatch.txt", "w") as f:
        f.write(mismatch_prompt)
    #print(f"response: \n\n {response} \n\n")
    if goal_reached:
        return True, reason
    else:
        return False, reason
    return None