# The requested user command requires the following sequence of features:
# 1. "set_menu" to select the Sweet program.
# 2. "set_loaf_size" to choose a loaf size of 700g.
# 3. "set_crust_color" to select the crust color to Medium.
# 4. "set_delay_timer" to set the delay timer to 4 hours.
# 5. "start_stop_program" to start the bread maker operation.

# Relevant raw user manual text:
# - "Choose a Programme with the MENU button."
# - "Press LOAF SIZE button to select the Loaf Size (as needed)."
# - "Press COLOR button to select the Crust Colour (as needed)."
# - "Use these [Delay Timer] buttons when you would like to delay the completion of your bread. To set the Timer, determine when you would like your bread to be ready, then set the Timer"
# - "Press START/STOP button to start or stop the Programmes."

# The feature_list has correctly modeled these functionalities:
# - Feature "set_menu" adjusts the `variable_menu_index` via "press_menu_button".
# - Feature "set_loaf_size" adjusts the `variable_loaf_size` via "press_loaf_size_button".
# - Feature "set_crust_color" adjusts the `variable_crust_color` via "press_color_button".
# - Feature "set_delay_timer" adjusts the `variable_delay_timer` via "press_time_plus_button" and "press_time_minus_button".
# - Feature "start_stop_program" toggles the `variable_start_running` between "on" and "off".

# Goal variable values for the requested user command:
# - Set `variable_menu_index` to "5" (Sweet program).
# - Set `variable_loaf_size` to "700g".
# - Set `variable_crust_color` to "Medium".
# - Set `variable_delay_timer` to 240 minutes (4 hours).
# - Set `variable_start_running` to "on" (start the bread maker operation).

class ExtendedSimulator(Simulator): 
    pass