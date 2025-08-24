feature_sequence = ["temp", "function", "selector", "timer"]
feature_choice_reason = "Feature 'temp' is chosen to set the temperature to 200°C. Feature 'function' is chosen to set the function dial to 'Convection'. Feature 'selector' is chosen to set the selector dial to 'Top Heating'. Feature 'timer' is chosen to set the timer to '30'."
changing_variables = ["variable_temperature_dial", "variable_function_dial", "variable_selector_dial", "variable_timer_dial"]
goal_state = Simulator()
# "temp", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("200°C")
# "function", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "selector", step 1, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Top Heating")
# "timer", step 1, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("30")