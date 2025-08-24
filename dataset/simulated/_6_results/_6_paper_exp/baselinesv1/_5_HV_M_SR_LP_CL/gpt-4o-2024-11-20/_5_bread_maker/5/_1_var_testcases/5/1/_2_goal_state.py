feature_sequence = ["set_menu", "set_loaf_size", "set_crust_color", "set_delay_timer", "start_stop_program"]
feature_choice_reason = "Feature 'set_menu' is included to select the Ultra Fast-1 program. Feature 'set_loaf_size' is included to set the loaf size to 700g. Feature 'set_crust_color' is included to set the crust color to Medium. Feature 'set_delay_timer' is included to set the delay timer to 2 hours. Feature 'start_stop_program' is included to power on and start the bread maker operation."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_delay_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("6")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("700g")
# "set_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Medium")
# "set_delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(120) # The number represents minutes.
# "start_stop_program", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")