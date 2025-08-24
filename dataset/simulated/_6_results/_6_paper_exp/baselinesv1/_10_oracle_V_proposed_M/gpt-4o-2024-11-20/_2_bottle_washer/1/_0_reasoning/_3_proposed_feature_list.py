feature_list = {}

# Feature: Power On/Off
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
]

# Feature: Automatic Sterilize/Dry Function
feature_list["automatic_sterilize_dry"] = [
    {"step": 1, "actions": ["press_automatic_sterilize_dry_button"], "variable": "variable_dry_time", 
     "comment": "Variable dry_time is dynamically set based on button press. Pressing button 1 time for 30 minutes dry time, 2 times for 45 minutes, 3 times for 60 minutes"}
]

# Feature: Dryer Only Function
feature_list["dryer_only"] = [
    {"step": 1, "actions": ["press_dry_only_button"], "variable": "variable_dryer_only_time", 
     "comment": "Variable dryer_only_time is dynamically set based on button press. Pressing button 1 time for 30 minutes dry time, 2 times for 45 minutes, 3 times for 60 minutes"}
]

# Feature: Sterilize Only Function
feature_list["sterilize_only"] = [
    {"step": 1, "actions": ["press_sterilize_only_button"], "comment": "Sterilize only function starts sterilization process and automatically switches off when complete"}
]

# Null feature to handle unused actions and variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))