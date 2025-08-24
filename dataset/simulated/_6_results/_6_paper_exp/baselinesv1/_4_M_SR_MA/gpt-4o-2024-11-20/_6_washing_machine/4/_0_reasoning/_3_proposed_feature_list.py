feature_list = {}

# Feature for turning power on/off
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button", "press_and_hold_power_button"], "variable": "variable_power_on_off"}
]

# Feature for starting or pausing the washing machine
feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button", "press_and_hold_start_pause_button"], 
     "variable": "variable_start_running", 
     "comment": "value always set to either 'start' or 'pause'"}
]

# Feature for adjusting washing program
feature_list["adjust_program"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program"}
]

# Feature for adjusting water level
feature_list["adjust_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level"}
]

# Feature for adjusting washing time
feature_list["adjust_wash_time"] = [
    {"step": 1, "actions": ["press_wash_button"], "variable": "variable_washing_time"}
]

# Feature for adjusting rinsing type
feature_list["adjust_rinse_type"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_type"}
]

# Feature for adjusting spin time
feature_list["adjust_spin_time"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_time"}
]

# Feature for setting delay timer
feature_list["delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_button"], "variable": "variable_delay_timer"}
]

# Null feature for unused actions/variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))