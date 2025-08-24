# The given code is accurate in modeling the steps to perform relevant tasks for the aforementioned user command.
# The needed user command sequence and corresponding actions are already well-covered in the current code.
# 
# Relevant User Manual Text:
# 1. **QUICK WARM FUNCTION:** 
#    - The function uses steam to warm the bottle as fast as possible.
#    - Step-by-step instructions are detailed, including "Tap the menu button until the 'quick' function is selected" 
#      and "To adjust the time use the +/- to add or decrease the time."
# 
# Feature Coverage:
# - Turn on the bottle warmer is achieved with the feature `turn_on_off_appliance`.
# - Setting the "Quick Warm" function mode and adjusting its time are covered under `set_and_adjust_menu`.
#
# Sequence of Features Needed:
# 1. `"turn_on_off_appliance"`: Turn the bottle warmer ON by pressing the power button.
# 2. `"set_and_adjust_menu"`: Select the "Quick" mode using the menu button and adjust its time to 3 minutes using the +/- buttons.
# 
# Goal Variable Values:
# - `variable_power_on_off`: Set to "on".
# - `variable_menu_index`: Set to "Quick".
# - `variable_menu_setting_quick`: Set to 3.

# Since the current Simulator correctly models everything, no changes are necessary.
class ExtendedSimulator(Simulator): 
    pass