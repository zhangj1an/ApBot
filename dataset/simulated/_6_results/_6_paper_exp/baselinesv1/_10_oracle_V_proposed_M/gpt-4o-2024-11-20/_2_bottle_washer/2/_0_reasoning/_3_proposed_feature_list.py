feature_list = {}

feature_list["power_toggle_or_start_warming"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "comment": "This action toggles 'variable_power_on_off' between 'on' and 'off'. If turning on the device while 'variable_power_on_off' is 'off', it also initializes the warming process."}
]

feature_list["adjust_bottle_type"] = [
    {"step": 1, "actions": ["press_bottle_button"], "variable": "variable_bottle_type"}
]

feature_list["adjust_initial_temp"] = [
    {"step": 1, "actions": ["press_initial_temp_button"], "variable": "variable_initial_temp"}
]

feature_list["adjust_volume"] = [
    {"step": 1, "actions": ["press_volume_button"], "variable": "variable_volume"}
]

feature_list["night_light_toggle"] = [
    {"step": 1, "actions": ["press_and_hold_power_button"], "variable": "variable_night_light", "comment": "This action toggles the night light 'variable_night_light' between 'on' and 'off' regardless of the device's power state."}
]

feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))