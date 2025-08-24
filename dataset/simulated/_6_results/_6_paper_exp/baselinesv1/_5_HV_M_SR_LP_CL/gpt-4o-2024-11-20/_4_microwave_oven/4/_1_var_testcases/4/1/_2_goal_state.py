feature_sequence = ["set_function_knob", "adjust_upper_heater_temperature", "adjust_lower_heater_temperature", "set_timer"]
feature_choice_reason = "Feature 'set_function_knob' is required to set the function knob to 'Upper Heater'. Feature 'adjust_upper_heater_temperature' is required to set the upper heater temperature to 110 °C. Feature 'adjust_lower_heater_temperature' is required to set the lower heater temperature to 110 °C. Feature 'set_timer' is required to set the timer to 100 minutes."
changing_variables = ["variable_function_knob", "variable_upper_heater_temperature", "variable_lower_heater_temperature", "variable_timer"]
goal_state = ExtendedSimulator()
# "set_function_knob", step 1, variable_function_knob
goal_state.variable_function_knob.set_current_value("Upper Heater")
# "adjust_upper_heater_temperature", step 1, variable_upper_heater_temperature
goal_state.variable_upper_heater_temperature.set_current_value(110) # The number represents degrees Celsius.
# "adjust_lower_heater_temperature", step 1, variable_lower_heater_temperature
goal_state.variable_lower_heater_temperature.set_current_value(110) # The number represents degrees Celsius.
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("100") # The number represents minutes.