feature_sequence = ["adjust_upper", "adjust_function", "adjust_lower", "adjust_timer"]
feature_choice_reason = "Feature 'adjust_upper' is chosen to set the upper element temperature. Feature 'adjust_function' is chosen to set the function to Toast/Broil. Feature 'adjust_lower' is chosen to set the lower element temperature. Feature 'adjust_timer' is chosen to set the timer."
changing_variables = ["variable_upper_element_temperature", "variable_function", "variable_lower_element_temperature", "variable_timer"]
goal_state = Simulator()
# "adjust_upper", step 1, variable_upper_element_temperature
goal_state.variable_upper_element_temperature.set_current_value("450°F")
# "adjust_function", step 1, variable_function
goal_state.variable_function.set_current_value("Toast/Broil")
# "adjust_lower", step 1, variable_lower_element_temperature
goal_state.variable_lower_element_temperature.set_current_value("450°F")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("10")