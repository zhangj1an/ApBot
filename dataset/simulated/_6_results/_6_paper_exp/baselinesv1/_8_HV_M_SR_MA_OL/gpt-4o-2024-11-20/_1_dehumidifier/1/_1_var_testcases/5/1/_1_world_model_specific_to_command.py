# Based on the user command: Switch on the dehumidifier and start air swing.

# The given code already correctly models relevant features for this command.
# Sequence of required features:
# 1. "power_on_off"
# 2. "adjust_air_swing"

# User manual for switching on the dehumidifier:
# "Press POWER, the Dehumidifier Starts Operation."
# Associated feature_list name: "power_on_off"

# User manual for starting air swing:
# "SWING: start air swing function to realize wide-angle air sweeping."
# Associated feature_list name: "adjust_air_swing"

# Goal variable values:
# 1. Set "variable_power_on_off" to "on"
# 2. Set "variable_air_swing" to "on"

class ExtendedSimulator(Simulator): 
    pass