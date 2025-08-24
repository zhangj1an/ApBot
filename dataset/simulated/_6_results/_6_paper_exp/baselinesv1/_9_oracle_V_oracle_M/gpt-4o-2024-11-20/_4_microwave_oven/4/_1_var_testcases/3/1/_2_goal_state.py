feature_sequence = ["set_upper_heater_temperature", "set_lower_heater_temperature", "set_timer", "set_function"]
feature_choice_reason = "Feature 'set_upper_heater_temperature' is required to set the upper heater temperature. Feature 'set_lower_heater_temperature' is required to set the lower heater temperature. Feature 'set_timer' is required to set the timer. Feature 'set_function' is required to set the function to convection."
changing_variables = ["variable_upper_heater_temperature", "variable_lower_heater_temperature", "variable_timer", "variable_function"]
goal_state = Simulator()
# "set_upper_heater_temperature", step 1, variable_upper_heater_temperature
goal_state.variable_upper_heater_temperature.set_current_value(190)
# "set_lower_heater_temperature", step 1, variable_lower_heater_temperature
goal_state.variable_lower_heater_temperature.set_current_value(190)
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("40")
# "set_function", step 1, variable_function
goal_state.variable_function.set_current_value("Convection")