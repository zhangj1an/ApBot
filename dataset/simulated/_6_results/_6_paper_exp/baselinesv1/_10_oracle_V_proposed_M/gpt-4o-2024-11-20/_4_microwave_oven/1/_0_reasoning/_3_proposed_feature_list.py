feature_list = {}

# Setting Clock
feature_list["set_clock"] = [
    {"step": 1, "actions": ["press_clock_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_clock", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_clock_button"]},
]

# Setting Timer
feature_list["set_kitchen_timer"] = [
    {"step": 1, "actions": ["press_timer_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_timer", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_start_plus_30sec_button"]},
]

# Microwave Cooking
feature_list["set_microwave_cook_time_power"] = [
    {"step": 1, "actions": ["press_time_cook_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_time_cook_time", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_power_button"]},
    {"step": 4, "actions": meta_actions_on_number, "variable": "variable_power"},
    {"step": 5, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "comment": "value always set to on"},
]

# Speedy Cooking
feature_list["speedy_cooking"] = [
    {"step": 1, "actions": meta_actions_on_number, "variable": "variable_time_cook_time", "comment": "requires parsing from variable_input_string"},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "comment": "value always set to on"},
]

# Add +30 Seconds During Cooking
feature_list["add_cook_time_plus_30sec"] = [
    {"step": 1, "actions": ["press_start_plus_30sec_button"], "variable": "variable_time_cook_time", "comment": "increments cooking time by 30 seconds"},
]

# Weight Defrost
feature_list["set_weight_defrost"] = [
    {"step": 1, "actions": ["press_weight_defrost_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_weight_defrost", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "comment": "value always set to on"},
]

# Time Defrost
feature_list["set_time_defrost"] = [
    {"step": 1, "actions": ["press_time_defrost_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_time_defrost", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_power_button"]},
    {"step": 4, "actions": meta_actions_on_number, "variable": "variable_power"},
    {"step": 5, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "comment": "value always set to on"},
]

# Preset Menus
feature_list["set_menu"] = [
    {"step": 1, "actions": ["press_popcorn_button", "press_potato_button", "press_frozen_vegetable_button", "press_beverage_button", "press_dinner_plate_button", "press_pizza_button"], "variable": "variable_menu_index"},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_menu_setting", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "comment": "value always set to on"},
]

# Child Lock
feature_list["toggle_child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_stop_cancel_button"], "variable": "variable_child_lock"},
]

# Cancel Operation
feature_list["cancel_operation"] = [
    {"step": 1, "actions": ["press_stop_cancel_button"], "variable": "variable_start_running", "comment": "value always set to off"},
]

# Null Feature
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

# Initialize the simulator feature
simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))