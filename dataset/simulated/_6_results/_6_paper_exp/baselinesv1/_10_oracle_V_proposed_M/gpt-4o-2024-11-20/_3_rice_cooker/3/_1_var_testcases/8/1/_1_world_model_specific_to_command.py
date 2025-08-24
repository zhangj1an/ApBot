# The current code accurately models the relevant appliance features to achieve the given command.
# 
# Sequence of features needed:
# 1. "set_menu" to set the menu to "Quinoa" and adjust its cooking time to 35 minutes.
# 2. "start_cooking" to start running the appliance.
#
# Relevant user manual text:
# "Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected. Press start if cooking time is okay. Use + and - if you want to adjust time."
# 
# Feature list names in the given code:
# - "set_menu"
# - "start_cooking"
#
# Goal variable values to achieve this command:
# - variable_menu_index: "Quinoa"
# - variable_menu_setting: 35
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass