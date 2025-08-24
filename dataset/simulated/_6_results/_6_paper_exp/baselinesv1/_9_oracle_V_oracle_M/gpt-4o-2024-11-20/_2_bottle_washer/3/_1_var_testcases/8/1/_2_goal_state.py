feature_sequence = ["turn_on_off", "select_wash_mode", "start_pause"]
feature_choice_reason = "The machine must be turned on first, so 'turn_on_off' is included. Then, the wash mode needs to be set to 'Wash, Sterilize, Dry', so 'select_wash_mode' is included. Finally, the washing procedure must begin, so 'start_pause' is included."
changing_variables = ["variable_power_on_off", "variable_wash_mode", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_wash_mode", step 1, variable_wash_mode
goal_state.variable_wash_mode.set_current_value("Wash, Sterilize, Dry")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")