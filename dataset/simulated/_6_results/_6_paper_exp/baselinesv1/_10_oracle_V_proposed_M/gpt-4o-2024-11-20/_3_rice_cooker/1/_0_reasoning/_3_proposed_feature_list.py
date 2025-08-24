feature_list = {}

# Feature to select different menu options
feature_list["select_menu_option"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

# Feature to set preset timer
feature_list["set_preset_timer"] = [
    {"step": 1, "actions": ["press_preset_timer_button"]},
    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_preset_timer_hours"},
    {"step": 3, "actions": ["press_min_button"], "variable": "variable_preset_timer_minutes"}
]

# Feature to set cooking time
feature_list["set_cooking_time"] = [
    {"step": 1, "actions": ["press_cooking_time_button"]},
    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_cooking_time_hours"},
    {"step": 3, "actions": ["press_min_button"], "variable": "variable_cooking_time_minutes"}
]

# Feature to select white rice cooking mode
feature_list["select_white_rice_mode"] = [
    {"step": 1, "actions": ["press_white_button"], "variable": "variable_cooking_mode", "comment": "Value always set to white rice"}
]

# Feature to select brown rice cooking mode
feature_list["select_brown_rice_mode"] = [
    {"step": 1, "actions": ["press_brown_rice_button"], "variable": "variable_cooking_mode", "comment": "Value always set to brown rice"}
]

# Feature to start cooking
feature_list["start_cooking"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_cooking", "comment": "Always set to on"}
]

# Feature to cancel or reset
feature_list["cancel_or_reset"] = [
    {"step": 1, "actions": ["press_keep_warm_cancel_button"], "variable": "variable_cancel_action", "comment": "Always set to cancel"}
]

# Null feature for unused actions and variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))