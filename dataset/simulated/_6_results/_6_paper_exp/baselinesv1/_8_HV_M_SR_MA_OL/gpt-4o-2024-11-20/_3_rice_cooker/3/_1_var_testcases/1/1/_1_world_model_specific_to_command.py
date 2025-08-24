# The provided code correctly models the relevant appliance features to achieve the described command.
# The command requires the following sequence of features and steps:

# 1. Use the "adjust_delay_timer" feature to set the delay time to 30 minutes.
#    - User Manual Text: "Press Delay Timer to delay the start of your cooker cycle. Use + and - to increase or decrease the desired start time, in increments of 30 minutes."
#    - Feature: feature_list["adjust_delay_timer"]

# 2. Use the "set_menu" feature to select White Rice mode.
#    - User Manual Text: "Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected."
#    - Feature: feature_list["set_menu"]

# 3. Use the "start_cooking" feature to start the rice cooker.
#    - User Manual Text: "Press Start to start cooking."
#    - Feature: feature_list["start_cooking"]

# The required goal variable values:
# - Set variable_delay_timer to "30".
# - Set variable_menu_index to "White Rice".
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass