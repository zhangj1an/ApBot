feature_sequence = ["set_upper_element_temperature", "set_lower_element_temperature", "set_function_dial", "set_timer"]
feature_choice_reason = "Feature 'set_upper_element_temperature' is required to set the upper element temperature to 350°F. Feature 'set_lower_element_temperature' is required to set the lower element temperature to 450°F. Feature 'set_function_dial' is required to set the function to Convection. Feature 'set_timer' is required to set the timer to 30 minutes."
changing_variables = ["variable_upper_element_temperature", "variable_lower_element_temperature", "variable_function_dial", "variable_timer"]
goal_state = ExtendedSimulator()
# "set_upper_element_temperature", step 1, variable_upper_element_temperature
goal_state.variable_upper_element_temperature.set_current_value("350")
# "set_lower_element_temperature", step 1, variable_lower_element_temperature
goal_state.variable_lower_element_temperature.set_current_value("450")
# "set_function_dial", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_value_ranges_steps([[0, 60, 10]], 30) # The number represents minutes.
goal_state.variable_timer.set_current_value(30) # The number represents minutes.