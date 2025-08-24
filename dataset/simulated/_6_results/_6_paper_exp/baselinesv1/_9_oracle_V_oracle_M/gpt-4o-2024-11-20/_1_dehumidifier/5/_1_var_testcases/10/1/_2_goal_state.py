feature_sequence = ["turn_on_off", "set_timer"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'set_timer' is required to set the timer for 1 hour."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("1H")