# Python comments listing findings and goals:
# The sequence of features needed to achieve the user command is:
# 1. "select_cooking_program" to set the rice cooker into "quick cooking steam mode".
# 2. "adjust_timer" to set the variable_timer to 20 minutes.
# 3. "start_appliance" to set the variable_start_running to "on".
#
# Relevant user manual text:
# - "Press the button of the program you want to choose directly, and the light of the selected program will be on."
# - "Press 'Timer', and set the cooking time you want."
# - "Press 'Start' button to start cooking."
#
# Corresponding feature_list names in the given code:
# - select_cooking_program
# - adjust_timer
# - start_appliance
#
# Goal variable values to achieve this command:
# - variable_cooking_program = "quick_cooking_steam"
# - variable_timer = 20
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass