feature_sequence = ["set_program_menu", "adjust_loaf_size", "adjust_crust_color", "adjust_delay_timer", "start_stop_appliance"]
feature_choice_reason = "Feature 'set_program_menu' is required to select the Basic program. Feature 'adjust_loaf_size' is needed to set the loaf size to 900g. Feature 'adjust_crust_color' is necessary to set the crust color to Medium. Feature 'adjust_delay_timer' is required to set the delay timer to 5 hours. Finally, 'start_stop_appliance' is needed to power on and start the bread maker operation."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_delay_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_program_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("1")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Medium")
# "adjust_delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(300) # The number represents minutes.
# "start_stop_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")