# Features list
feature_list = {}

# Feature for setting menu and menu-specific settings
feature_list["set_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_menu_setting"}
]

# Feature for adjusting the delay timer
feature_list["adjust_delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_button"]},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_delay_timer"}
]

# Feature for toggling Keep Warm mode
feature_list["toggle_keep_warm_mode"] = [
    {"step": 1, "actions": ["press_keep_warm_stop_button"], "variable": "variable_keep_warm", "comment": "value toggles between on and off depending on mode"}
]

# Feature for starting the cooking process
feature_list["start_cooking"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Feature for stopping the cooking process if Keep Warm is not needed
feature_list["stop_cooking"] = [
    {"step": 1, "actions": ["press_and_hold_keep_warm_stop_button"], "variable": "variable_start_running", "comment": "value always set to off"}
]

# Null feature capturing unused actions and variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

# Initialize the Feature object
simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))