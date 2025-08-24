feature_list = {}

feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
]

feature_list["select_program"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program"}
]

feature_list["adjust_load_size"] = [
    {"step": 1, "actions": ["press_load_size_button"], "variable": "variable_load_size"}
]

feature_list["adjust_wash_time"] = [
    {"step": 1, "actions": ["press_wash_button"], "variable": "variable_wash_time"}
]

feature_list["adjust_rinse_times"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_times"}
]

feature_list["adjust_spin_time"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_time"}
]

feature_list["start_pause_cycle"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

feature_list["null"] = [
    {"step": 1, "actions": ["press_and_hold_start_pause_button", "press_and_hold_on_off_button"], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))