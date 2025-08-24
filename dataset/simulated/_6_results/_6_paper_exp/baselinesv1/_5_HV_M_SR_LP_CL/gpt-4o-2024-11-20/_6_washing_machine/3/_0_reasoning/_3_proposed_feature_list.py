feature_list = {}

# Feature for water level adjustment
feature_list["adjust_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level"}
]

# Feature for preset timer
feature_list["adjust_preset_timer"] = [
    {"step": 1, "actions": ["press_preset_button"], "variable": "variable_preset_timer"}
]

# Feature for process setting adjustment
feature_list["adjust_process_setting"] = [
    {"step": 1, "actions": ["press_process_button"], "variable": "variable_process_setting"}
]

# Feature for program selection
feature_list["select_program"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program_selection"}
]

# Feature for starting operation
feature_list["start_operation"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Feature for toggling power on/off
feature_list["toggle_power"] = [
    {"step": 1, "actions": ["press_power_button", "press_and_hold_power_button"], "variable": "variable_power_on_off"}
]

# Feature for child lock
feature_list["set_child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_program_button"], "variable": "variable_child_lock"}
]

# Feature for manually rotating the tub
feature_list["manual_rotate_tub"] = [
    {"step": 1, "actions": ["turn_tub_dial_clockwise"]}
]

# Feature for holding start/pause button (if this is a dedicated action apart from the normal press)
feature_list["hold_start_pause"] = [
    {"step": 1, "actions": ["press_and_hold_start_pause_button"]}
]

# Null feature to capture unused variables and actions
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))