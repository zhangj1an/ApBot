feature_sequence = ["power_on_off", "timer"]
feature_choice_reason = "The 'power_on_off' feature is required to turn on the appliance. The 'timer' feature is needed to set the timer to '4H'."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = Simulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("4H")