# The current code accurately represents the user manual features relevant to the user command.

# User command: Turn on and cook brown rice with a preset finish time in 9 hours. Then start the machine.
# Sequence of features needed to achieve the command:
# 1. Select the cooking program to "brown rice" using the "select_cooking_program" feature.
# 2. Adjust the preset time to 540 minutes (9 hours) using the "adjust_preset_time" feature.
# 3. Start the appliance by setting the "start_running" variable to "on" using the "start_appliance" feature.

# User manual text corresponding to the relevant features:
# - Selecting the cooking program:
#   "*You can press the button of the program you want to choose directly, and the light of the selected program will be on.*"
# - Adjusting the preset time:
#   "*When the cooking program is chosen (not available on 'Clay Pot', 'Reheat' and 'Keep Warm'), press the 'Preset' button to set the time for finishing cooking.*"
# - Starting the machine:
#   "*Press 'start' button to start cooking.*"

# Corresponding feature list names in the provided code:
# 1. "select_cooking_program"
# 2. "adjust_preset_time"
# 3. "start_appliance"

# The target goal variable values to achieve this command:
# - Set `variable_cooking_program` to "brown_rice".
# - Set `variable_preset_time` to 540 (equivalent to 9 hours).
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass