feature_sequence = ["adjust_delay_timer", "set_menu", "start_cooking"]
feature_choice_reason = "Feature 'adjust_delay_timer' is required to set the delay time to 2 hours. Feature 'set_menu' is required to set the rice cooker to Brown Rice. Feature 'start_cooking' is required to start the cooking process."
changing_variables = ["variable_delay_timer", "variable_menu_index", "variable_menu_setting", "variable_start_running"]
goal_state = ExtendedSimulator()
# "adjust_delay_timer", step 2, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(2) # each number represents an hour.
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Brown Rice")
# "set_menu", step 2, variable_menu_setting
goal_state.variable_menu_setting = goal_state.menu_setting_dict["Brown Rice"]
goal_state.variable_menu_setting.set_current_value(0) # Default value for menu-specific setting.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")