feature_list = {}

feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

feature_list["set_sleep_mode"] = [
    {"step": 1, "actions": ["press_sleep_button"], "variable": "variable_sleep_mode"}
]

feature_list["set_mode"] = [
    {"step": 1, "actions": ["press_mode_button"], "variable": "variable_mode_selection"},
    {"step": 2, "actions": ["press_and_hold_mode_button"], "variable": "variable_child_lock", "comment": "value always set to on"}
]

feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"},
    {"step": 2, "actions": ["press_and_hold_timer_button"], "variable": "null", "comment": "No explicit variable to adjust"}
]

feature_list["set_humidity_level"] = [
    {"step": 1, "actions": ["press_humidity_button"], "variable": "variable_humidity_level"}
]

feature_list["set_internal_drying"] = [
    {"step": 1, "actions": ["press_and_hold_drying_button"], "variable": "variable_internal_drying"}
]

feature_list["set_drying_mode"] = [
    {"step": 1, "actions": ["press_drying_button"], "variable": "null", "comment": "No explicit variable to adjust"}
]

feature_list["set_anion_function"] = [
    {"step": 1, "actions": ["press_anion_button"], "variable": "variable_anion_function"}
]

feature_list["set_air_swing"] = [
    {"step": 1, "actions": ["press_swing_button"], "variable": "variable_air_swing"}
]

feature_list["convert_temperature_units"] = [
    {"step": 1, "actions": ["press_and_hold_humidity_button_and_timer_button"], "variable": "null", "comment": "Set between °C and °F conversion"}
]

feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))