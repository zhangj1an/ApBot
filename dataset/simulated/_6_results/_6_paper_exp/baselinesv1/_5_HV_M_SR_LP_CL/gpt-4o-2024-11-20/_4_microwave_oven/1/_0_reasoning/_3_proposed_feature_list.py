feature_list = {}

feature_list["set_clock"] = [
    {"step": 1, "actions": ["press_clock_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_clock", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_clock_button"]}
]

feature_list["set_kitchen_timer"] = [
    {"step": 1, "actions": ["press_timer_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_timer", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_start_plus_30sec_button"]}
]

feature_list["microwave_cook"] = [
    {"step": 1, "actions": ["press_time_cook_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_time_cook_time", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_power_button"]},
    {"step": 4, "actions": meta_actions_on_number, "variable": "variable_power"},
    {"step": 5, "actions": ["press_start_plus_30sec_button"]}
]

feature_list["weight_defrost"] = [
    {"step": 1, "actions": ["press_weight_defrost_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_weight_defrost", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_start_plus_30sec_button"]}
]

feature_list["time_defrost"] = [
    {"step": 1, "actions": ["press_time_defrost_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_time_defrost", "comment": "requires parsing from variable_input_string"},
    {"step": 3, "actions": ["press_power_button"]},
    {"step": 4, "actions": meta_actions_on_number, "variable": "variable_power"},
    {"step": 5, "actions": ["press_start_plus_30sec_button"]}
]

feature_list["adjust_menu_settings"] = [
    {"step": 1, "actions": ["press_popcorn_button", "press_potato_button", "press_frozen_vegetable_button", "press_beverage_button", "press_dinner_plate_button", "press_pizza_button"], "variable": "variable_menu_index"},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_menu_setting"}
]

feature_list["speedy_cooking"] = [
    {"step": 1, "actions": meta_actions_on_number, "variable": "variable_time_cook_time", "comment": "Set cooking time directly using number pads"},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

feature_list["add_30_seconds"] = [
    {"step": 1, "actions": ["press_start_plus_30sec_button"], "variable": "variable_time_cook_time", "comment": "Each press adds 30 seconds to the remaining cooking time"}
]

feature_list["child_lock_control"] = [
    {"step": 1, "actions": ["press_and_hold_stop_cancel_button"], "variable": "variable_child_lock", "comment": "value toggles between locked and unlocked depending on current state"}
]

feature_list["stop_cancel_operation"] = [
    {"step": 1, "actions": ["press_stop_cancel_button"], "variable": "variable_start_running", "comment": "value always set to off"}
]

feature_list["memory_function"] = [
    {"step": 1, "actions": ["press_memory_button"]},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "comment": "This activates a memory cooking procedure if already set"}
]

feature_list["null"] = [
    {"step": 1, "actions": ["press_and_hold_start_plus_30sec_button"], "missing_variables": []}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))