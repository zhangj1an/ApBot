feature_sequence = ["menu_selection", "crust_color_selection", "loaf_size_selection", "delay_time_setting", "start_stop_operation"]
feature_choice_reason = "Feature 'menu_selection' is needed to set the bread type to French. Feature 'crust_color_selection' is required to set the crust color to dark. Feature 'loaf_size_selection' is necessary to set the loaf size to 2.0LB. Feature 'delay_time_setting' is required to set the delay timer to 6 hours. Finally, 'start_stop_operation' is needed to start the bread maker."
changing_variables = ["variable_menu_index", "variable_crust_color", "variable_loaf_size", "variable_delay_time", "variable_start_running"]

goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("FRENCH")
# "crust_color_selection", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("DARK")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("2.0LB")
# "delay_time_setting", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(6)  # The number represents hours.
# "start_stop_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")