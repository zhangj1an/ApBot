feature_sequence = ["select_cycle", "select_crust_color", "select_loaf_size", "set_delay_timer", "start_stop_operation"]
feature_choice_reason = "Feature 'select_cycle' is needed to set variable_cycle to 'Cake'. Feature 'select_crust_color' is needed to set variable_crust_color to 'Medium'. Feature 'select_loaf_size' is needed to set variable_loaf_size to '1.5lb'. Feature 'set_delay_timer' is needed to set variable_delay_timer to 180 minutes. Feature 'start_stop_operation' is needed to set variable_start_running to 'on'."
changing_variables = ["variable_cycle", "variable_crust_color", "variable_loaf_size", "variable_delay_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cycle", step 1, variable_cycle
goal_state.variable_cycle.set_current_value("Cake")
# "select_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Medium")
# "select_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("1.5lb")
# "set_delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(180) # The number represents minutes.
# "start_stop_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")