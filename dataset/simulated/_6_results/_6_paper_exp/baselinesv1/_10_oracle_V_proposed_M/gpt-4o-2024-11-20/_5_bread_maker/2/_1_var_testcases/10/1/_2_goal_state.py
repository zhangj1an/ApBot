feature_sequence = ["adjust_loaf_size", "adjust_crust_color", "set_menu", "adjust_timer", "start_stop"]
feature_choice_reason = "Feature 'adjust_loaf_size' is required to set the bread size to large. Feature 'adjust_crust_color' is required to set the crust color to medium. Feature 'set_menu' is required to set the menu to Fastbake I. Feature 'adjust_timer' is required to set the timer delay to 2 hours. Feature 'start_stop' is required to start the bread maker."
changing_variables = ["variable_loaf_size", "variable_crust_color", "variable_menu_index", "variable_timer_delay", "variable_start_running"]
goal_state = ExtendedSimulator()
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("2lb")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("medium")
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("6 Fastbake I")
# "adjust_timer", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value(120)  # The number represents minutes.
# "start_stop", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")