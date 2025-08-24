feature_sequence = ["adjust_upper_tube_temperature", "adjust_function_selection", "adjust_lower_tube_temperature", "adjust_time_or_stay_on"]
feature_choice_reason = "Feature 'adjust_upper_tube_temperature' is required to set variable_upper_tube_temperature to 150°C. Feature 'adjust_function_selection' is required to set variable_function_selection to 'upper_and_lower_tubes'. Feature 'adjust_lower_tube_temperature' is required to set variable_lower_tube_temperature to 190°C. Feature 'adjust_time_or_stay_on' is required to set variable_time_adjustment to 30 minutes."
changing_variables = ["variable_upper_tube_temperature", "variable_function_selection", "variable_lower_tube_temperature", "variable_time_adjustment"]
goal_state = ExtendedSimulator()
# "adjust_upper_tube_temperature", step 1, variable_upper_tube_temperature
goal_state.variable_upper_tube_temperature.set_current_value(150)
# "adjust_function_selection", step 1, variable_function_selection
goal_state.variable_function_selection.set_current_value("upper_and_lower_tubes")
# "adjust_lower_tube_temperature", step 1, variable_lower_tube_temperature
goal_state.variable_lower_tube_temperature.set_current_value(190)
# "adjust_time_or_stay_on", step 1, variable_time_adjustment
goal_state.variable_time_adjustment.set_current_value(30) # The number represents minutes.