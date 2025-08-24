feature_list = {}

feature_list["adjust_upper_heater_temperature"] = [
    {"step": 1, "actions": ["turn_upper_temp_dial_clockwise", "turn_upper_temp_dial_anticlockwise"], "variable": "variable_upper_heater_temperature"}
]

feature_list["adjust_lower_heater_temperature"] = [
    {"step": 1, "actions": ["turn_lower_temp_dial_clockwise", "turn_lower_temp_dial_anticlockwise"], "variable": "variable_lower_heater_temperature"}
]

feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["turn_time_dial_clockwise", "turn_time_dial_anticlockwise"], "variable": "variable_timer"}
]

feature_list["select_function"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function_knob"}
]

# Include unused actions and variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))