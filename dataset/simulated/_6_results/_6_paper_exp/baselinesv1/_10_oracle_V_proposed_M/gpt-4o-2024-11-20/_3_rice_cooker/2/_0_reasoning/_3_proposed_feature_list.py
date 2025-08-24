feature_list = {}

# Feature: Start running the appliance (ON state)
feature_list["start_running"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", 
    "comment": "value always set to 'on'"},
]

# Feature: Set cooking mode
feature_list["set_cooking_mode"] = [
    {"step": 1, "actions": ["press_menu_cancel_button"], "variable": "variable_cooking_mode"}
]

# Feature: Control preset timer for delayed cooking
feature_list["set_preset_timer"] = [
    {"step": 1, "actions": ["press_preset_time_time_button"], "variable": "variable_preset_timer"}
]

# Null feature for unused variables and actions
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

# Initialize the simulator feature object
simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))