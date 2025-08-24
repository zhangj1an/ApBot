feature_sequence = ["set_menu", "set_reservation_time", "start_cooking"]
feature_choice_reason = "Feature 'set_menu' is used to select the 'PORRIDGE' menu. Feature 'set_reservation_time' is used to set the reservation time to 1 hour. Feature 'start_cooking' is used to start the machine."
changing_variables = ["variable_menu_index", "variable_reservation_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("PORRIDGE")
# "set_reservation_time", step 1, variable_reservation_time
goal_state.variable_reservation_time.set_current_value(1) # each number represents an hour.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")