feature_list = {}

# Feature: Activate Sterilizer
feature_list["activate_sterilizer"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
]

# Feature: Set Dry Time for Automatic Sterilize/Dry
feature_list["automatic_sterilize_dry_time"] = [
    {"step": 1, "actions": ["press_automatic_sterilize_dry_button"], "variable": "variable_dry_time"}
]

# Feature: Set Dry Time for Dryer Only
feature_list["dryer_only_time"] = [
    {"step": 1, "actions": ["press_dry_only_button"], "variable": "variable_dryer_only_time"}
]

# Feature: Start Sterilize Only
feature_list["sterilize_only"] = [
    {"step": 1, "actions": ["press_sterilize_only_button"]}
]

# Null feature for unused actions and variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))