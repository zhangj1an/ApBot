# The provided code already includes the features and variables to execute the user command. Below, we verify the sequence of features and variables needed to complete the command:

# Sequence of features needed to achieve the user command:
# 1. Use the "select_cooking_mode" feature to set the mode to "soup".
#    User manual text: "Press Menu/Cancel to choose ... Soup 🍜"
#    Feature: "select_cooking_mode"
#    Variable: "variable_cooking_mode"

# 2. Use the "adjust_preset_timer" feature to set the preset timer to 3 hours (180 minutes).
#    User manual text: "Press Preset/Timer to set the preset timer. The preset timer should be longer than cooking time. The preset time is up to 24 hours."
#    Feature: "adjust_preset_timer"
#    Variable: "variable_preset_timer"

# 3. Use the "start_cooking" feature to start the machine.
#    User manual text: "Press Start to start the cooking process."
#    Feature: "start_cooking"
#    Variable: "variable_start_running"

# Goal variable values for the user command:
# variable_cooking_mode should be set to "soup".
# variable_preset_timer should be set to 180.
# variable_start_running should be set to "on".

class ExtendedSimulator(Simulator): 
    pass