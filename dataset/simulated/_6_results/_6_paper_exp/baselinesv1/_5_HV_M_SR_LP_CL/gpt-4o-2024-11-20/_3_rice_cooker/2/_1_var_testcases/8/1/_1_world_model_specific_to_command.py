# The existing code has correctly modeled the relevant features to fulfill the user command.
# Here is the sequence of the features required, along with the goal variables to achieve this command:

# Sequence of features needed:
# 1. "select_cooking_mode" - Set the cooking mode to "soup".
# 2. "adjust_preset_timer" - Set the timer to 6 hours (360 minutes).
# 3. "start_cooking" - Start the machine.

# Relevant raw user manual text:
# - "Press 'Menu/Cancel' to choose a cooking mode such as Fast cook, White rice, Congee, Soup, Cake, Keep warm."
# - "Choose a function you need, Press Preset/Timer to set the preset timer."
# - "Press Start to confirm. The rice cooker starts working at the selected mode."

# Feature list names in the given code:
# - "select_cooking_mode"
# - "adjust_preset_timer"
# - "start_cooking"

# Goal variable values:
# - Set `variable_cooking_mode` to "soup".
# - Set `variable_preset_timer` to 360.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass