feature_list = {}

# Feature: Adjust Menu
feature_list["adjust_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

# Feature: Adjust Crust Color
feature_list["adjust_crust_color"] = [
    {"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color"}
]

# Feature: Adjust Loaf Size
feature_list["adjust_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_button"], "variable": "variable_loaf_size"}
]

# Feature: Adjust Delay Time
feature_list["adjust_delay_time"] = [
    {"step": 1, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_delay_time"}
]

# Feature: Start or Stop Bread Maker
feature_list["start_stop_bread_maker"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value always set to on or off"}
]

# Null feature for unused actions and variables
feature_list["null"] = [{"step": 1, "actions": ["press_and_hold_start_stop_button"], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))