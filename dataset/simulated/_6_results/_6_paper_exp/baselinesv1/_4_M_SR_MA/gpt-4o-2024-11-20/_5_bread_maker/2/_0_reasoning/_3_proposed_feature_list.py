feature_list = {}

feature_list["set_menu_and_setting"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"} 
]

feature_list["adjust_crust_color"] = [
    {"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color"}
]

feature_list["adjust_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
]

feature_list["adjust_timer_delay"] = [
    {"step": 1, "actions": ["press_time_up_button", "press_time_down_button"], "variable": "variable_timer_delay"}
]

feature_list["start_stop_operation"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value always set to on or off"}
]

feature_list["null"] = [{"step": 1, "actions": ["press_and_hold_start_stop_button"], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))