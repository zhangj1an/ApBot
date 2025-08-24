feature_sequence = ["set_menu", "set_delay_time", "start_cooking"]
feature_choice_reason = "Feature 'set_menu' is required to set the menu to 'steam'. Feature 'set_delay_time' is required to set the delay time to 5 hours. Feature 'start_cooking' is required to start the machine."
changing_variables = ["variable_menu_index", "variable_delay_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("steam")
# "set_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(5) # each number represents an hour.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")