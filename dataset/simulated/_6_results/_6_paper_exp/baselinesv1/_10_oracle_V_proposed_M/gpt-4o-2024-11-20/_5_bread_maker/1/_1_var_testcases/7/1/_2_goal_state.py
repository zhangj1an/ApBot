feature_sequence = ["set_menu", "set_crust_color", "set_loaf_size", "adjust_delay_time", "start_or_stop_bread_maker"]
feature_choice_reason = "Feature 'set_menu' is required to set the menu to 'Cake'. Feature 'set_crust_color' is required to set the crust color to 'Dark'. Feature 'set_loaf_size' is required to set the loaf size to '2.0LB'. Feature 'adjust_delay_time' is required to set the timer to 4 hours (240 minutes). Feature 'start_or_stop_bread_maker' is required to start the bread maker."
changing_variables = ["variable_menu_index", "variable_crust_color", "variable_loaf_size", "variable_delay_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Cake")
# "set_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Dark")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("2.0LB")
# "adjust_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(240) # The number represents minutes.
# "start_or_stop_bread_maker", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")