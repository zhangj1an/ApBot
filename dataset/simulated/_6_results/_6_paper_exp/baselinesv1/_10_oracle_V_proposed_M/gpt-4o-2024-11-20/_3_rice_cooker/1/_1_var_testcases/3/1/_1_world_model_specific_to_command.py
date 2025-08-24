# The provided code already implements the features necessary to achieve the user command:
# "Cook bean in the rice cooker, set cooking time to be 1 hour and 20 minutes, then start."
# The required features are:
# 1. Select the menu option "Bean" - This uses the `select_menu_option` feature.
#    User manual reference: "3. Select the Bean or Soup function by pressing the Menu button (fig. 10)."
# 2. Set cooking time - This uses the `set_cooking_time` feature.
#    User manual reference: "6. Press the Cooking time button."
#    "3. Press the Hr. button to set the hour unit (fig. 17)."
#    "5. Press the Min. button to set the minute unit (fig. 17)."
# 3. Start cooking - This uses the `start_cooking` feature.
#    User manual reference: "7. Press the Start button to start cooking (fig. 8)."

# Sequence of features needed to complete the command:
# 1. Select the appropriate menu option for "Bean".
# 2. Set the cooking time to 1 hour and 20 minutes.
# 3. Start cooking.

# The goal variable values needed to achieve the command:
# - Set `variable_menu_index` to "Bean"
# - Set `variable_cooking_time_hours` to 1
# - Set `variable_cooking_time_minutes` to 20
# - Set `variable_start_cooking` to "on"

class ExtendedSimulator(Simulator):
    pass