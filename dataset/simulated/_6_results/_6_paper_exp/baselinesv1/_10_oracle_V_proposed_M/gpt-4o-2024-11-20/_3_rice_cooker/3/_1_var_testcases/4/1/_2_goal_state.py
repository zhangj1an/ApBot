feature_sequence = ["set_delay_timer", "set_menu", "start_cooking"]
feature_choice_reason = "Feature 'set_delay_timer' is required to set the delay timer to 1.5 hours. Feature 'set_menu' is required to select 'Steel Cut Oats' and configure its settings. Feature 'start_cooking' is required to start the appliance."
changing_variables = ["variable_delay_timer", "variable_menu_index", "variable_menu_setting", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_delay_timer", step 2, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(1.5) # each number represents an hour.
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Steel Cut Oats")
# "set_menu", step 2, variable_menu_setting
goal_state.variable_menu_setting = goal_state.menu_setting_dict["Steel Cut Oats"]
goal_state.variable_menu_setting.set_current_value(25) # each number represents minutes.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")