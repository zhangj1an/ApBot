feature_sequence = ["power_on_off", "set_timer"]
feature_choice_reason = "The 'power_on_off' feature is required to turn on the appliance. The 'set_timer' feature is needed to set the timer to '8H'."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("8H")