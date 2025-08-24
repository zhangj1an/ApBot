feature_list = {}

# Feature: Adjust Child Lock
feature_list["adjust_child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_temp_button_and_spin_button"], "variable": "variable_child_lock"}
]

# Feature: Adjust Temperature
feature_list["adjust_temperature"] = [
    {"step": 1, "actions": ["press_temp_button"], "variable": "variable_temperature"}
]

# Feature: Adjust Spin Speed
feature_list["adjust_spin_speed"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_speed"}
]

# Feature: Adjust Options
feature_list["adjust_options"] = [
    {"step": 1, "actions": ["press_option_button"], "variable": "variable_option"}
]

# Feature: Adjust Cycle Selector
feature_list["adjust_cycle_selector"] = [
    {"step": 1, "actions": ["turn_cycle_selector_dial_clockwise", "turn_cycle_selector_dial_anticlockwise"], "variable": "variable_cycle_selector"}
]

# Feature: Adjust Delay End
feature_list["adjust_delay_end"] = [
    {"step": 1, "actions": ["press_delay_end_button"], "variable": "variable_delay_end"}
]

# Feature: Power On/Off
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Feature: Start/Pause a Cycle
feature_list["start_pause_cycle"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "comment": "value always set to on/off"}
]

# Null feature to capture unused actions and variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))