feature_sequence = ["menu_selection", "loaf_size_selection", "crust_color_selection", "delay_timer_setting", "start_stop_operation"]
feature_choice_reason = "Feature 'menu_selection' is required to select the Quick program. Feature 'loaf_size_selection' is needed to choose the loaf size of 700g. Feature 'crust_color_selection' is necessary to set the crust color to Light. Feature 'delay_timer_setting' is required to set the delay timer for 11 hours. Finally, 'start_stop_operation' is needed to power on and start the bread maker operation."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_delay_timer", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("4 Quick")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("700g")
# "crust_color_selection", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Light")
# "delay_timer_setting", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(11) # The number represents hours.
# "start_stop_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")