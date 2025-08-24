feature_list = {}

# Feature: Power On/Off
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Feature: Adjust Microbe Shield™ and Night Mode
feature_list["adjust_microbe_shield_night_mode"] = [
    {"step": 1, "actions": ["press_microbe_shield_night_mode_button"], "variable": "variable_microbe_shield_night_mode"}
]

# Feature: Adjust Fan Speed
feature_list["adjust_fan_speed"] = [
    {"step": 1, "actions": ["press_fan_speed_button"], "variable": "variable_fan_speed"}
]

# Feature: Timer Settings
feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

# Null feature for unused actions and variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))