feature_list = {}

# Feature: Sterilise Only Function
feature_list["sterilise_only_function"] = [
    {"step": 1, "actions": ["press_sterilise_only_button"], "variable": "variable_sterilise_only_duration"}
]

# Feature: Drying Only Function
feature_list["drying_only_function"] = [
    {"step": 1, "actions": ["press_drying_only_button"], "variable": "variable_drying_only_duration"}
]

# Feature: Auto Mode
feature_list["auto_mode"] = [
    {"step": 1, "actions": ["press_auto_mode_button"], "variable": "variable_auto_mode_duration"}
]

# Feature: Storage Function
feature_list["storage_function"] = [
    {"step": 1, "actions": ["press_storage_button"], "variable": "variable_storage_mode"}
]

# Feature: Power On/Off
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_on_off_button"], "variable": "variable_power_on_off"}
]

# Feature: Button Sound
feature_list["button_sound"] = [
    {"step": 1, "actions": ["press_and_hold_sterilise_only_button_and_power_on_off_button"], "variable": "variable_button_sound"}
]

# Null Feature
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))