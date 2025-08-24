feature_sequence = ["power_control", "choose_sterilize_dry_mode", "start_cycle"]
feature_choice_reason = "Feature 'power_control' is required to turn on the appliance. Feature 'choose_sterilize_dry_mode' is needed to set the cycle to 'Sterilize & Dry'. Feature 'start_cycle' is required to start the selected cycle."
changing_variables = ["variable_power_on_off", "variable_sterilize_dry_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "choose_sterilize_dry_mode", step 1, variable_sterilize_dry_mode
goal_state.variable_sterilize_dry_mode.set_current_value("Sterilize & Dry")
# "start_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")