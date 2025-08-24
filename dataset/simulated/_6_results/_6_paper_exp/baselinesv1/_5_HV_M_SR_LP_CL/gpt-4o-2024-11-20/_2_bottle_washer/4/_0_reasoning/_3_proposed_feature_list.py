feature_list = {}

# Feature to turn the appliance on or off
feature_list["turn_on_off_appliance"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Feature to select and adjust menu options
feature_list["set_and_adjust_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_menu_setting"}
]

# Feature to capture unused or irrelevant actions, and unmentioned variables
feature_list["null"] = [
    {"step": 1, "actions": ["press_and_hold_power_button", "press_and_hold_minus_button", "press_and_hold_plus_button", "press_and_hold_menu_button"], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))