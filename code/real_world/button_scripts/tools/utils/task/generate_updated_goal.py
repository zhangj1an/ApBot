import os
import sys
import re
import io 
import contextlib
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.load_string_from_file import load_string_from_file, load_string_from_files
from foundation_models.gpt_4o_model import GPT4O
from simulated.utils.extract_python_code import extract_python_code
import warnings

def remove_lines_containing_phrase(input_text, phrase):
    """
    Removes lines containing a specific phrase from a multiline string.

    Args:
        input_text (str): The input multiline string.
        phrase (str): The phrase to search for.

    Returns:
        str: The modified multiline string with the specified lines removed.
    """
    # Define the regex pattern to match entire lines containing the phrase
    pattern = rf'^.*{re.escape(phrase)}.*$'
    # Use re.sub to replace matching lines with an empty string
    result = re.sub(pattern, '', input_text, flags=re.MULTILINE)
    # Remove any extra blank lines introduced by the replacement
    result = '\n'.join([line for line in result.splitlines() if line.strip()])
    return result

def generate_updated_goal(gpt_model_type,updated_simulator_entire_environment_filepaths, calibrated_code_filepaths, goal_state_code, variable_name, command_string, update_goal_prompt_filepath, generate_goal_prompt_filepath, updated_goal_state_filepath, verbose = False):
    prompt = load_string_from_file(update_goal_prompt_filepath)
    updated_simulator_entire_environment_code = load_string_from_files(updated_simulator_entire_environment_filepaths)
    calibrated_code = load_string_from_files(calibrated_code_filepaths)
    goal_generation_format = load_string_from_file(generate_goal_prompt_filepath)

    pattern = r"\$\$\$(.*)"  # Use a capturing group for the content

    # Use re.search with the re.DOTALL flag
    match = re.search(pattern, goal_generation_format, re.DOTALL)
    if match:
        result = match.group()  # Extract the matched text
        print(f"Located Var Format")
    else:
        result = "Sorry, the text is not available"
    prompt = prompt.replace("rrrrr", result)


    prompt = prompt.replace("xxxxx", calibrated_code)
    prompt = prompt.replace("zzzzz", goal_state_code)
    prompt = prompt.replace("yyyyy", variable_name)
    prompt = prompt.replace("wwwww", command_string)
    
    if verbose:
        print(f"Prompt: {prompt}")
    error_msg = ""
    for i in range(3):
        model = GPT4O()
        updated_prompt = prompt + "\n" + error_msg
        response = model.chat_with_text(updated_prompt, temperature=1, top_p=1, gpt_model_type=gpt_model_type)
        
        response = extract_python_code(response)
        try:
            print(f"Attempt to update goal: round {i + 1}")
            trimmed_goal_state_code = remove_lines_containing_phrase(goal_state_code, f"goal_state.{variable_name}")
            all_code = updated_simulator_entire_environment_code + "\n" + trimmed_goal_state_code + "\n" + response

            with open("test.py", "w") as f:
                f.write(all_code)

            stdout_capture = io.StringIO()
            stderr_capture = io.StringIO()

            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")  # catch all warnings

                # Redirect stdout and stderr to capture outputs
                with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                    exec(all_code, globals())  # Execute the code

                # Raise error if any warnings were caught
                if w:
                    warning_msg = f"Warning triggered: {w[0].message}"
                    raise ValueError(warning_msg)

            feature_sequence = globals().get('feature_sequence', None)
            feature_list = globals().get('feature_list', None)

            if feature_sequence is None:
                raise ValueError("feature_sequence not found in the global scope.")
            if feature_list is None:
                raise ValueError("feature_list not found in the global scope.")

            for feature in feature_sequence:
                if feature not in feature_list:
                    raise KeyError(f"Feature '{feature}' not found in feature_list")

            with open("temp_goal.py", "w") as f:
                f.write(trimmed_goal_state_code + "\n" + response)
            with open(updated_goal_state_filepath, "w") as f:
                f.write(trimmed_goal_state_code + "\n" + response)

            print(f"Goal state updated successfully and saved to temp_goal.py.")
            return response

        except KeyError as ke:
            error_msg = f"Your previous attempt to modify {variable_name} has the following result: \n{response}\nThis results in an error: {ke}. Please correct the error and try again."
            print(error_msg)

        except ValueError as ve:
            error_msg = f"Your previous attempt to modify {variable_name} has the following result: \n{response}\nThis results in an error: {ve}. Please correct the error and try again."
            print(error_msg)

        except Exception as e:
            print(stderr_capture.getvalue())
            error_msg = f"Your previous attempt to modify {variable_name} has the following result: \n{response}\nThis results in an error: {e}. Please correct the error and try again."
            print(error_msg)
                #exit()
        #exit()
    # if it raises error, then generate again.
    return None

