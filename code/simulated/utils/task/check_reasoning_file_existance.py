import os 
import json
import sys
sys.path.append(os.path.expanduser("~/TextToActions/code"))
from simulated.utils.create_or_replace_path import create_or_replace_path
def check_reasoning_file_existance(filepaths, log_record, log_record_filepath):
    # if the given file does not exists, directly return zero. 
    if not all(os.path.exists(path) for path in filepaths):
        log_record["score"] = 0
        log_record["score_comments"] = "the appliance mechanism is too complicated and cannot be modelled."

        # write the log record as a json file 
        create_or_replace_path(log_record_filepath)
        with open(log_record_filepath, 'w') as f:
            json.dump(log_record, f)
        return False 
    return True