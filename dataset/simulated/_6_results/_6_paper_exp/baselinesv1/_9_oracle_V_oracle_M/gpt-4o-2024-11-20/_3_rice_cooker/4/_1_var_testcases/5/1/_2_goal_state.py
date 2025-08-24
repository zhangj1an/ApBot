feature_sequence = ["menu_selection", "delay_timer", "start_running"]
feature_choice_reason = "Feature 'menu_selection' is used to set the variable_menu_index to 'MIXED'. Feature 'delay_timer' is used to set the variable_delay_timer to 6 hours. Feature 'start_running' is used to start the machine after all configurations are set."
changing_variables = ["variable_menu_index", "variable_delay_timer", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("MIXED")
# "delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(6) # each number represents an hour.
# "start_running", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")