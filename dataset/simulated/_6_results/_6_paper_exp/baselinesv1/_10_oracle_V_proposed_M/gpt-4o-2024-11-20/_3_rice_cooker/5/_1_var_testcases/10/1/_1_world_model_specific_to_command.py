# Based on the user manual and given code, the following sequence of features and variable adjustments from the existing code can achieve the command.

# Sequence of Features to Achieve the User Command:
# 1. Select "congee mode" (soup_congee cooking program) by using the "select_cooking_program" feature.
# 2. Set the timer to 1.5 hours (90 minutes) using the "adjust_timer" feature.
# 3. Turn on the appliance (start running) using the "start_running" feature.

# Relevant User Manual Text for Each Feature:
# - Select Cooking Program: "You can press the button of the program you want to choose directly, and the light of the selected program will be on."
# - Timer Adjustment: "For these programs, you can adjust the cooking time. Select the program, and LED screen will show the default cooking time."
# - Start Running: "Press 'start' button to start cooking."

# Relevant Feature List:
# - "select_cooking_program": Responsible for selecting the cooking mode.
# - "adjust_timer": Responsible for setting the timer.
# - "start_running": Responsible for starting the rice cooker.

# Goal Variable Values:
# - variable_cooking_program = "soup_congee"
# - variable_timer = 90
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass