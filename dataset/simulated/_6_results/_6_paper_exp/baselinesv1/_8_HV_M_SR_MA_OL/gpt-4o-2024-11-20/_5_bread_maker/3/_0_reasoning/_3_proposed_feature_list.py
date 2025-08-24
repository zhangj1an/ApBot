feature_list = {}

feature_list["select_cycle"] = [
    {"step": 1, "actions": ["press_cycle_button"], "variable": "variable_cycle"}
]

feature_list["adjust_crust_color"] = [
    {"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color"}
]

feature_list["adjust_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
]

feature_list["adjust_delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_plus_button", "press_delay_timer_minus_button"], "variable": "variable_delay_timer"}
]

feature_list["start_or_stop_operation"] = [
    {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value alternates between on and off"}
]

feature_list["cancel_operation"] = [
    {"step": 1, "actions": ["press_and_hold_start_stop_button"], "variable": "variable_start_running", "comment": "value set to off"}
]

feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))