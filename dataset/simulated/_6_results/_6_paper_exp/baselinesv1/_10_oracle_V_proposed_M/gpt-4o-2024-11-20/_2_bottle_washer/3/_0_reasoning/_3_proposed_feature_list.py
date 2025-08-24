feature_list = {}
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_and_hold_power_button"], "variable": "variable_power_on_off"}
]

feature_list["set_wash_mode"] = [
    {"step": 1, "actions": ["press_wash_mode_button"], "variable": "variable_wash_mode"}
]

feature_list["set_sterilize_dry_mode"] = [
    {"step": 1, "actions": ["press_sterilize_dry_button"], "variable": "variable_sterilize_dry_mode"}
]

feature_list["start_appliance"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))