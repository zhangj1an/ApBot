feature_sequence = ["set_menu", "adjust_crust_color", "adjust_loaf_size", "adjust_timer", "start_stop"]
feature_choice_reason = "Feature 'set_menu' is required to set the dough program. Feature 'adjust_crust_color' is needed to set the crust color to light. Feature 'adjust_loaf_size' is necessary to set the loaf size to large. Feature 'adjust_timer' is required to set the timer delay to 3 hours. Finally, feature 'start_stop' is needed to start the bread maker."
changing_variables = ["variable_menu_index", "variable_crust_color", "variable_loaf_size", "variable_timer_delay", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("8 Dough")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("light")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("2lb")
# "adjust_timer", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value(180) # The number represents minutes.
# "start_stop", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")