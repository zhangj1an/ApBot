feature_sequence = ["set_menu", "set_delay_time", "start_cooking"]
feature_choice_reason = "Feature 'set_menu' is required to select the 'PORRIDGE' menu. Feature 'set_delay_time' is required to set the reservation time to 1 hour. Feature 'start_cooking' is required to start the machine after setting the configurations."
changing_variables = ["variable_menu_index", "variable_delay_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("porridge")
# "set_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(1) # each number represents an hour.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")