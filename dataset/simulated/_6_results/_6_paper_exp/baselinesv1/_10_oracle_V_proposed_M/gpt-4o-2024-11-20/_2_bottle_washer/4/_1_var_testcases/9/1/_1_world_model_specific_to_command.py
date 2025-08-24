# Python comments specifying sequence of features, relevant user manual text, and corresponding feature_list names:

# Sequence of features needed to achieve the command:
# 1. Power on the bottle warmer:
#    - Feature: "power_on_off"
#    - Action: press_power_button
#    - User Manual Text: "Tap the power button to shut down the appliance."
# 2. Set the menu to "Sterilize" and adjust the sterilizing time to 15 minutes:
#    - Feature: "set_menu_and_adjust_setting"
#    - Actions: press_menu_button (to select "Sterilize"), press_plus_button / press_minus_button (to adjust time to 15 minutes)
#    - User Manual Text: "Tap the menu button to cycle through various function modes ('Quick', 'Slow', 'Defrost', 'Sterilize', 'Steam', 'Preset'). The sterilizer function has three settings 10, 15, and 20 minutes. Use +/- to adjust the time."

# Relevant feature_list names:
# - Feature 'power_on_off': Handles power on/off using 'press_power_button'.
# - Feature 'set_menu_and_adjust_setting': Allows cycling through menu options and adjusting the menu setting using 'press_menu_button', 'press_plus_button', and 'press_minus_button'.

# Goal variable values to achieve this command:
# - variable_power_on_off: Set to "on".
# - variable_menu_index: Set to "Sterilize".
# - variable_menu_setting: Set to 15 (for sterilize function).

class ExtendedSimulator(Simulator): 
    pass