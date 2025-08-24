feature_sequence = ["adjust_function", "adjust_upper", "adjust_lower", "adjust_timer"]
feature_choice_reason = "Feature 'adjust_function' is needed to set the function to Rotisserie. Feature 'adjust_upper' is needed to set the upper element temperature to 450°F. Feature 'adjust_lower' is needed to set the lower element temperature to 450°F. Feature 'adjust_timer' is needed to set the timer to 60 minutes."
changing_variables = ["variable_function", "variable_upper_element_temperature", "variable_lower_element_temperature", "variable_timer"]
goal_state = Simulator()
# "adjust_function", step 1, variable_function
goal_state.variable_function.set_current_value("Rotisserie")
# "adjust_upper", step 1, variable_upper_element_temperature
goal_state.variable_upper_element_temperature.set_current_value("450°F")
# "adjust_lower", step 1, variable_lower_element_temperature
goal_state.variable_lower_element_temperature.set_current_value("450°F")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("60")