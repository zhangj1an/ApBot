feature_sequence = ["power_control", "adjust_timer"]
feature_choice_reason = "Feature power_control is chosen to turn on the dehumidifier. Feature adjust_timer is chosen to set the timer to run for 2 hours."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("2H")