feature_list = {}

# Feature: Turn on and start the appliance
feature_list["start_appliance"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Feature: Activate cooking time adjustment and adjust times (unified feature)
feature_list["adjust_cooking_time"] = [
    {"step": 1, "actions": ["press_cooking_time_button"]},
    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_cooking_time_hr"},
    {"step": 3, "actions": ["press_min_button"], "variable": "variable_cooking_time_min"}
]

# Feature: Activate preset time setting and set times (unified feature)
feature_list["set_preset_time"] = [
    {"step": 1, "actions": ["press_preset_timer_button"]},
    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_preset_time_hr"},
    {"step": 3, "actions": ["press_min_button"], "variable": "variable_preset_time_min"}
]

# Feature: Selecting a cooking mode (menu)
feature_list["set_cooking_mode"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_cooking_mode"}
]

# Feature: Selecting the rice type
feature_list["set_rice_type"] = [
    {"step": 1, "actions": ["press_white_button", "press_brown_rice_button"], "variable": "variable_rice_type"}
]

# Feature: Cancel operation or switch to Keep Warm
feature_list["cancel_or_keep_warm"] = [
    {"step": 1, "actions": ["press_keep_warm_cancel_button"], "variable": "variable_keep_warm_cancel"}
]

# Null feature for unused actions/variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))