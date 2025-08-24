feature_sequence = ["set_menu", "set_loaf_size", "set_crust_color", "set_delay_timer", "start_stop_program"]
feature_choice_reason = "Feature 'set_menu' is used to select the Whole Wheat program. Feature 'set_loaf_size' is used to set the loaf size to 900g. Feature 'set_crust_color' is used to set the crust color to Dark. Feature 'set_delay_timer' is used to set the delay timer to 6 hours. Feature 'start_stop_program' is used to power on and start the bread maker operation."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_delay_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("3")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "set_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Dark")
# "set_delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(360) # The number represents minutes.
# "start_stop_program", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")