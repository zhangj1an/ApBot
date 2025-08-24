# The existing code correctly models the required appliance features for the given user command:
# - "Set the mode to congee": This is covered by the `select_cooking_mode` feature using the `variable_cooking_mode`.
# - "Starting 12 hours from now": This is covered by the `adjust_preset_timer` feature using the `variable_preset_timer`.
# - "Start the machine": This is covered by the `start_cooking` feature using the `variable_start_running`.

# Relevant features and user manual excerpts:
# - "Press Menu/Cancel to choose Congee": This sets the variable `variable_cooking_mode`.
# - "Press Preset/Timer to set the preset timer": This adjusts the variable `variable_preset_timer` in increments of 15 minutes.
# - "Press Start to start the cooking process": This sets `variable_start_running` to "on".

# Sequence of features needed to achieve the command:
# 1. "select_cooking_mode" to set the mode to "congee"
# 2. "adjust_preset_timer" to set the preset timer to 12 hours (720 minutes)
# 3. "start_cooking" to start the machine

# Goal variable values to achieve this command:
# - `variable_cooking_mode`: "congee"
# - `variable_preset_timer`: 720 (in minutes)
# - `variable_start_running`: "on"

class ExtendedSimulator(Simulator): 
    pass