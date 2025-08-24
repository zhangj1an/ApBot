feature_sequence = ["power_on_off", "timer"]
feature_choice_reason = "The appliance must be turned on first, so 'power_on_off' is included. Then, the timer needs to be set to '8H', which is achieved using the 'timer' feature."
changing_variables = ["variable_power_on_off", "variable_timer"]
goal_state = Simulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("8H")