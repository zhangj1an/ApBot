# The provided code accurately models the necessary appliance features to achieve the user command to set the rice cooker menu to "Quinoa," adjust the cooking time to 20 minutes, and start running. 

# Sequence of features needed to achieve this command:
# 1. Use "set_menu" feature to set the menu to "Quinoa" and adjust the cooking time.
# 2. Use "start_cooking" feature to start running the rice cooker.

# Relevant user manual text:
# - "**Menu** Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected. Press start if cooking time is okay. Use + and - if you want to adjust time."
# - "**Start** Press to start cooking."

# Relevant feature_list names in the given code:
# - "set_menu"
# - "start_cooking"

# Goal variable values:
# - Set variable_menu_index to "Quinoa"
# - Set variable_menu_setting to 20 minutes
# - Set variable_start_running to "on"

class ExtendedSimulator(Simulator): 
    pass