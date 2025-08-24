feature_list = {}

# Power On/Off Feature
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Set Menu and Adjust Menu Setting Feature
feature_list["set_menu_and_adjust_setting"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"},
    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_menu_setting"}
]

# Null Feature
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))