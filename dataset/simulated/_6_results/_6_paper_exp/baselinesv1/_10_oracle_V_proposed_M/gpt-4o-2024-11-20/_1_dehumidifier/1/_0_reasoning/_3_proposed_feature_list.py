feature_list = {}

# Power ON/OFF Feature
feature_list["power_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

# Sleep Mode Feature
feature_list["sleep_mode"] = [
    {"step": 1, "actions": ["press_sleep_button"], "variable": "variable_sleep_mode"}
]

# Mode Selection Feature
feature_list["mode_selection"] = [
    {"step": 1, "actions": ["press_mode_button"], "variable": "variable_mode_selection"}
]

# Timer Adjustment Feature
feature_list["timer_adjustment"] = [
    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
]

# Humidity Level Adjustment Feature
feature_list["humidity_level_adjustment"] = [
    {"step": 1, "actions": ["press_humidity_button"], "variable": "variable_humidity_level"},
    {"step": 2, "actions": ["press_and_hold_humidity_button_and_timer_button"], "comment": "Humidity units (°C/°F) toggle using this button combination."}
]

# Internal Drying Feature
feature_list["internal_drying"] = [
    {"step": 1, "actions": ["press_and_hold_drying_button"], "variable": "variable_internal_drying"}
]

# Anion Function Feature
feature_list["anion_function"] = [
    {"step": 1, "actions": ["press_anion_button"], "variable": "variable_anion_function"}
]

# Air Swing Feature
feature_list["air_swing"] = [
    {"step": 1, "actions": ["press_swing_button"], "variable": "variable_air_swing"}
]

# Child Lock Feature
feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_mode_button"], "variable": "variable_child_lock"}
]

# Null Feature for Unused Actions and Variables
feature_list["null"] = [
    {"step": 1, "actions": [], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))