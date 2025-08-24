feature_sequence = ["power_on_off", "set_wash_mode", "start_appliance"]
feature_choice_reason = "The 'power_on_off' feature is required to turn on the appliance. The 'set_wash_mode' feature is needed to select the 'Wash, Sterilize, Dry' mode. Finally, the 'start_appliance' feature is necessary to begin the washing procedure."
changing_variables = ["variable_power_on_off", "variable_wash_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_wash_mode", step 1, variable_wash_mode
goal_state.variable_wash_mode.set_current_value("Wash, Sterilize, Dry")
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")