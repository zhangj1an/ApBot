feature_sequence = ["adjust_upper_tube_temperature", "adjust_function_selection", "adjust_lower_tube_temperature", "adjust_cooking_time_and_start"]
feature_choice_reason = "Feature 'adjust_upper_tube_temperature' is required to set the upper tube temperature. Feature 'adjust_function_selection' is required to select the cooking function. Feature 'adjust_lower_tube_temperature' is required to set the lower tube temperature. Feature 'adjust_cooking_time_and_start' is required to set the cooking time and start the appliance."
changing_variables = ["variable_upper_tube_temperature", "variable_function_selection", "variable_lower_tube_temperature", "variable_time_adjustment"]

goal_state = ExtendedSimulator()
# "adjust_upper_tube_temperature", step 1, variable_upper_tube_temperature
goal_state.variable_upper_tube_temperature.set_current_value(150)
# "adjust_function_selection", step 1, variable_function_selection
goal_state.variable_function_selection.set_current_value("upper_and_lower_tubes")
# "adjust_lower_tube_temperature", step 1, variable_lower_tube_temperature
goal_state.variable_lower_tube_temperature.set_current_value(150)
# "adjust_cooking_time_and_start", step 1, variable_time_adjustment
goal_state.variable_time_adjustment.set_current_value(20) # each number represents minutes.