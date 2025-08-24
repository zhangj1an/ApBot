# User command: Cook 'PORRIDGE' with a reserved start time of 1 hour from now, then start the machine.

# Step 1: Check the given code's feature list against the user manual.

# 1. The code has a feature "set_menu" to adjust the cooking mode to PORRIDGE via "press_menu_button".
# 2. The code has a feature "set_delay_time" where delay time (reservation time) can be set.
# 3. The code has a feature "start_cooking" with "press_start_button", which sets the machine to start mode.

# The sequence of features in the given code leads to the needed steps:
# a. Adjust menu to PORRIDGE using the "set_menu" feature.
# b. Set a delay time of 1 hour using the "set_delay_time" feature.
# c. Start cooking using the "start_cooking" feature.

# Relevant user manual text:
# - "Select Quick Rice or other functions using the Quick Rice or MENU button." This confirms adjusting the cooking mode (related to set_menu).
# - "Press the ‘DELAY’ button... to adjust the displayed reservation time." This confirms setting delay time (related to set_delay_time).
# - "Press the ‘START’ button, the cooking will be finished at the appointed time." This confirms starting the cooking process (related to start_cooking).

# Hence, the provided code has accurately modeled the appliance features required for this task.

# Sequence of features to achieve this command:
# 1. Use "set_menu" to set the menu to PORRIDGE.
# 2. Use "set_delay_time" to set the reservation/start time to 1 hour.
# 3. Use "start_cooking" to start the machine.

# Goal variable values:
# - Set "variable_menu_index" to "porridge".
# - Set "variable_delay_time" to 1.
# - Set "variable_start_running" to "on".

class ExtendedSimulator(Simulator): 
    pass