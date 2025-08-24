feature_sequence = ["temp", "function", "selector", "timer"]
feature_choice_reason = "Feature 'temp' is chosen to set the temperature. Feature 'function' is chosen to set the function dial. Feature 'selector' is chosen to set the selector dial. Feature 'timer' is chosen to set the timer."
changing_variables = ["variable_temperature_dial", "variable_function_dial", "variable_selector_dial", "variable_timer_dial"]
goal_state = Simulator()
# "temp", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("150°C")
# "function", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "selector", step 1, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Top & Bottom Heating")
# "timer", step 1, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("20")