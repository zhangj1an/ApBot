feature_list = {}

feature_list["power_control"] = [
    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_on_off"}
]

feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

feature_list["set_program"] = [
    {"step": 1, "actions": ["press_program_buttons"], "variable": "variable_program"}
]

feature_list["adjust_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level"}
]

feature_list["adjust_rinse_times"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_times"}
]

feature_list["adjust_spin_speed"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_speed"}
]

feature_list["adjust_time_manager"] = [
    {"step": 1, "actions": ["press_time_manager_button"], "variable": "variable_time_manager"}
]

feature_list["toggle_clean_tub"] = [
    {"step": 1, "actions": ["press_clean_tub_off_button"], "variable": "variable_clean_tub"}
]

feature_list["toggle_child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_water_level_button_and_time_manager_button"], "variable": "variable_child_lock"}
]

feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))