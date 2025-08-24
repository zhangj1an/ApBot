# The current code correctly models the relevant appliance features to achieve the user command:
# Set the mode to cake, set the timer to seven hours, and start the machine.
#
# Sequence of features needed to achieve the command:
# - "set_cooking_mode"
# - "set_preset_timer"
# - "start_running"
#
# Raw user manual text describing each feature:
# 1. For "set_cooking_mode":
# "2. Press Menu/Cancel to select Cake (chef hat) function."
# 2. For "set_preset_timer":
# "The preset time is up to 24 hours."
# "1. Choose a function you need, Press Preset/Timer to set the preset timer. ↳ The preset timer indicator blinks."
# 3. For "start_running":
# "3. Press Start to start the cooking process."
#
# Corresponding feature list names in the given code:
# - Feature name: "set_cooking_mode"
# - Feature name: "set_preset_timer"
# - Feature name: "start_running"
#
# Goal variable values to achieve the command:
# - Set `variable_cooking_mode` to "cake".
# - Set `variable_preset_timer` to 420 (minutes, equivalent to 7 hours).
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator):
    pass