# User command: Turn on the rice cooker and set to congee mode with a variable_timer set for 1.5 hours. Then start the machine.

# Python comment: The code correctly models the relevant appliance features for the given command.
# Sequence of features needed to achieve this command:
# 1. "start_appliance" to turn on the rice cooker.
# 2. "select_cooking_program" to set the mode to "soup_congee".
# 3. "adjust_timer" to set the timer to 1.5 hours (90 minutes).
# 4. "start_appliance" to start the machine.

# Corresponding user manual text:
# - **Start the appliance:** "Press 'start' to start and power on the machine."
# - **Select cooking program:** "You can press the button of the program you want to choose directly."
# - **Set the timer:** "Press 'Timer' and set the time using buttons."
# - **Start the machine:** "Press 'start' button to start cooking."

# Features referenced in the given code:
# - "start_appliance"
# - "select_cooking_program"
# - "adjust_timer"

# Goal variable values to achieve this command:
# - `variable_start_running`: "on"
# - `variable_cooking_program`: "soup_congee"
# - `variable_timer`: 90

class ExtendedSimulator(Simulator): 
    pass