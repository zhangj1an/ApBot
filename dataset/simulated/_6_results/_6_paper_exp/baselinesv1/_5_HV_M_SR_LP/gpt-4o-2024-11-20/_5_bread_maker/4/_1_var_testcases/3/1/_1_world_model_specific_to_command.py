# The requested user command involves setting menu, crust color, loaf size, timer, gluten-free mode, and starting the program.
# Based on the provided user manual and existing modeling, the current implementation of features and variables closely
# aligns with the user manual regarding the required command steps. Below is the verification.

# Step 1: Set the menu to "Whole Wheat."
# Relevant feature:
# feature_list["set_auto_menu"] = [
#     {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
# ]
# User manual: "Press the MENU button until the preferred auto menu number is shown on the display screen."

# Step 2: Set crust color to "Dark."
# Relevant feature:
# feature_list["adjust_crust_color"] = [
#     {"step": 1, "actions": ["press_crust_colour_button"], "variable": "variable_crust_color"}
# ]
# User manual text: "To change the crust colour, press the CRUST COLOUR button repeatedly to cycle through Light, Medium, Dark (and Rapid) on the display screen."

# Step 3: Set loaf size to "900g."
# Relevant feature:
# feature_list["adjust_loaf_size"] = [
#     {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
# ]
# User manual text: "To change the loaf size, press the LOAF SIZE button repeatedly to cycle through 450g, 680g or 900g on the display screen."

# Step 4: Turn on gluten-free mode.
# Relevant feature:
# feature_list["activate_gluten_free_mode"] = [
#     {"step": 1, "actions": ["press_gluten_free_button"], "variable": "variable_gluten_free_mode"}
# ]
# User manual text: "Press the GLUTEN FREE button on the control panel. GLUTEN FREE will display on the screen."

# Step 5: Set a 3-hour delay.
# Relevant feature:
# feature_list["adjust_timer"] = [
#     {"step": 1, "actions": ["press_timer_up_button", "press_timer_down_button"], "variable": "variable_timer"}
# ]
# User manual text: "Press up arrow to increase the time in 10-minute increments or press down arrow to decrease the time in 10-minute increments."

# Step 6: Start the appliance.
# Relevant feature:
# feature_list["start_or_cancel_program"] = [
#     {"step": 1, "actions": ["press_start_cancel_button"], "variable": "variable_start_running", "comment": "value always set to on or off"},
# ]
# User manual text: "Press START/CANCEL when selections are complete to begin the program."

# Based on the user manual description and the given feature_list, the current implementation is accurate, and all relevant appliance features are correctly modeled.

# Goal variable values to execute the user command:
goal_variable_values = {
    "variable_menu_index": "Whole Wheat",
    "variable_crust_color": "Dark",
    "variable_loaf_size": "900g",
    "variable_timer": "03:00:00",
    "variable_gluten_free_mode": "on",
    "variable_start_running": "on",
}

class ExtendedSimulator(Simulator):
    pass