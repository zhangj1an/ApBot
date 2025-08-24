feature_list = {}

# Feature: Set Auto Menu
feature_list["set_auto_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

# Feature: Set Crust Color
feature_list["set_crust_color"] = [
    {"step": 1, "actions": ["press_crust_colour_button"], "variable": "variable_crust_colour"}
]

# Feature: Set Loaf Size
feature_list["set_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
]

# Feature: Activate Gluten Free Mode
feature_list["set_gluten_free_mode"] = [
    {"step": 1, "actions": ["press_gluten_free_button"], "variable": "variable_gluten_free_mode", "comment": "value always set to on"}
]

# Feature: Set Timer
feature_list["set_timer"] = [
    {"step": 1, "actions": ["press_timer_up_button", "press_timer_down_button"], "variable": "variable_timer_setting"}
]

# Feature: Start or Cancel Operation
feature_list["start_or_cancel"] = [
    {"step": 1, "actions": ["press_start_cancel_button"], "variable": "variable_start_running", "comment": "value always set to on"}
]

# Null Feature
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))