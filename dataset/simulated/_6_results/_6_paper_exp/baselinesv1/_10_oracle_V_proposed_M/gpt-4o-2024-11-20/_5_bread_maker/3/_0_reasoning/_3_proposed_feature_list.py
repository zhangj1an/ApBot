feature_list = {}

# Feature for selecting cycle
feature_list["select_cycle"] = [
    {"step": 1, "actions": ["press_cycle_button"], "variable": "variable_cycle"}
]

# Feature for selecting crust color
feature_list["select_crust_color"] = [
    {"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color"}
]

# Feature for selecting loaf size
feature_list["select_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
]

# Feature for setting delay timer
feature_list["set_delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_plus_button", "press_delay_timer_minus_button"], "variable": "variable_delay_timer"}
]

# Feature for starting or stopping the operation
feature_list["start_stop_operation"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value set to 'on'."}
]

# Feature for cancelling operation when holding the button
feature_list["cancel_operation"] = [
    {"step": 1, "actions": ["press_and_hold_start_stop_button"], "variable": "variable_start_running", "comment": "value set to 'off'."}
]

# Null feature with no missing actions or variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

# Initialize the Feature() object
simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))