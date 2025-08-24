feature_list = {}

# Power On/Off Feature
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_on_off_button"], "variable": "variable_power_on_off"}
]

# Sterilise Only Feature
feature_list["sterilise_only"] = [
    {"step": 1, "actions": ["press_sterilise_only_button"], "variable": "variable_sterilise_only_time"}
]

# Drying Only Feature
feature_list["drying_only"] = [
    {"step": 1, "actions": ["press_drying_only_button"], "variable": "variable_drying_only_time"}
]

# Auto Mode Feature
feature_list["auto_mode"] = [
    {"step": 1, "actions": ["press_auto_mode_button"], "variable": "variable_auto_mode"}
]

# Storage Mode Feature
feature_list["storage_mode"] = [
    {"step": 1, "actions": ["press_storage_button"], "variable": "variable_storage_mode"}
]

# Null Feature for completeness
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))