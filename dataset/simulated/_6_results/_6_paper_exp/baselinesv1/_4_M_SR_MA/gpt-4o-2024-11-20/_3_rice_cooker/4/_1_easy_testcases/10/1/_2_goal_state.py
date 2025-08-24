feature_sequence = ["set_menu", "set_delay_time", "start_cooking"]
feature_choice_reason = "Feature 'set_menu' is used to set the variable_menu_index to 'brown'. Feature 'set_delay_time' is used to set the variable_delay_time to 7 hours. Feature 'start_cooking' is used to set the variable_start_running to 'on'. Each feature is necessary and sufficient to achieve the goal without redundancy."
changing_variables = ["variable_menu_index", "variable_delay_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("brown")
# "set_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(7) # each number represents an hour.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")