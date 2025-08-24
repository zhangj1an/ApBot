feature_list = {}

# Feature: Set program/menu for breadmaking
feature_list["set_menu"] = [
    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
]

# Feature: Adjust loaf size
feature_list["adjust_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
]

# Feature: Adjust crust color
feature_list["adjust_crust_color"] = [
    {"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color"}
]

# Feature: Adjust timer-related variables (combined feature)
feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["press_time_up_button", "press_time_down_button"],
     "variable": "variable_timer_delay", 
     "comment": "This feature also covers adjusting extra bake time conditionally for menu 12 if applicable."}
]

# Feature: Start or Stop the appliance
feature_list["start_stop"] = [
    {
        "step": 1,
        "actions": ["press_start_stop_button"], 
        "variable": "variable_start_running", 
        "comment": "value always set to 'on' if starting, or 'off' if stopping."
    }
]

# Null feature for unused actions or variables
feature_list["null"] = [{"step": 1, "actions": [], "missing_variables": []}]

# Initialize the Feature object
simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))