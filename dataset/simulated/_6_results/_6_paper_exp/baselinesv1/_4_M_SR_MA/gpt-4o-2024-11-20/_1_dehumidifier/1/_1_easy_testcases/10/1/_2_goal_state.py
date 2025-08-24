feature_sequence = ["power_on_off", "adjust_timer"]
feature_choice_reason = "The 'power_on_off' feature is required to turn on the dehumidifier. The 'adjust_timer' feature is needed to configure the timer to shut down after 3 hours."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(3) # each number represents an hour.