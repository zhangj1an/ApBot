feature_sequence = ["select_cycle", "adjust_crust_color", "adjust_loaf_size", "adjust_delay_timer", "start_or_stop_operation"]
feature_choice_reason = "Feature 'select_cycle' is needed to set variable_cycle to 'Basic'. Feature 'adjust_crust_color' is needed to set variable_crust_color to 'Light'. Feature 'adjust_loaf_size' is needed to set variable_loaf_size to '2.0lb'. Feature 'adjust_delay_timer' is needed to set variable_delay_timer to 120 minutes. Feature 'start_or_stop_operation' is needed to set variable_start_running to 'on'."
changing_variables = ["variable_cycle", "variable_crust_color", "variable_loaf_size", "variable_delay_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cycle", step 1, variable_cycle
goal_state.variable_cycle.set_current_value("Basic")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Light")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("2.0lb")
# "adjust_delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(120) # The number represents minutes.
# "start_or_stop_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")