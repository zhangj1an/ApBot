# The given code correctly models the relevant appliance features needed to achieve the user command.

# Relevant sequence of features needed:
# 1. Select "SOUP" from the menu using the "set_menu" feature, setting variable_menu_index to "soup".
# 2. Set the cooking delay to 3 hours using the "set_delay_time" feature, modifying variable_delay_time to 3.
# 3. Start the machine using the "start_cooking" feature, setting variable_start_running to "on".

# Raw user manual text describing the relevant features:
# - "Close the lid, select Quick Rice or other functions by using the Quick Rice or MENU button."
# - "Press the “DELAY” button, the Time Display flashes, and then press the button “DELAY” again to adjust the displayed reservation time."
# - "Press the “START” button, the cooking will be finished at the appointed time."

# Feature list in the provided code:
# - "set_menu" for selecting variable_menu_index (e.g., "soup").
# - "set_delay_time" for adjusting variable_delay_time.
# - "start_cooking" for starting the cooking process by setting variable_start_running.

# Goal variable values to achieve this command:
# - variable_menu_index = "soup"
# - variable_delay_time = 3
# - variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass