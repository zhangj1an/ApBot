feature_list = {}

# Feature: Power On/Off
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Feature: Timer Setting
feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

# Feature: UV Light On/Off
feature_list["uv_light_control"] = [
    {"step": 1, "actions": ["press_uv_button"], "variable": "variable_uv_light"}
]

# Feature: UV Light Reset
feature_list["uv_reset"] = [
    {"step": 1, "actions": ["press_and_hold_uv_button"]}
]

# Feature: Ionizer On/Off
feature_list["ionizer_control"] = [
    {"step": 1, "actions": ["press_ionizer_button"], "variable": "variable_ionizer"}
]

# Feature: Filter Reset
feature_list["filter_reset"] = [
    {"step": 1, "actions": ["press_and_hold_ionizer_button"]}
]

# Feature: Fan Speed/Mode Setting
feature_list["fan_speed_mode_control"] = [
    {"step": 1, "actions": ["press_speed_mode_button"], "variable": "variable_fan_speed_mode"}
]

# Null feature for unused actions and variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))