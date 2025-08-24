feature_list = {}

feature_list["adjust_cooking_time_and_start"] = [
    {"step": 1, "actions": ["turn_time_adjustment_dial_clockwise", "turn_time_adjustment_dial_anticlockwise"], "variable": "variable_time_adjustment", "comment": "variable_start_running: set to 'on' when starting"}
]

feature_list["adjust_upper_tube_temperature"] = [
    {"step": 1, "actions": ["turn_upper_tube_temperature_adjustment_dial_clockwise", "turn_upper_tube_temperature_adjustment_dial_anticlockwise"], "variable": "variable_upper_tube_temperature"}
]

feature_list["adjust_function_selection"] = [
    {"step": 1, "actions": ["turn_function_selection_dial_clockwise", "turn_function_selection_dial_anticlockwise"], "variable": "variable_function_selection"}
]

feature_list["adjust_lower_tube_temperature"] = [
    {"step": 1, "actions": ["turn_lower_tube_temperature_adjustment_dial_clockwise", "turn_lower_tube_temperature_adjustment_dial_anticlockwise"], "variable": "variable_lower_tube_temperature"}
]

feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))