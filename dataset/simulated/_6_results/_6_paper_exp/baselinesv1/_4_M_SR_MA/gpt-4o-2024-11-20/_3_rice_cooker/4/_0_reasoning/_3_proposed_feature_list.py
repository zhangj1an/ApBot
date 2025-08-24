feature_list = {}

# Feature to set the menu index
feature_list["set_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

# Feature to enable delay cooking/reservation
feature_list["set_delay_time"] = [
    {"step": 1, "actions": ["press_delay_button"], "variable": "variable_delay_time"}
]

# Feature to start cooking process
feature_list["start_cooking"] = [
    {
        "step": 1,
        "actions": ["press_start_button"],
        "variable": "variable_start_running",
        "comment": "value always set to on",
    }
]

# Feature to cancel cooking or set to keep warm mode
feature_list["keep_warm_cancel"] = [
    {
        "step": 1,
        "actions": ["press_keep_warm_cancel_button"],
        "variable": "variable_keep_warm",
    }
]

# Feature for Quick Rice function
feature_list["quick_rice_function"] = [
    {"step": 1, "actions": ["press_quick_rice_button"], "variable": "variable_menu_index", "comment": "value always set to quick_rice"}
]

# Include unused variables and actions in the "null" feature
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))