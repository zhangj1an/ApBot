# Python comments explaining step sequences, features, and goal variables:

# Sequence of features needed to achieve the user command:
# 1. Use "set_menu" feature to select the program to Whole Wheat (menu 3).
# 2. Use "set_loaf_size" feature to set the loaf size to 900g.
# 3. Use "set_crust_color" feature to set the crust color to Dark.
# 4. Use "set_delay_timer" feature to set the timer to 6 hours (360 minutes).
# 5. Use "start_stop_program" feature to ensure the bread maker starts (set to "on").

# Relevant raw user manual text and corresponding feature_list:
# - Set Menu: "Choose a Programme with the MENU button."
# - Feature: "set_menu"
# - Set Loaf Size: "Press LOAF SIZE button to select the Loaf Size (as needed)."
# - Feature: "set_loaf_size"
# - Set Crust Color: "Press COLOR button to select the Crust Colour (as needed)."
# - Feature: "set_crust_color"
# - Set Delay Timer: "To set the Timer, determine when you would like your bread to be ready, then set the Timer."
# - Feature: "set_delay_timer"
# - Start Program: "Press START/STOP button to start the breadmaker."
# - Feature: "start_stop_program"

# Goal variable values to achieve the user command:
# - variable_menu_index: "3" (Whole Wheat program)
# - variable_loaf_size: "900g"
# - variable_crust_color: "Dark"
# - variable_delay_timer: 360 (6 hours in minutes)
# - variable_start_running: "on" (start the program)

class ExtendedSimulator(Simulator):
    pass