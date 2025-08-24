# The current code correctly models the relevant appliance features needed to achieve the command. 
# Sequence of features needed to achieve this command:
# 1. "turn_on_off_appliance": Turn on the appliance. (Set variable_power_on_off to "on").
# 2. "set_and_adjust_menu": Select the "Steam" function and set the steam time to 13 minutes.

# Relevant user manual text:
# - For turning on/off: "Tap the power button to shut down the appliance."
# - For selecting and adjusting menu:
#   - "Tap the menu button to cycle through various function modes ("Quick", "Slow", "Defrost", "Sterilize", "Steam", "Preset")."
#   - "The steam function uses steam cooking at a time adjustable setting (default 12 minutes, adjustable using +/-)."

# Corresponding feature_list names in the given code:
# 1. "turn_on_off_appliance"
# 2. "set_and_adjust_menu"

# Goal variable values to achieve this command:
# Set variable_power_on_off to "on".
# Set variable_menu_index to "Steam".
# Set variable_menu_setting to 13.

class ExtendedSimulator(Simulator):
    pass