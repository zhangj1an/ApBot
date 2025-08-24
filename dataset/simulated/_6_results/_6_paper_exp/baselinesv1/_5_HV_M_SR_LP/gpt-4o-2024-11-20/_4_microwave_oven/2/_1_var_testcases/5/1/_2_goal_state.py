feature_sequence = ["set_function_dial", "set_upper_element_temperature", "set_lower_element_temperature", "set_timer"]
feature_choice_reason = "Feature 'set_function_dial' is used to set the function to Rotisserie. Feature 'set_upper_element_temperature' is used to set the upper element temperature to 450°F. Feature 'set_lower_element_temperature' is used to set the lower element temperature to 450°F. Feature 'set_timer' is used to set the timer to 60 minutes."
changing_variables = ["variable_function_dial", "variable_upper_element_temperature", "variable_lower_element_temperature", "variable_timer"]
goal_state = ExtendedSimulator()
# "set_function_dial", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Rotisserie")
# "set_upper_element_temperature", step 1, variable_upper_element_temperature
goal_state.variable_upper_element_temperature.set_current_value("450")
# "set_lower_element_temperature", step 1, variable_lower_element_temperature
goal_state.variable_lower_element_temperature.set_current_value("450")
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(60) # The number represents minutes.