feature_list = {}

feature_list["adjust_upper_element_temperature"] = [
    {"step": 1, "actions": ["turn_upper_element_temperature_dial_clockwise", "turn_upper_element_temperature_dial_anticlockwise"], "variable": "variable_upper_element_temperature"}
]

feature_list["adjust_lower_element_temperature"] = [
    {"step": 1, "actions": ["turn_lower_element_temperature_dial_clockwise", "turn_lower_element_temperature_dial_anticlockwise"], "variable": "variable_lower_element_temperature"}
]

feature_list["adjust_function_dial"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function_dial"}
]

feature_list["adjust_timer_dial"] = [
    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], "variable": "variable_timer"}
]

feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))