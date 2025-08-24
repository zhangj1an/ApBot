feature_list = {}

# "Delay Timer" feature
feature_list["set_delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_button"]},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_delay_timer"}
]

# "Menu Selection and Setting" feature
feature_list["set_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_menu_setting"}
]

# "Start Cooking" feature
feature_list["start_cooking"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# "Keep Warm/Stop" feature
feature_list["set_keep_warm_or_stop"] = [
    {"step": 1, "actions": ["press_keep_warm_stop_button"], "variable": "variable_keep_warm"}
]

# Null feature to include all unused actions and variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))