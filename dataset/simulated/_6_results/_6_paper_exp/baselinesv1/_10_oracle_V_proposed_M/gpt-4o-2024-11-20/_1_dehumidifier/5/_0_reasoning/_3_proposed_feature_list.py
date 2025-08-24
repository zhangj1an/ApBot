feature_list = {}

feature_list["toggle_power"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

feature_list["adjust_fan_speed"] = [
    {"step": 1, "actions": ["press_speed_button"], "variable": "variable_fan_speed"}
]

feature_list["toggle_ion_generator"] = [
    {"step": 1, "actions": ["press_ion_button"], "variable": "variable_ion_generator"}
]

feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

feature_list["toggle_sleep_mode_or_reset_filter_timer"] = [
    {"step": 1, "actions": ["press_sleep_button"], "variable": "variable_sleep_mode", "comment": "hold action resets filter timer after replacing filter"}
]

feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))