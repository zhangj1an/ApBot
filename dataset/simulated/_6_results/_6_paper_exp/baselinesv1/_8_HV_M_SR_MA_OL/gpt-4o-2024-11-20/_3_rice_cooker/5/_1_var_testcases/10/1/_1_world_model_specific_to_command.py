# User command:
# Turn on the rice cooker and set to congee mode with a variable_timer set for 1.5 hours. Then start the machine.

# The sequence of features needed:
# 1. Activate "start_appliance" to turn on the appliance (set variable_start_running to "on").
# 2. Use "select_cooking_program" to set variable_cooking_program to "soup_congee" (congee mode).
# 3. Use "adjust_timer" to set variable_timer to 90 minutes (1.5 hours).
# 4. Restart "start_appliance" to initiate the cooking process.

# Relevant user manual text:
# "Press “start” button to start cooking."
# "You can press the button of the program you want to choose directly."
# "Press 'Timer', and set the cooking time you want. Press 'Start' to start cooking."

# Feature list modeled in the code:
# - feature_list["start_appliance"]
# - feature_list["select_cooking_program"]
# - feature_list["adjust_timer"]

# Goal variable values:
# - variable_start_running: "on"
# - variable_cooking_program: "soup_congee"
# - variable_timer: 90

class ExtendedSimulator(Simulator): 
    pass