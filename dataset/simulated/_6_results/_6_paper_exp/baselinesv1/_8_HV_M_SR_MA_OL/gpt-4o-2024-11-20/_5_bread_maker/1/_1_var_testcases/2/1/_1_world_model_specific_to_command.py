# The given code correctly models the relevant features of the appliance based on the user manual as follows:
# Sequence of features needed to achieve the user command:
# 1. Adjust the bread maker's menu to "French bread" using feature "adjust_menu".
# 2. Adjust the crust color to "Dark" using feature "adjust_crust_color".
# 3. Adjust the loaf size to "2.0LB" using feature "adjust_loaf_size".
# 4. Set the delay timer to 6 hours using feature "adjust_delay_time".
# 5. Start the bread maker using feature "start_stop_bread_maker".

# Relevant user manual text:
# - "The Menu button is used to select a program. Each time it is pressed, the program will vary."
# - "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
# - "Press this button to select the desired size of the loaf."
# - "Use this button to delay the start time for your desired program."
# - "START/STOP: This button is used for starting and stopping the selected baking program."

# Features in the given code:
# - "adjust_menu" for menu selection.
# - "adjust_crust_color" for crust color selection.
# - "adjust_loaf_size" for loaf size selection.
# - "adjust_delay_time" for setting the delay timer.
# - "start_stop_bread_maker" for starting/stopping the bread maker.

# Goal variable values:
# - variable_menu_index = "French"
# - variable_crust_color = "Dark"
# - variable_loaf_size = "2.0LB"
# - variable_delay_time = 360 (6 hours).
# - variable_start_running = "on".

# Existing features correctly model the appliance, so no modification is necessary. Below is the extended simulator with no changes.

class ExtendedSimulator(Simulator): 
    pass