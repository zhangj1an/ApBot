# The existing code already models the required features accurately to achieve the user's specified command.

# User Command: Turn on the cooker and set it to brown rice mode for a preset time of 5 hours. Then start the machine.
# The sequence of features required to achieve this command:
# 1. Feature: "start_appliance" (to turn on the appliance)
# 2. Feature: "select_cooking_program" (to set the cooker to brown rice mode)
# 3. Feature: "adjust_preset_time" (to set the preset time to 5 hours)
# 4. Feature: "start_appliance" (to start the machine)

# Relevant raw user manual text:
# 1. "Press 'Start' to turn the appliance on."
# 2. "You can press the button of the program you want to choose directly..."
# 3. "When the cooking program is chosen... press the 'Preset' button to set the time for finishing cooking."
# 4. "Press 'Start' button to start cooking."

# Feature List Names in the Given Code:
# 1. "start_appliance" for turning on the appliance
# 2. "select_cooking_program" for selecting the cooking program
# 3. "adjust_preset_time" for setting preset time
# 4. "start_appliance" for starting the machine

# Goal Variable Values:
# - Set `variable_start_running` to "on"
# - Set `variable_cooking_program` to "brown_rice"
# - Set `variable_preset_time` to "300" (as 5 hours = 5 * 60 minutes)

class ExtendedSimulator(Simulator): 
    pass