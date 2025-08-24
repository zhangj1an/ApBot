feature_sequence = ["menu_selection", "loaf_size_selection", "crust_color_selection", "delay_timer_setting", "start_stop_operation"]
feature_choice_reason = "Feature menu_selection is used to select the Quick program. Feature loaf_size_selection is used to choose a loaf size of 900g. Feature crust_color_selection is used to set the crust color to Medium. Feature delay_timer_setting is used to set the delay timer to 2 hours. Feature start_stop_operation is used to power on and start the operation."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_delay_timer", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("4 Quick")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "crust_color_selection", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Medium")
# "delay_timer_setting", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(2) # each number represents an hour.
# "start_stop_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")