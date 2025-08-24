# The provided code already accurately models the relevant appliance features. 

# Sequence of features needed to achieve the user command:
# 1. "power_control": Turn the power on (variable_power_on_off).
# 2. "adjust_timer": Set the timer to 8 hours (variable_timer).

# Relevant raw user manual text:
# - "Power Button: Turn air purifier on and off."
# - "Timer Button: Time can be selected from 1, 2, 4, and 8 hours."

# Corresponding feature_list names in the given code:
# - "power_control"
# - "adjust_timer"

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on".
# - Set variable_timer to "8H".

class ExtendedSimulator(Simulator):
    pass