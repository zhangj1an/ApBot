feature_sequence = ["set_menu", "set_crust_color", "set_loaf_size", "adjust_delay_time", "start_or_stop_bread_maker"]
feature_choice_reason = "Feature 'set_menu' is required to select the 'Basic' menu. Feature 'set_crust_color' is needed to set the crust color to 'Medium'. Feature 'set_loaf_size' is necessary to set the loaf size to '1.5LB'. Feature 'adjust_delay_time' is required to set the delay timer to 10 hours. Finally, feature 'start_or_stop_bread_maker' is needed to start the bread maker."
changing_variables = ["variable_menu_index", "variable_crust_color", "variable_loaf_size", "variable_delay_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Basic")
# "set_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Medium")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("1.5LB")
# "adjust_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(600) # 600 minutes (10 hours)
# "start_or_stop_bread_maker", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")