feature_list = {}

# Feature to set the function knob
feature_list["set_function_knob"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function_knob"}
]

# Feature to adjust the upper heater temperature
feature_list["adjust_upper_heater_temperature"] = [
    {"step": 1, "actions": ["turn_upper_temp_dial_clockwise", "turn_upper_temp_dial_anticlockwise"], "variable": "variable_upper_heater_temperature"}
]

# Feature to adjust the lower heater temperature
feature_list["adjust_lower_heater_temperature"] = [
    {"step": 1, "actions": ["turn_lower_temp_dial_clockwise", "turn_lower_temp_dial_anticlockwise"], "variable": "variable_lower_heater_temperature"}
]

# Feature to set the timer
feature_list["set_timer"] = [
    {"step": 1, "actions": ["turn_time_dial_clockwise", "turn_time_dial_anticlockwise"], "variable": "variable_timer"}
]

# Null feature
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))