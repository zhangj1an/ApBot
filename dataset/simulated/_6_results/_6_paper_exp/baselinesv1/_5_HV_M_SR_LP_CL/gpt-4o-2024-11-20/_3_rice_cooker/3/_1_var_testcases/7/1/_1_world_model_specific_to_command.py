# Based on the user command, we verify that the provided code already includes adequate features to achieve the task:
# 1. Select the "Quinoa" cooking menu. 
# Feature: "set_menu" allows selecting the menu (step 1) and adjusting the cooking time (step 2).
# User Manual Reference: "Press menu button to scroll through preset functions: White Rice, Brown Rice, Quinoa, Steel Cut Oats.”
# 
# 2. Reduce the cooking time to 20 minutes.
# Feature: "set_menu" step 2 allows adjusting cooking times using the plus or minus buttons.
# 3. Start cooking.
# Feature: "start_cooking" explicitly enables starting the cooking process through the "press_start_button" action.
# User Manual Reference: "Press Start to start cooking."
#
# Goal variable values to achieve the command:
# - Set `variable_menu_index` to "Quinoa".
# - Set `variable_menu_setting_quinoa` to 20.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass