feature_list = {}

# Feature to adjust the function dial
feature_list["adjust_function_dial"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], 
    "variable": "variable_function_dial"}
]

# Feature to adjust the temperature dial
feature_list["adjust_temperature_dial"] = [
    {"step": 1, "actions": ["turn_temperature_dial_clockwise", "turn_temperature_dial_anticlockwise"], 
    "variable": "variable_temperature_dial"}
]

# Feature to adjust the selector dial
feature_list["adjust_selector_dial"] = [
    {"step": 1, "actions": ["turn_selector_dial_clockwise", "turn_selector_dial_anticlockwise"], 
    "variable": "variable_selector_dial"}
]

# Feature to adjust the timer dial
feature_list["adjust_timer_dial"] = [
    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], 
    "variable": "variable_timer_dial"}
]

# Null feature to handle unused actions and variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))