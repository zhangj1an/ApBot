feature_sequence = ["set_menu_and_setting", "adjust_loaf_size", "adjust_crust_color", "adjust_timer_delay", "start_stop_operation"]
feature_choice_reason = "Feature 'set_menu_and_setting' is used to select the wholewheat menu. Feature 'adjust_loaf_size' is required to set the loaf size to small (1.5LB). Feature 'adjust_crust_color' is needed to set the crust color to dark. Feature 'adjust_timer_delay' is necessary to set the timer delay to 2 hours. Finally, feature 'start_stop_operation' is used to start the bread maker."
changing_variables = ["variable_menu_index", "variable_menu_setting", "variable_loaf_size", "variable_crust_color", "variable_timer_delay", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu_and_setting", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("3")
# "set_menu_and_setting", step 1, variable_menu_setting
goal_state.variable_menu_setting = goal_state.menu_setting_dict["3"]
goal_state.variable_menu_setting.set_current_value("3:40:00")  # The number represents hours, minutes, and seconds.
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("1.5LB")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("dark")
# "adjust_timer_delay", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value("02:00:00")  # The number represents hours, minutes, and seconds.
# "start_stop_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")