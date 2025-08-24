feature_list = {}

# Setting the auto menu
feature_list["set_auto_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"},
]

# Adjusting crust color
feature_list["adjust_crust_color"] = [
    {"step": 1, "actions": ["press_crust_colour_button"], "variable": "variable_crust_color"},
]

# Adjusting loaf size
feature_list["adjust_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"},
]

# Adjusting timer using up and down arrows
feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["press_timer_up_button", "press_timer_down_button"], "variable": "variable_timer"},
]

# Activating gluten-free mode
feature_list["activate_gluten_free_mode"] = [
    {"step": 1, "actions": ["press_gluten_free_button"], "variable": "variable_gluten_free_mode"},
]

# Starting or cancelling a program
feature_list["start_or_cancel_program"] = [
    {"step": 1, "actions": ["press_start_cancel_button"], "variable": "variable_start_running", "comment": "value always set to on or off"},
]

# Press and hold to cancel keep warm functionality
feature_list["hold_to_cancel_keep_warm"] = [
    {"step": 1, "actions": ["press_and_hold_start_cancel_button"], "variable": "variable_start_running", "comment": "value always set to off"},
]

# Null feature for unused actions and variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))