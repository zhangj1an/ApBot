feature_list = {}

# Feature: Power On/Off
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
]

# Feature: Set Operating Mode
feature_list["set_operating_mode"] = [
    {"step": 1, "actions": ["press_mode_button"], "variable": "variable_mode"}
]

# Feature: Set Temperature
feature_list["set_temperature"] = [
    {"step": 1, "actions": ["press_decrease_temp_setting_button", "press_increase_temp_setting_button"], "variable": "variable_temperature_setting"}
]

# Feature: Set Fan Speed
feature_list["set_fan_speed"] = [
    {"step": 1, "actions": ["press_speed_uv_button"], "variable": "variable_fan_speed"}
]

# Feature: Set Timer
feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer_setting"}
]

# Feature: Activate Sleep Mode
feature_list["activate_sleep_mode"] = [
    {"step": 1, "actions": ["press_and_hold_mode_button"], "variable": "variable_sleep_mode"}
]

# Null Feature for unused actions and variables
feature_list["null"] = [{"step": 1, "actions": ["press_and_hold_on_off_button", "press_and_hold_speed_uv_button", "press_and_hold_decrease_temp_setting_button_and_increase_temp_setting_button", "press_and_hold_increase_temp_setting_button"], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))