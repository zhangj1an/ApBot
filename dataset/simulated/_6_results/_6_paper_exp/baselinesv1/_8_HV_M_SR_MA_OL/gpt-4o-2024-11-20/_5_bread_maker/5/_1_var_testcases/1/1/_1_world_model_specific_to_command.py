# User Command Analysis and Checking the Existing Code:

# The requested user action involves:
# 1. Selecting the Quick program: The variable for menu selection (variable_menu_index) and feature "set_menu" exist.
# 2. Choosing loaf size to be 700g: The variable for loaf size (variable_loaf_size) and feature "set_loaf_size" exist.
# 3. Setting crust color to Light: The variable for crust color (variable_crust_color) and feature "set_crust_color" exist.
# 4. Setting the delay timer for 11 hours: The variable for delay timer (variable_delay_timer) and feature "set_delay_timer" exist. However, the delay timer's step adjustments (ContinuousVariable) are modeled correctly already.
# 5. Power on and start the bread maker operation: Starting and stopping programs through the variable (variable_start_running) and feature "start_stop_program" exist.

# The code correctly models all required features based on the user manual. It has clearly defined actions for each step, and all variables and actions necessary for the user command are present.

# Sequence of Features to Achieve the User Command:
# 1. Feature Name: "set_menu"
#     - Select the Quick program using the "press_menu_button".
# 2. Feature Name: "set_loaf_size"
#     - Select the loaf size to 700g using "press_loaf_size_button".
# 3. Feature Name: "set_crust_color"
#     - Set the crust color to Light using "press_color_button".
# 4. Feature Name: "set_delay_timer"
#     - Set the delay timer to 11 hours using the "press_time_plus_button".
# 5. Feature Name: "start_stop_program"
#     - Start the bread maker operation using "press_start_stop_button".

# Relevant User Manual Text:
# 1. "Choose a Programme with the MENU button."
# 2. "Press LOAF SIZE button to select the Loaf Size (as needed)."
# 3. "Press COLOR button to select the Crust Colour (as needed)."
# 4. "Use the delay timer function to delay the completion of your bread. To set the Timer, set the desired time."
# 5. "Press START/STOP button to start or stop the Programmes."
# 6. "The appliance will beep 10 times and start baking the bread."

# Relevant Feature List Names in the Given Code:
# Feature List Names: ["set_menu", "set_loaf_size", "set_crust_color", "set_delay_timer", "start_stop_program"]

# Goal Variable Values to Achieve the Command:
# 1. Set variable_menu_index to "4" (Quick program).
# 2. Set variable_loaf_size to "700g".
# 3. Set variable_crust_color to "Light".
# 4. Set variable_delay_timer to 660 minutes (11 hours).
# 5. Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass