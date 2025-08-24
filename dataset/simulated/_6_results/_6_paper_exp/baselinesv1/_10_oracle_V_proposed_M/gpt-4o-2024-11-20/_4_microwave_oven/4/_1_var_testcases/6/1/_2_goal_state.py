feature_sequence = ["select_function", "adjust_upper_heater_temperature", "adjust_lower_heater_temperature", "adjust_timer"]
feature_choice_reason = "Feature 'select_function' is required to set the function knob to 'Lower & Upper Heater'. Feature 'adjust_upper_heater_temperature' is required to set the upper heater temperature to 70 °C. Feature 'adjust_lower_heater_temperature' is required to set the lower heater temperature to 70 °C. Feature 'adjust_timer' is required to set the timer to 80 minutes."
changing_variables = ["variable_function_knob", "variable_upper_heater_temperature", "variable_lower_heater_temperature", "variable_timer"]
goal_state = ExtendedSimulator()
# "select_function", step 1, variable_function_knob
goal_state.variable_function_knob.set_current_value("Lower & Upper Heater")
# "adjust_upper_heater_temperature", step 1, variable_upper_heater_temperature
goal_state.variable_upper_heater_temperature.set_current_value(70) # The number represents °C
# "adjust_lower_heater_temperature", step 1, variable_lower_heater_temperature
goal_state.variable_lower_heater_temperature.set_current_value(70) # The number represents °C
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("80") # The number represents minutes