feature_sequence = ["set_menu", "adjust_loaf_size", "adjust_crust_color", "adjust_timer", "start_stop"]
feature_choice_reason = "Feature 'set_menu' is required to select the '1 Basic white' menu. Feature 'adjust_loaf_size' is needed to set the loaf size to '2lb'. Feature 'adjust_crust_color' is necessary to set the crust color to 'medium'. Feature 'adjust_timer' is required to set the timer delay to 5 hours. Finally, feature 'start_stop' is needed to start the breadmaker."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_timer_delay", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("1 Basic white")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("2lb")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("medium")
# "adjust_timer", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value(300) # The number represents minutes.
# "start_stop", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")