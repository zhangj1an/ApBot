# The provided code already models the relevant appliance features needed to achieve the user command.
# Below are the relevant user manual texts and the sequence of features required.

# Relevant user manual text:
# 1. "**Power On/Off:** Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
# 2. "**Timer:** The air purifier can be set to operate for timed intervals of 2 hours, 4 hours, and 8 hours, stopping automatically when the selected operating time has elapsed."
# 
# Sequence of features needed to achieve the command:
# Feature 1: "power_on_off"
# Feature 2: "set_timer"
# 
# From the given `feature_list`, use:
# Feature name: **"power_on_off"** to toggle the power on.
# Feature name: **"set_timer"** to adjust the timer to '4H'.
# 
# Goal variable values to achieve this command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_timer` to "4H".

class ExtendedSimulator(Simulator): 
    pass