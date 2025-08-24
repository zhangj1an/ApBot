feature_list = {}

feature_list["set_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

feature_list["set_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
]

feature_list["set_crust_color"] = [
    {"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color"}
]

feature_list["set_delay_timer"] = [
    {"step": 1, "actions": ["press_time_plus_button", "press_time_minus_button"], "variable": "variable_delay_timer"}
]

feature_list["start_stop_program"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value always toggles between on and off"}
]

feature_list["null"] = [
    {"step": 1, "actions": ["press_and_hold_start_stop_button"], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))