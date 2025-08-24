feature_list = {}

# Feature for turning on/off the power
feature_list["power"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Feature for starting operation
feature_list["start_operation"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Feature for adjusting water level
feature_list["adjust_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level"}
]

# Feature for setting child lock
feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_program_button"], "variable": "variable_child_lock"}
]

# Feature for setting preset timer
feature_list["set_preset_timer"] = [
    {"step": 1, "actions": ["press_preset_button"], "variable": "variable_preset_timer"}
]

# Feature for changing process setting (wash/rinse/spin)
feature_list["change_process_setting"] = [
    {"step": 1, "actions": ["press_process_button"], "variable": "variable_process_setting"}
]

# Feature for selecting program
feature_list["select_program"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program_selection"}
]

# Null feature for unused actions or variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))