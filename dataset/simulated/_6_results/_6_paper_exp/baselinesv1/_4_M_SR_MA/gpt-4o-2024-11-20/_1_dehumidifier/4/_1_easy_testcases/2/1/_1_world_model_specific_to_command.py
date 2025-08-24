# The given code correctly models the features described in the user manual to achieve the task of powering on the appliance and setting the timer to '2H'. Below is the sequence of features required and raw user manual text to support this:

# Sequence of features:
# 1. Use the "power_on_off" feature to turn on the appliance.
# 2. Use the "set_timer" feature to set the timer to '2H'.

# Raw user manual text describing the relevant features:
# - "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
# - "The air purifier can be set to operate for timed intervals of 2 hours, 4 hours and 8 hours, stopping automatically when the selected operating time has elapsed."
# - Feature names in the given codebase: "power_on_off" and "set_timer".

# Goal variable values to achieve the required user command:
# - `variable_power_on_off`: Set to "on".
# - `variable_timer`: Set to "2H".

class ExtendedSimulator(Simulator): 
    pass