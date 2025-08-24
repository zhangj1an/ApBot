# The relevant user manual text describes:
# 1. "Press Menu to select the desired function" - used for selecting the menu. 
# 2. "Use + and - if you want to adjust time" - used for adjusting the cooking time.
# 3. "Press to start cooking" - used for starting the cooking process.

# The relevant feature_list names in the provided code are:
# - "set_menu" for selecting the menu (step 1 sets "variable_menu_index", step 2 adjusts "variable_menu_setting").
# - "start_cooking" for starting the cooking process (step 1 sets "variable_start_running").

# To achieve the command:
#   1. Use the "set_menu" feature to set `variable_menu_index` to "Quinoa".
#   2. Use the "set_menu" feature to adjust `variable_menu_setting` to "35" for cooking time.
#   3. Use the "start_cooking" feature to set `variable_start_running` to "on".

# Goal variable values are:
# - `variable_menu_index` = "Quinoa"
# - `variable_menu_setting` = "35"
# - `variable_start_running` = "on".

class ExtendedSimulator(Simulator): 
	pass