feature_list = {}

feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

feature_list["microbe_shield_night_mode"] = [
    {"step": 1, "actions": ["press_microbe_shield_night_mode_button"], "variable": "variable_microbe_shield_night_mode"}
]

feature_list["adjust_fan_speed"] = [
    {"step": 1, "actions": ["press_fan_speed_button"], "variable": "variable_fan_speed"}
]

feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

feature_list["null"] = [
    {"step": 1, "actions": ["press_and_hold_power_button"], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))