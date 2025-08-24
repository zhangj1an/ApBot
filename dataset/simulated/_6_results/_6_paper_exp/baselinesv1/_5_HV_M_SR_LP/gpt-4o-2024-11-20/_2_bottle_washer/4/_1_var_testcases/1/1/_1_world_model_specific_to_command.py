# The current code accurately models the features required to turn on the appliance, set the "Quick Warm" menu, and adjust its time to 3 minutes for the intended user command.

# Sequence of features needed:
# 1. Turn on the appliance using feature "turn_on_off_appliance."
# 2. Set the "Quick Warm" menu using feature "set_and_adjust_menu."
# 3. Adjust the default time (3 minutes) if needed using the same feature: "set_and_adjust_menu."

# Raw user manual text:
# - KNOW YOUR BOTTLE WARMER
# - QUICK WARM FUNCTION: "Tap the power button. All options will appear on the screen."
# - "Tap the menu button until the 'quick' function is selected. The 3-minute default time will appear on the display screen. To adjust the time, use the +/- keys to add or decrease the time."

# Corresponding feature_list in the given code:
# - "turn_on_off_appliance" for power control: {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
# - "set_and_adjust_menu" for selecting the "Quick Warm" menu and adjusting its settings.

# Goal variable values:
# - variable_power_on_off: "on"
# - variable_menu_index: "Quick"
# - variable_menu_setting_quick: 3

class ExtendedSimulator(Simulator): 
    pass