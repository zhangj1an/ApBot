feature_sequence = ["power_on_off", "timer"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'timer' is required to set the timer to '2H'."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = Simulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("2H")