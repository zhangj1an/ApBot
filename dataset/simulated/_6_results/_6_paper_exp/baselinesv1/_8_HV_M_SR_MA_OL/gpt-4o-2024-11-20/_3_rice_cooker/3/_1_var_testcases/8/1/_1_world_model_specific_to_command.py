# The current code accurately models the relevant appliance features needed to achieve the user command: 
# "Set the rice cooker to Quinoa, and increase the cooking time to 35 minutes, and start running."

# Sequence of features needed to achieve this command:
# 1. "set_menu": Adjust `variable_menu_index` to "Quinoa" (pressing the "menu" button).
# 2. "set_menu": Increase `variable_menu_setting` to 35 minutes using "press_plus_button".
# 3. "start_cooking": Start the rice cooker by setting `variable_start_running` to "on" (pressing the "start" button).

# Relevant user manual text:
# "Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected."
# "Press Start to start cooking."
# "Use + and - to adjust cooking time."

# Feature_list names in the given code:
# 1. "set_menu" 
# 2. "start_cooking"

# Goal variable values to achieve this command:
# - Set `variable_menu_index` to "Quinoa".
# - Set `variable_menu_setting` (for Quinoa) to 35.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
	pass