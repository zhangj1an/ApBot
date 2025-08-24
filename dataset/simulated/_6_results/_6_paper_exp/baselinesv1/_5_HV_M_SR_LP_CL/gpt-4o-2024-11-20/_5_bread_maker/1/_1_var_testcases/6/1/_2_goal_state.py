feature_sequence = ["adjust_menu", "adjust_loaf_size", "adjust_delay_time", "start_stop_bread_maker"]
feature_choice_reason = "Feature 'adjust_menu' is needed to set the menu to 'Sandwich'. Feature 'adjust_loaf_size' is required to set the loaf size to '1.5LB'. Feature 'adjust_delay_time' is necessary to set the delay timer to 6 hours. Finally, 'start_stop_bread_maker' is needed to start the bread maker."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_delay_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "adjust_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Sandwich")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("1.5LB")
# "adjust_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(360) # The number represents minutes.
# "start_stop_bread_maker", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")