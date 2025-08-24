feature_sequence = ["set_menu", "adjust_loaf_size", "adjust_crust_color", "adjust_timer", "start_stop"]
feature_choice_reason = "Feature 'set_menu' is used to select the 'Fastbake II' menu. Feature 'adjust_loaf_size' is required to set the loaf size to '2lb'. Feature 'adjust_crust_color' is needed to set the crust color to 'medium'. Feature 'adjust_timer' is used to set the timer delay to 1 hour. Finally, feature 'start_stop' is used to start the bread maker."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_timer_delay", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("7 Fastbake II")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("2lb")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("medium")
# "adjust_timer", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value(60) # The number represents minutes.
# "start_stop", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")