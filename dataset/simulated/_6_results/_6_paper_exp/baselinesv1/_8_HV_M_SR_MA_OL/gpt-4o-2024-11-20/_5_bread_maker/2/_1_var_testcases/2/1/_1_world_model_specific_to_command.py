# The sequence of features needed to achieve the user's command:
# 1. "set_menu_and_setting" to set the appliance to the "wholewheat" menu.
# 2. "adjust_loaf_size" to set a small loaf (1.5LB).
# 3. "adjust_crust_color" to set the crust color to "dark".
# 4. "adjust_timer_delay" to set the timer delay to 2 hours.
# 5. "start_stop_operation" to start the bread maker.

# Relevant user manual text:
# - “Use the menu button for choosing the bread-making program from the list 1 to 12.”
# - “For selecting small (1.5lb) or large (2lb) loaf size (certain programs only).”
# - “For selecting crust color from light, medium, or dark (certain programs only).”
# - "Use to delay the start of bread making (all programs except Fastbake)."
# - "Press to start for approx 1 second, a beep sounds and the colon (:) flashes, and the program starts."

# Corresponding feature_list names in the given code:
# - "set_menu_and_setting"
# - "adjust_loaf_size"
# - "adjust_crust_color"
# - "adjust_timer_delay"
# - "start_stop_operation"

# Goal variable values:
# - Set variable_menu_index to "3" (corresponding to the "wholewheat" menu).
# - Set variable_loaf_size to "1.5LB".
# - Set variable_crust_color to "dark".
# - Set variable_timer_delay to "02:00:00".
# - Set variable_start_running to "on".

# The following code doesn't require modifications from the given Simulator because all relevant features and actions are correctly implemented based on the user manual:

class ExtendedSimulator(Simulator):
    pass