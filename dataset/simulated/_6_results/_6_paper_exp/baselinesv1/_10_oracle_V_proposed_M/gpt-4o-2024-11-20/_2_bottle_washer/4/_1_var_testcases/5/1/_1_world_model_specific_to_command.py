# The current code correctly models the appliance feature to achieve the command “Turn on the appliance and use the steam cooking function for a pear. Set the steam time to 13 minutes.”
# 
# Sequence of features needed to achieve this command:
# 1. "power_on_off" – Turn the appliance on.
# 2. "set_menu_and_adjust_setting" – Set the menu to the "Steam" function and adjust the steam time to 13 minutes.
#
# Relevant user manual text:
# - Power On/Off: "Tap the power button to shut down the appliance."
# - Steam Cooking: "Tap the menu button until the steam function appears. The default time is 12 minutes. Warning: During the steaming process hot steam will escape from the cover - be careful!"
#
# Relevant `feature_list` names in the given code:
# - "power_on_off"
# - "set_menu_and_adjust_setting"
#
# Goal variable values:
# - Set `variable_power_on_off` to "on".
# - Set `variable_menu_index` to "Steam".
# - Set `variable_menu_setting` to 13.

class ExtendedSimulator(Simulator): 
    pass