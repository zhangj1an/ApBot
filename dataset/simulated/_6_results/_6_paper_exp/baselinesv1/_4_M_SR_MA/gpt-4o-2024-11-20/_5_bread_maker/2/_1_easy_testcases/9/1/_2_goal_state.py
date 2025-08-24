feature_sequence = ["set_menu_and_setting", "adjust_crust_color", "adjust_loaf_size", "adjust_timer_delay", "start_stop_operation"]
feature_choice_reason = "Feature 'set_menu_and_setting' is required to set the menu to 'Cake'. Feature 'adjust_crust_color' is needed to set the crust color to 'light'. Feature 'adjust_loaf_size' is necessary to set the loaf size to '1.5LB'. Feature 'adjust_timer_delay' is required to set the timer delay to '3:00:00'. Finally, 'start_stop_operation' is needed to start the bread maker."
changing_variables = ["variable_menu_index", "variable_menu_setting", "variable_crust_color", "variable_loaf_size", "variable_timer_delay", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu_and_setting", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("10")
goal_state.variable_menu_setting = goal_state.menu_setting_dict["10"]
goal_state.variable_menu_setting.set_current_value("2:50:00") # each number represents seconds.
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("light")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("1.5LB")
# "adjust_timer_delay", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value("03:00:00") # each number represents seconds.
# "start_stop_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")