feature_sequence = ["power", "timer"]
feature_choice_reason = "Feature 'power' is required to turn on the dehumidifier. Feature 'timer' is required to configure the timer to shut down after 3 hours."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = Simulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(3) # The number represents hours.