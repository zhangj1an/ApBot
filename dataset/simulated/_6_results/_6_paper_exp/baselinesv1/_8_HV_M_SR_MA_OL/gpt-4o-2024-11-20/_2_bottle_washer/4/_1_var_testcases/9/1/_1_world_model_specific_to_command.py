# The given code correctly models the necessary appliance features to fulfill the user command.
# The required sequence of features is as follows:
# 1. Turn on the appliance using the "turn_on_off_appliance" feature, which toggles the power state.
#    - Raw user manual text: "Tap the power button then tap the menu button until the sterilizer option appears."
#    - Feature list in the code: "turn_on_off_appliance"
#    - Goal value: Set `variable_power_on_off` to "on".
#
# 2. Select the "Sterilize" menu option and configure the sterilizer time, using the "set_and_adjust_menu" feature.
#    - Step 1: Use `press_menu_button` to set `variable_menu_index` to "Sterilize".
#    - Step 2: Use `press_plus_button` or `press_minus_button` to adjust the time to 15 minutes.
#    - Raw user manual text: "Tap the menu button until the sterilizer option appears. The default time is 15 minutes. The sterilizer function has three settings 10, 15, and 20 minutes. Use +/- to adjust the time."
#    - Feature list in the code: "set_and_adjust_menu"
#    - Goal values: Set `variable_menu_index` to "Sterilize" and `variable_menu_setting` (`variable_menu_setting_sterilize`) to "15".

class ExtendedSimulator(Simulator):
    pass