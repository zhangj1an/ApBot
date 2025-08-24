feature_sequence = ["adjust_upper_heater_temperature", "adjust_lower_heater_temperature", "adjust_timer", "select_function"]
feature_choice_reason = "Feature 'adjust_upper_heater_temperature' is included to set the upper heater temperature to 230°C. Feature 'adjust_lower_heater_temperature' is included to set the lower heater temperature to 230°C. Feature 'adjust_timer' is included to set the timer to 40 minutes. Feature 'select_function' is included to set the function knob to 'Lower & Upper Heater'."
changing_variables = ["variable_upper_heater_temperature", "variable_lower_heater_temperature", "variable_timer", "variable_function_knob"]
goal_state = ExtendedSimulator()
# "adjust_upper_heater_temperature", step 1, variable_upper_heater_temperature
goal_state.variable_upper_heater_temperature.set_current_value(230)
# "adjust_lower_heater_temperature", step 1, variable_lower_heater_temperature
goal_state.variable_lower_heater_temperature.set_current_value(230)
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("40")
# "select_function", step 1, variable_function_knob
goal_state.variable_function_knob.set_current_value("Lower & Upper Heater")