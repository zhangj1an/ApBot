feature_list = {}

# Feature for starting the appliance
feature_list["start_appliance"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Feature for cancelling or stopping operation
feature_list["cancel_operation"] = [
    {"step": 1, "actions": ["press_cancel_button"], "variable": "variable_start_running", "comment": "value always set to off"}
]

# Feature for selecting a cooking program (e.g., Jasmine Rice, White Rice, Brown Rice, etc.)
feature_list["select_cooking_program"] = [
    {"step": 1, "actions": ["press_jasmine_rice_button", "press_white_rice_button", "press_brown_rice_button", 
                            "press_glutinous_rice_button", "press_clay_pot_button", "press_quick_cooking_steam_button", 
                            "press_soup_congee_button", "press_slow_cook_stew_button", "press_reheat_button"], 
     "variable": "variable_cooking_program"}
]

# Feature for setting the timer
feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

# Feature for setting the preset time
feature_list["adjust_preset_time"] = [
    {"step": 1, "actions": ["press_preset_button"], "variable": "variable_preset_time"}
]

# Feature for enabling/disabling keep warm functionality
feature_list["toggle_keep_warm"] = [
    {"step": 1, "actions": ["press_and_hold_start_button", "press_and_hold_start_button_and_cancel_button"], 
     "variable": "variable_keep_warm"}
]

# Feature for handling unused or extra actions
feature_list["null"] = [
    {"step": 1, "actions": ["press_and_hold_cancel_button"], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))