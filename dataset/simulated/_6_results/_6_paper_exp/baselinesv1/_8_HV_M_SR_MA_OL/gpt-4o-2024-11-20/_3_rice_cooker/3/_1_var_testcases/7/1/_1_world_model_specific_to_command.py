# Python comment: The current code accurately models the relevant appliance features to achieve the user command.
# Sequence of features needed: "set_menu", "start_cooking"
# User manual text describing relevant features:
# 1. **Menu**: "Press menu button to scroll through preset functions, White Rice, Brown Rice, Quinoa, Steel Cut Oats. Indicator light shows which function is selected. Press start if cooking time is okay. Use + and - if you want to adjust time."
# 2. **Start**: "Press to start cooking."
# Feature list names in the given code: "set_menu", "start_cooking"
# Goal variable values to achieve this command: 
# - Set `variable_menu_index` to "Quinoa"
# - Set `variable_menu_setting` to 20
# - Set `variable_start_running` to "on"

class ExtendedSimulator(Simulator): 
	pass