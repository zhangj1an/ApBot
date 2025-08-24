# The current code correctly models the relevant appliance features described in the user manual.
# Here is the sequence of features and steps required to achieve the user command to adjust the delay timer to 30 minutes,
# set the rice cooker to White Rice mode, and start running:

# 1. "adjust_delay_timer"
# - Step 1: Press the "press_delay_timer_button" to enter the delay timer adjustment mode.
# - Step 2: Use "press_plus_button" or "press_minus_button" to set the delay timer to 30 minutes.

# 2. "set_menu"
# - Step 1: Press "press_menu_button" to select the White Rice mode.
# - Step 2: Use "press_plus_button" or "press_minus_button" to adjust any additional menu-specific settings (if applicable).

# 3. "start_cooking"
# - Step 1: Press the "press_start_button" to begin the cooking process.

# Relevant raw user manual text:
# - "Press Delay Timer to delay the start of your cooker cycle. Use + and - to increase or decrease the desired start time, in increments of 30 minutes. Delay can be from 1 - 24 hours."
# - "Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected. Press start if cooking time is okay. Use + and - if you want to adjust time."
# - "Press to start cooking."

# Features List:
# - "adjust_delay_timer"
# - "set_menu"
# - "start_cooking"

# The goal variable values to achieve the command are:
# - Set `variable_delay_timer` to "0.5" (30 minutes).
# - Set `variable_menu_index` to "White Rice".
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass