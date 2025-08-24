feature_sequence = ["power_on_off", "adjust_timer"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'adjust_timer' is required to set the timer to operate for 8 hours."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(8) # each number represents an hour.