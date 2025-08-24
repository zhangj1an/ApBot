feature_sequence = ["adjust_upper_element_temperature", "adjust_lower_element_temperature", "adjust_function_dial", "adjust_timer_dial"]
feature_choice_reason = "Feature 'adjust_upper_element_temperature' is required to set the upper element to 350°F. Feature 'adjust_lower_element_temperature' is required to set the lower element to 450°F. Feature 'adjust_function_dial' is required to set the function to Convection. Feature 'adjust_timer_dial' is required to set the timer to 30 minutes."
changing_variables = ["variable_upper_element_temperature", "variable_lower_element_temperature", "variable_function_dial", "variable_timer"]
goal_state = ExtendedSimulator()
# "adjust_upper_element_temperature", step 1, variable_upper_element_temperature
goal_state.variable_upper_element_temperature.set_current_value("350")
# "adjust_lower_element_temperature", step 1, variable_lower_element_temperature
goal_state.variable_lower_element_temperature.set_current_value("450")
# "adjust_function_dial", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "adjust_timer_dial", step 1, variable_timer
goal_state.variable_timer.set_current_value(30) # The number represents minutes.