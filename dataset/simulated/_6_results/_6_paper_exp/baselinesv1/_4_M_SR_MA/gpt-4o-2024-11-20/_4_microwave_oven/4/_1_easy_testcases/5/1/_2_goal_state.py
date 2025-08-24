feature_sequence = ["adjust_upper_heater_temperature", "adjust_lower_heater_temperature", "set_timer", "set_function_knob"]
feature_choice_reason = "Feature 'adjust_upper_heater_temperature' is needed to set the upper heater temperature. Feature 'adjust_lower_heater_temperature' is needed to set the lower heater temperature. Feature 'set_timer' is required to set the timer. Feature 'set_function_knob' is necessary to set the function to the upper heater."
changing_variables = ["variable_upper_heater_temperature", "variable_lower_heater_temperature", "variable_timer", "variable_function_knob"]
goal_state = ExtendedSimulator()
# "adjust_upper_heater_temperature", step 1, variable_upper_heater_temperature
goal_state.variable_upper_heater_temperature.set_current_value(150) # The number represents degrees Celsius.
# "adjust_lower_heater_temperature", step 1, variable_lower_heater_temperature
goal_state.variable_lower_heater_temperature.set_current_value(150) # The number represents degrees Celsius.
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("60") # The number represents minutes.
# "set_function_knob", step 1, variable_function_knob
goal_state.variable_function_knob.set_current_value("Upper Heater")