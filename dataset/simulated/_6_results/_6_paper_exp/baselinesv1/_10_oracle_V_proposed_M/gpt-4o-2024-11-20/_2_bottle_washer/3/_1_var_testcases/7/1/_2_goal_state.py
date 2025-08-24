feature_sequence = ["power_on_off", "set_wash_mode", "start_appliance"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'set_wash_mode' is needed to set the wash mode to 'Wash & Dry'. Feature 'start_appliance' is necessary to start the cycle after setting the configurations."
changing_variables = ["variable_power_on_off", "variable_wash_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_wash_mode", step 1, variable_wash_mode
goal_state.variable_wash_mode.set_current_value("Wash & Dry")
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")