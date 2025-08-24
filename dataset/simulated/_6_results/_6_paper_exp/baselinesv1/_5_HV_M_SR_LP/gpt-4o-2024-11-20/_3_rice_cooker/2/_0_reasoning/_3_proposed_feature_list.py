feature_list = {}

# Feature 1: Select Cooking Mode
feature_list["select_cooking_mode"] = [
    {"step": 1, "actions": ["press_menu_cancel_button"], "variable": "variable_cooking_mode"}
]

# Feature 2: Adjust Preset Timer
feature_list["adjust_preset_timer"] = [
    {"step": 1, "actions": ["press_preset_time_time_button"], "variable": "variable_preset_timer"}
]

# Feature 3: Start Cooking
feature_list["start_cooking"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Null feature for unused actions and variables
feature_list["null"] = [{"step": 1, "actions": ["press_and_hold_preset_time_time_button"], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))