feature_list = {}

feature_list["power_and_start_warming"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "comment": "variable_start_running: set to on"}
]

feature_list["adjust_night_light"] = [
    {"step": 1, "actions": ["press_and_hold_power_button"], "variable": "variable_night_light"}
]

feature_list["select_bottle_type"] = [
    {"step": 1, "actions": ["press_bottle_button"], "variable": "variable_bottle_type"}
]

feature_list["select_initial_temperature"] = [
    {"step": 1, "actions": ["press_initial_temp_button"], "variable": "variable_initial_temp"}
]

feature_list["select_volume"] = [
    {"step": 1, "actions": ["press_volume_button"], "variable": "variable_volume"}
]

feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))