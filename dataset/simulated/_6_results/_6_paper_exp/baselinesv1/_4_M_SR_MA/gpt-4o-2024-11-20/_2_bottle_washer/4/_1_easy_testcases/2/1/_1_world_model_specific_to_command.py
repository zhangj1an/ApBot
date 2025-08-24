# The current code accurately models the relevant appliance features required for the user command.
# Sequence of features needed to achieve the command:
# 1. Turn on the appliance using "turn_on_off_appliance" feature.
# 2. Select and adjust the "Slow Warm" menu, and set its value to "HI" using the "set_and_adjust_menu" feature.

# Relevant user manual text:
# - "Tap the power button. All options will appear on the screen." (for turning the appliance on).
# - "Tap the menu button until the 'slow' function is selected." 
# - "If any of the bottles have 7 oz of milk or more... use the +/- keys to select the HI setting."
# - "For any other volume of milk, use the LO setting. Note: If you use the LO setting and your milk isn’t warm enough, feel free to try the HI setting."

# Corresponding feature_list names:
# 1. "turn_on_off_appliance"
# 2. "set_and_adjust_menu"

# Goal variable values to achieve the command:
# - Set variable_power_on_off to "on".
# - Set variable_menu_index to "Slow".
# - Set variable_menu_setting (menu corresponding to "Slow") to "HI".

class ExtendedSimulator(Simulator):
    pass