# The given code does model the required appliance features accurately according to the user manual
# Here is the sequence of features needed to achieve this command:
# 1. Use the "power_on_off" feature to switch the bottle warmer on by pressing the power button.
# 2. Use the "set_menu_and_adjust_setting" feature to select the sterilize function by pressing the menu button.
# 3. Use the "+" button in the "set_menu_and_adjust_setting" feature to set the cycle time to 20 minutes.

# Relevant user manual texts:
# - "Tap the power button then tap the menu button until the sterilizer option appears."
# - "The sterilizer function has three settings 10, 15, and 20 minutes. Use +/- to adjust the time."
# - "Tap the power button to shut down the appliance."

# feature_list names in the given code:
# - "power_on_off"
# - "set_menu_and_adjust_setting"

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on".
# - Set variable_menu_index to "Sterilize".
# - Set variable_menu_setting_sterilize to "20".

class ExtendedSimulator(Simulator): 
    pass