# here should give an example from both sides of the format


def compare_ground_truth(ground_truth_dict, appliance_current_state):

    for key in ground_truth_dict.keys():
        # Check if the key exists in appliance_current_state
        if key not in appliance_current_state:
            return 0, f"{key} is not modelled in oracle simulator, this should not happen, code has bug"
        
        # Check if the value in ground_truth_dict is a list
        if isinstance(ground_truth_dict[key], list):
            try:
                # Try converting appliance_current_state[key] to float
                machine_value = float(appliance_current_state[key])
                # Try converting all list items to floats
                ground_truth_values = [float(value) for value in ground_truth_dict[key]]
                # Check if the machine value is in the converted list
                if machine_value not in ground_truth_values:
                    return 0, (f"for the variable {key}, the value decided by the robot is {appliance_current_state[key]} "
                            f"(type: {type(appliance_current_state[key])}), but the ground truth is {ground_truth_dict[key]} "
                            f"(type: {type(ground_truth_dict[key])})")
            except (ValueError, TypeError):
                # If float conversion fails, fall back to string comparison
                if str(appliance_current_state[key]) not in ground_truth_dict[key]:
                    return 0, (f"for the variable {key}, the value decided by the robot is {appliance_current_state[key]} "
                            f"(type: {type(appliance_current_state[key])}), but the ground truth is {ground_truth_dict[key]} "
                            f"(type: {type(ground_truth_dict[key])})")
        else:
            # If it's a single value, attempt to compare as floats
            try:
                machine_value = float(appliance_current_state[key])
                ground_truth_value = float(ground_truth_dict[key])
                if machine_value != ground_truth_value:
                    return 0, (f"for the variable {key}, the value decided by the robot is {appliance_current_state[key]} "
                            f"(type: {type(appliance_current_state[key])}), but the ground truth is {ground_truth_dict[key]} "
                            f"(type: {type(ground_truth_dict[key])})")
            except (ValueError, TypeError):
                # If float conversion fails, fall back to string comparison
                if (str(ground_truth_dict[key]) != str(appliance_current_state[key])) and ground_truth_dict[key] != "any":
                    return 0, (f"for the variable {key}, the value decided by the robot is {appliance_current_state[key]} "
                            f"(type: {type(appliance_current_state[key])}), but the ground truth is {ground_truth_dict[key]} "
                            f"(type: {type(ground_truth_dict[key])})")
    return 1, "everything is correct"

def generate_score(appliance_current_state, testcase_info):
#def generate_score(testcase_info, appliance_current_state):
    print("ground truth info", testcase_info)
    print("robot's decision", appliance_current_state)

    ground_truth_dict = testcase_info["important_target_states"]
    # if the ground truth is a list :
    if isinstance(ground_truth_dict, list):
        for ground_truth in ground_truth_dict:
            score, message = compare_ground_truth(ground_truth, appliance_current_state)
            if score == 1:
                return score, message
        return 0, f"the allowed ground truth states include {ground_truth_dict}, but the robot's decision is {appliance_current_state}. It does not match any of the allowed states."
    if isinstance(ground_truth_dict, dict):
        score, message = compare_ground_truth(ground_truth_dict, appliance_current_state)
        return score, message
    

