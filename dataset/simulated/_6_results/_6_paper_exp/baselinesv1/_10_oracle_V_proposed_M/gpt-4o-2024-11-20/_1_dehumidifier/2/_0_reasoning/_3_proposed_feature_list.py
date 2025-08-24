feature_list = {}

# Power On/Off Feature
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
]

# Adjust Mode Feature
feature_list["adjust_mode"] = [
    {"step": 1, "actions": ["press_mode_button"], "variable": "variable_mode"}
]

# Adjust Temperature Feature
feature_list["adjust_temperature"] = [
    {"step": 1, "actions": ["press_increase_temp_setting_button", "press_decrease_temp_setting_button"], "variable": "variable_temperature_setting"}
]

# Adjust Fan Speed Feature
feature_list["adjust_fan_speed"] = [
    {"step": 1, "actions": ["press_speed_uv_button"], "variable": "variable_fan_speed"}
]

# Timer Setting Feature
feature_list["adjust_timer_setting"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer_setting"}
]

# Null Feature
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))