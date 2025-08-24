feature_sequence = ["power_on_off", "set_sterilize_dry_mode", "start_appliance"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'set_sterilize_dry_mode' is needed to select the 'Sterilize & Dry' mode. Finally, feature 'start_appliance' is required to start the appliance."
changing_variables = ["variable_power_on_off", "variable_sterilize_dry_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_sterilize_dry_mode", step 1, variable_sterilize_dry_mode
goal_state.variable_sterilize_dry_mode.set_current_value("Sterilize & Dry")
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")