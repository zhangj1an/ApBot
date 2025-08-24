feature_list = {}

# Feature 1: Turning the unit on and off
feature_list["power_control"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Feature 2: Adjusting the Fan/Air Speed
feature_list["adjust_fan_speed"] = [
    {"step": 1, "actions": ["press_speed_button"], "variable": "variable_fan_speed"}
]

# Feature 3: Controlling the Ion Generator
feature_list["control_ion_generator"] = [
    {"step": 1, "actions": ["press_ion_button"], "variable": "variable_ion_generator"}
]

# Feature 4: Setting the Auto On/Off Timer
feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

# Feature 5: Enabling Sleep Mode
feature_list["enable_sleep_mode"] = [
    {"step": 1, "actions": ["press_sleep_button"], "variable": "variable_sleep_mode"}
]

# Feature 6: Resetting the filter timer after replacing the filter
feature_list["reset_filter_timer"] = [
    {"step": 1, "actions": ["press_and_hold_sleep_button"], "variable": "variable_filter_timer_reset"}
]

# Null feature to include unused actions and variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))