feature_list = {}

# Feature to set the menu (initial menu selection)
feature_list["set_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

# Feature to set reservation time after menu selection
feature_list["set_reservation_time"] = [
    {"step": 1, "actions": ["press_delay_button"], "variable": "variable_reservation_time"}
]

# Feature to start cooking
feature_list["start_cooking"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Feature to cancel cooking
feature_list["cancel_cooking"] = [
    {"step": 1, "actions": ["press_keep_warm_cancel_button"], "variable": "variable_start_running", "comment": "value always set to off"}
]

# Feature to directly activate the QUICK RICE function
feature_list["quick_rice_function"] = [
    {"step": 1, "actions": ["press_quick_rice_button"], "variable": "variable_menu_index", "comment": "value always set to QUICK RICE"}
]

# Null feature for unused variables or actions
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))