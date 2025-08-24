# The provided simulator code is already accurately modeling the requested user command based on the user manual.
# The sequence of features needed to achieve the user command is:
# 1. Select the "Bean" menu option. (Feature: "select_menu_option")
# 2. Set the cooking time to 1 hour and 10 minutes. (Feature: "set_cooking_time")
# 3. Start the cooking process. (Feature: "start_cooking")
#
# Relevant user manual text:
# 1. "3. Select the Bean or Soup function by pressing the Menu button (fig. 10)."
# 2. "6. Press the 'Cooking time' button."
#    "Press the Hr. button to set the hour unit (fig. 17)."
#    "Press the Min. button to set the minute unit (fig. 17)."
# 3. "7. Press the 'Start' button to start cooking (fig. 8)."
#
# The relevant features from the given feature_list are:
# - "select_menu_option"
# - "set_cooking_time"
# - "start_cooking"
#
# Corresponding goal variable values to achieve this command:
# - Set `variable_menu_index` to "Bean".
# - Set `variable_cooking_time_hours` to 1.
# - Set `variable_cooking_time_minutes` to 10.
# - Set `variable_start_cooking` to "on".

class ExtendedSimulator(Simulator): 
    pass