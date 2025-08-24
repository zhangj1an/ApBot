feature_list = {}

# Feature: General Cooking Use
feature_list["general_cooking"] = [
    {"step": 1, "actions": ["turn_temperature_dial_clockwise"], "variable": "variable_temperature_dial"},
    {"step": 2, "actions": ["turn_function_dial_clockwise"], "variable": "variable_function_dial"},
    {"step": 3, "actions": ["turn_selector_dial_clockwise"], "variable": "variable_selector_dial"},
    {"step": 4, "actions": ["turn_timer_dial_clockwise"], "variable": "variable_timer_dial"}
]

# Feature: Grill Cooking (Specialized Cooking Method)
feature_list["grill_cooking"] = [
    {"step": 1, "actions": ["turn_selector_dial_clockwise"], "variable": "variable_selector_dial", "comment": 'Set to "Top Heating"'},
    {"step": 2, "actions": ["turn_temperature_dial_clockwise"], "variable": "variable_temperature_dial", "comment": 'Set to "250°C"'},
    {"step": 3, "actions": ["turn_timer_dial_clockwise"], "variable": "variable_timer_dial"}
]

# Feature: Rotisserie (Specialized Cooking Method)
feature_list["rotisserie_use"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise"], "variable": "variable_function_dial", "comment": 'Select "Rotisserie" or "Rotisserie & Convection"'},
    {"step": 2, "actions": ["turn_temperature_dial_clockwise"], "variable": "variable_temperature_dial", "comment": 'Set to "250°C"'},
    {"step": 3, "actions": ["turn_selector_dial_clockwise"], "variable": "variable_selector_dial"},
    {"step": 4, "actions": ["turn_timer_dial_clockwise"], "variable": "variable_timer_dial"}
]

# Null Feature (accounts for unused actions and variables)
feature_list["null"] = [
    {"step": 1,
     "actions": ["turn_timer_dial_anticlockwise", "turn_temperature_dial_anticlockwise", "turn_function_dial_anticlockwise", "turn_selector_dial_anticlockwise"],
     "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))