feature_sequence = ["power_on_off", "timer_adjustment"]
feature_choice_reason = "Feature 'power_on_off' is required to switch on the dehumidifier. Feature 'timer_adjustment' is required to configure the timer to shut down after 3 hours."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "timer_adjustment", step 1, variable_timer
goal_state.variable_timer.set_current_value(3) # each number represents an hour.