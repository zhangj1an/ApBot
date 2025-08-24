feature_list = {}

# Power On/Off Feature
feature_list["power_control"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Start/Pause Feature
feature_list["start_pause_control"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running"}
]

# Adjust Program Feature
feature_list["select_program"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program"}
]

# Adjust Water Level Feature
feature_list["adjust_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level"}
]

# Adjust Washing Time Feature
feature_list["adjust_washing_time"] = [
    {"step": 1, "actions": ["press_wash_button"], "variable": "variable_washing_time"}
]

# Adjust Rinse Type Feature
feature_list["adjust_rinse_type"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_type"}
]

# Adjust Spin Time Feature
feature_list["adjust_spin_time"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_time"}
]

# Adjust Delay Timer Feature
feature_list["adjust_delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_button"], "variable": "variable_delay_timer"}
]

# Null Feature
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))