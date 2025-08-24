feature_sequence = ["set_delay_timer", "set_menu", "start_cooking"]
feature_choice_reason = "Feature 'set_delay_timer' is required to adjust the delay timer to 10 hours. Feature 'set_menu' is required to set the rice cooker to 'White Rice'. Feature 'start_cooking' is required to start the appliance."
changing_variables = ["variable_delay_timer", "variable_menu_index", "variable_menu_setting", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_delay_timer", step 2, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(10) # each number represents an hour.
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("White Rice")
# "set_menu", step 2, variable_menu_setting
goal_state.variable_menu_setting = goal_state.menu_setting_dict["White Rice"]
goal_state.variable_menu_setting.set_current_value(40) # each number represents minutes.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")