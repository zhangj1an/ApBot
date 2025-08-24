import sys 
import os 
import json 
import copy
import re 
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.extract_python_code import extract_python_code

def matches_run_action_format(text):
    """
    Check if the provided text matches the specified run_action format.

    Args:
    text (str): The text to check against the regex pattern.

    Returns:
    bool: True if the text matches the regex pattern, False otherwise.
    """
    # can extract from the text
    # if is instance tuple or list:
    if isinstance(text, (tuple, list)):
        duration = None 
        if len(text) == 4:
            duration = text[3]
        action_type = text[0]
        bbox_index = text[1]
        execution_times = text[2]
        # check if execution times is an integer, action type is a string, and bbox index is an integer
        if isinstance(action_type, str) and isinstance(bbox_index, (int, list)) and isinstance(execution_times, int) and (duration is None or isinstance(duration, int)):
            if isinstance(bbox_index, list) and len(bbox_index) != 2:
                return False
            return True
        else:
            return False 
            pass 
    elif isinstance(text, str):
        text = extract_python_code(text)
        pattern = r"^(run_action\(\s*(['\"])([^'\"]+)\2\s*,\s*execution_times\s*=\s*(\d+)(\s*,\s*duration\s*=\s*(\d+))?\s*\)$|end)"
        return re.match(pattern, text) is not None

if __name__ == "__main__":
    # Test the function with example text
    text = "run_action('turn_power_selector_dial_clockwise', execution_times=4)"
    print(matches_run_action_format(text))  # Expected output: True
    exit()
    text = "run_action('heat_coffee', execution_times=1, duration=60)"
    print(matches_run_action_format(text))  # Expected output: True

    text = "run_action('heat_coffee', execution_times=1)"
    print(matches_run_action_format(text))  # Expected output: True

    text = "run_action('heat_coffee', execution_times=1, duration=60)  # Comment"
    print(matches_run_action_format(text))  # Expected output: True

    text = "run_action('heat_coffee', execution_times=1, duration=60, extra_param=123)"
    print(matches_run_action_format(text))  # Expected output: False

    text = "end"
    print(matches_run_action_format(text))  # Expected output: True