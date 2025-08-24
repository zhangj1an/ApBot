# User Command: Turn on and set the rice cooker to cook congee for 2 hours using the variable_timer. Then start the machine.

# Relevant user manual text:
# - "Congee/Soup: For these programs, you can adjust the cooking time. 
#  1. Select the program, and LED screen will show the default cooking time. 
#  2. Press “Timer”, and set the cooking time you want. 
#  3. Press “Start” to start cooking."

# Relevant features from the given code:
# - Feature: "select_cooking_program", for selecting "congee/soup".
# - Feature: "adjust_timer", for setting the variable_timer.
# - Feature: "start_appliance", for starting the machine.

# The current code already handles this workflow accurately:
# 1. Select the "congee/soup" cooking program using the "press_soup_congee_button".
# 2. Use the "press_timer_button" to adjust the cooking time (variable_timer).
# 3. Use the "press_start_button" to start the machine (variable_start_running).

# Goal variable values:
# - variable_cooking_program: "soup_congee"
# - variable_timer: 120 (representing 2 hours)
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass