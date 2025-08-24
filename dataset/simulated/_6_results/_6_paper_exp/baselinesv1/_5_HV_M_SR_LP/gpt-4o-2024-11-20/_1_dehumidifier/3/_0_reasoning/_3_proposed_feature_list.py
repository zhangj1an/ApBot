feature_list = {}

# Feature: Power Control
feature_list["power_control"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Feature: Adjust Timer
feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

# Feature: UV Light Control
feature_list["uv_light_control"] = [
    {"step": 1, "actions": ["press_uv_button"], "variable": "variable_uv_light"}
]

# Feature: Reset UV Indicator (Requires resetting when usage reaches 3000 hours)
feature_list["reset_uv_indicator"] = [
    {"step": 1, "actions": ["press_and_hold_uv_button"]}
]

# Feature: Ionizer Control
feature_list["ionizer_control"] = [
    {"step": 1, "actions": ["press_ionizer_button"], "variable": "variable_ionizer"}
]

# Feature: Reset Filter Indicator (Requires resetting when usage reaches 2000 hours)
feature_list["reset_filter_indicator"] = [
    {"step": 1, "actions": ["press_and_hold_ionizer_button"]}
]

# Feature: Adjust Fan Speed/Mode
feature_list["adjust_fan_speed_mode"] = [
    {"step": 1, "actions": ["press_speed_mode_button"], "variable": "variable_fan_speed_mode"}
]

# Null feature: No unused actions or variables are provided.
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

# Initialize the simulator feature object
simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))