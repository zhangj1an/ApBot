# User command: Turn on the dehumidifier and set the timer to run for 2 hours.

# Checking relevant features and variables:
# From the given feature_list and user manual, we need:
# 1. To turn on the appliance using the "power_on_off" feature, toggle `variable_power_on_off` to "on".
# 2. To set the timer to 2 hours using the "set_timer" feature, toggle `variable_timer` to "2H".

# Relevant user manual text:
# - **Power Button**: Turn air purifier on and off.
# - **Timer Button**: Time can be selected from 1, 2, 4, and 8 hours.

# Given feature_list names:
# - "power_on_off"
# - "set_timer"

# Sequence of features needed to achieve the command:
# 1. Use "power_on_off", action "press_power_button" to set `variable_power_on_off` to "on".
# 2. Use "set_timer", action "press_timer_button" to set `variable_timer` to "2H".

# Goal variable values:
# variable_power_on_off = "on"
# variable_timer = "2H"

class ExtendedSimulator(Simulator): 
    pass