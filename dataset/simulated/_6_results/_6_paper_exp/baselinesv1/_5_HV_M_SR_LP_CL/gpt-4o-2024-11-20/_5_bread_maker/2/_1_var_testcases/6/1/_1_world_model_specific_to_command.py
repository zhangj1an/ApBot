# The given code accurately models the appliance's features as described in the user manual
# The sequence of features needed to achieve the user’s command is as follows:
# 1. Use Feature `set_menu_and_setting` to select the fastbake 2 menu.
#      - Press `press_menu_button` until variable_menu_index is set to "7" (Fastbake II).
# 2. Use Feature `adjust_crust_color` to set crust color to "medium".
#      - Press `press_crust_button` until variable_crust_color is set to "medium".
# 3. Use Feature `adjust_loaf_size` to set loaf size to "2LB".
#      - Press `press_loaf_size_button` until variable_loaf_size is set to "2LB".
# 4. Use Feature `adjust_timer_delay` to set the timer delay to "1:00:00".
#      - Adjust using `press_time_up_button` or `press_time_down_button`.
# 5. Use Feature `start_stop_operation` to start the bread maker.
#      - Press `press_start_stop_button` to set variable_start_running to "on".

# Relevant user manual excerpts supporting the features:
# - "Menu button: For choosing the bread making program from the list 1 to 12."
# - "Color button: For selecting crust color from light, medium or dark."
# - "Loaf size button: For selecting small (1.5lb) or large (2lb) loaf size."
# - "Timer delay buttons: Use to delay the start of bread making (all programs except Fastbake)."
# - "Start: Press to start for approx 1 second, a beep sounds and the colon (:) flashes and the program starts."

# Feature names in the provided code:
# - Feature: `set_menu_and_setting` (select menu and program setting)
# - Feature: `adjust_crust_color` (adjust crust color)
# - Feature: `adjust_loaf_size` (adjust loaf size)
# - Feature: `adjust_timer_delay` (adjust timer delay)
# - Feature: `start_stop_operation` (start bread maker)

# The final goal variable values to achieve this user command:
goal_variable_values = {
    "variable_menu_index": "7",
    "variable_menu_setting": "0:58:00",  # Time in Fastbake II menu.
    "variable_crust_color": "medium",
    "variable_loaf_size": "2LB",
    "variable_timer_delay": "1:00:00",
    "variable_start_running": "on"
}

class ExtendedSimulator(Simulator):
    pass