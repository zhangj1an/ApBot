feature_sequence = ["turn_on_off", "select_sterilize_dry_mode", "start_pause"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the appliance. Feature 'select_sterilize_dry_mode' is needed to set the mode to 'Sterilize & Dry'. Feature 'start_pause' is required to start the cycle."
changing_variables = ["variable_power_on_off", "variable_sterilize_dry_mode", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_sterilize_dry_mode", step 1, variable_sterilize_dry_mode
goal_state.variable_sterilize_dry_mode.set_current_value("Sterilize & Dry")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")