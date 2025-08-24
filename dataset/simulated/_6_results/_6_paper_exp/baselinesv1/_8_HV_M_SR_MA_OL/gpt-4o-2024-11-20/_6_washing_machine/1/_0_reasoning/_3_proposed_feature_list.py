feature_list = {}

# Adjust Power: activating and deactivating the power.
feature_list["power_adjust"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Adjust Start/Rerun state: start or pause the cycle.
feature_list["start_pause_cycle"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running"}
]

# Adjust Child Lock: activating and deactivating the child lock.
feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_temp_button_and_spin_button"], "variable": "variable_child_lock"}
]

# Adjust Temperature: cycling through temperature options.
feature_list["adjust_temperature"] = [
    {"step": 1, "actions": ["press_temp_button"], "variable": "variable_temperature"}
]

# Adjust Spin Speed: cycling through spin speed options.
feature_list["adjust_spin_speed"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_speed"}
]

# Adjust Options: cycling through available washing options.
feature_list["adjust_options"] = [
    {"step": 1, "actions": ["press_option_button"], "variable": "variable_option"}
]

# Adjust Cycle Selector: selecting a washing cycle pattern.
feature_list["adjust_cycle_selector"] = [
    {"step": 1, "actions": ["turn_cycle_selector_dial_clockwise", "turn_cycle_selector_dial_anticlockwise"], "variable": "variable_cycle_selector"}
]

# Adjust Delay End: setting delay end timer.
feature_list["adjust_delay_end"] = [
    {"step": 1, "actions": ["press_delay_end_button"], "variable": "variable_delay_end"}
]

# Null feature for unused actions and variables and addressing the missing actions.
feature_list["null"] = [
    {
        "step": 1,
        "actions": ["press_and_hold_option_button_and_delay_end_button", "press_and_hold_spin_button_and_option_button"],
        "missing_variables": []
    }
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))