feature_sequence = ["adjust_menu", "adjust_crust_color", "adjust_loaf_size", "adjust_delay_time", "start_stop_bread_maker"]
feature_choice_reason = "Each feature is necessary to set the desired menu, crust color, loaf size, delay time, and to start the bread maker. No redundant features are included."
changing_variables = ["variable_menu_index", "variable_crust_color", "variable_loaf_size", "variable_delay_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "adjust_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("French")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Light")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("1.5LB")
# "adjust_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(660) # 660 minutes (11 hours)
# "start_stop_bread_maker", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")