# The given code correctly models the relevant appliance feature necessary to achieve the user command.

# Sequence of features required to achieve the command:
# 1. Feature "power_on_off" is used to turn on the appliance.
#    Raw user manual text: "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
#    Feature name in the given code: "power_on_off"
#
# 2. Feature "set_timer" is used to set the timer to '8H'.
#    Raw user manual text: "The air purifier can be set to operate for timed intervals of 2 hours, 4 hours and 8 hours, stopping automatically when the selected operating time has elapsed."
#    Feature name in the given code: "set_timer"

# Goals for variable values:
# - Set `variable_power_on_off` to "on".
# - Set `variable_timer` to "8H".

class ExtendedSimulator(Simulator): 
    pass