# User Command: Switch on the dehumidifier and set the timer for 2 hours.
# Relevant user manual text:
# 1. "Turns the unit on and off."
# 2. "Sets an Auto-On or Shut-Off timer, 1H, 2H or 4H."
# 
# Sequence of features from the given code to achieve this command:
# 1. Feature "power_control" to switch on the dehumidifier.
# 2. Feature "adjust_timer" to set a 2-hour timer.
#
# Goal Variable Values:
# - Set variable_power_on_off to "on".
# - Set variable_timer to "2".

class ExtendedSimulator(Simulator): 
    pass