# Python Comment: The current code accurately models the required appliance feature that is used to achieve the user command.  
# The sequence of features needed to achieve this command is as follows:
# Step 1: Use the "power_on_off" feature to power on the bottle warmer.
# Step 2: Use the "set_menu_and_adjust_setting" feature to set the menu to "Quick" and adjust its setting to 3 minutes.
# The goal variable values needed to achieve this command are:
# - Set the variable_power_on_off to "on".
# - Set the variable_menu_index to "Quick".
# - Set the variable_menu_setting_quick to 3 (minutes).
# Based on the user manual and feature list provided, the associated user manual text confirms the correctness:
# - "Tap the power button. All options will appear on the screen."
# - "Tap the menu button until the 'quick' function is selected. The 3-minute default time will appear on the display screen. To adjust the time use the +/- to add or decrease the time."

class ExtendedSimulator(Simulator):
    pass