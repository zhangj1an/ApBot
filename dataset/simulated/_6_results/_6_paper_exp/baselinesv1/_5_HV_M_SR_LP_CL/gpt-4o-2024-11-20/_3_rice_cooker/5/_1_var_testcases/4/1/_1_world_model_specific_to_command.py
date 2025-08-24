# The given code already accurately models the requested features, variables, and actions required to achieve the user command.
# Sequence of features needed to achieve the command:
# 1. "select_cooking_program" to set the rice cooker to cook congee.
#    - Relevant user manual text: “For these programs, you can adjust the cooking time." (describing Congee setting and adjustability of time)
#    - Feature list name: "select_cooking_program".
# 2. "adjust_timer" to set the timer to 2 hours.
#    - Relevant user manual text: “Press ‘Timer’, and set the cooking time you want."
#    - Feature list name: "adjust_timer".
# 3. "start_appliance" to start the machine.
#    - Relevant user manual text: “Press ‘Start’ button to start cooking."
#    - Feature list name: "start_appliance".

# Goal variable values to achieve this command:
# - Set variable_cooking_program to "soup_congee".
# - Set variable_timer to 120 (representing 2 hours).
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass