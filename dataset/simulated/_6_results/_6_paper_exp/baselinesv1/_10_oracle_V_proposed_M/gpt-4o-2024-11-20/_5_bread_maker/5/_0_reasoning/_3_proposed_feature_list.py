feature_list = {}

# Feature to set the program menu
feature_list["set_program_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

# Feature to adjust loaf size
feature_list["adjust_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
]

# Feature to adjust crust color
feature_list["adjust_crust_color"] = [
    {"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color"}
]

# Feature to adjust delay timer
feature_list["adjust_delay_timer"] = [
    {"step": 1, "actions": ["press_time_plus_button", "press_time_minus_button"], "variable": "variable_delay_timer"}
]

# Feature to start/stop the appliance
feature_list["start_stop_appliance"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value toggles between 'on' and 'off'"}
]

# Null feature for unused actions and variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))