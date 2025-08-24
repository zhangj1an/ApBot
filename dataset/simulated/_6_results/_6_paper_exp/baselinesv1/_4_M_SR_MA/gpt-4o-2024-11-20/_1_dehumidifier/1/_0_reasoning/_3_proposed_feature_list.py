feature_list = {}

feature_list["power_on_off"] = [
        {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

feature_list["adjust_sleep_mode"] = [
        {"step": 1, "actions": ["press_sleep_button"], "variable": "variable_sleep_mode"}
]

feature_list["mode_selection"] = [
        {"step": 1, "actions": ["press_mode_button"], "variable": "variable_mode_selection"},
        {"step": 2, "actions": ["press_and_hold_mode_button"], "variable": "variable_child_lock"}
]

feature_list["adjust_timer"] = [
        {"step": 1, "actions": ["press_timer_button", "press_and_hold_timer_button"], "variable": "variable_timer"}
]

feature_list["adjust_humidity"] = [
        {"step": 1, "actions": ["press_humidity_button"], "variable": "variable_humidity_level"}
]

feature_list["adjust_humidity_unit"] = [
        {"step": 1, "actions": ["press_and_hold_humidity_button_and_timer_button"], "comment": "changes between °C and °F"}
]

feature_list["internal_drying_process"] = [
        {"step": 1, "actions": ["press_and_hold_drying_button"], "variable": "variable_internal_drying"}
]

feature_list["adjust_anion_function"] = [
        {"step": 1, "actions": ["press_anion_button"], "variable": "variable_anion_function"}
]

feature_list["adjust_air_swing"] = [
        {"step": 1, "actions": ["press_swing_button"], "variable": "variable_air_swing"}
]

feature_list["null"] = [
        {"step": 1, "actions": ["press_drying_button"], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))