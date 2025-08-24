# The code accurately models the required features and variables described in the user manual. 
# The sequence of features needed to achieve the user command is:
# 1. "set_menu": To set the rice cooker to Quinoa mode.
# 2. "set_menu" (step 2): To adjust the cooking time to 35 minutes for the Quinoa mode.
# 3. "start_cooking": To start running.

# Raw user manual text that describes the features:
# 1. "Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected."
# 2. "Use + and - if you want to adjust time."
# 3. "Press to start cooking."

# Relevant features in the current code:
# - feature_list["set_menu"]
# - feature_list["start_cooking"]

# Goal variable values to achieve the command:
# - Set `variable_menu_index` to "Quinoa".
# - Set `variable_menu_setting` to 35 (time in minutes).
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass