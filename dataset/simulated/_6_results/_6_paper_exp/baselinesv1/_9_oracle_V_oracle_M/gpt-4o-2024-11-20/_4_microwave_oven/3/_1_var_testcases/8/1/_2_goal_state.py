feature_sequence = ["adjust_upper_tube_temperature", "select_cooking_function", "adjust_lower_tube_temperature", "adjust_cooking_time"]
feature_choice_reason = "Each feature is necessary to independently adjust the respective variables: upper tube temperature, cooking function, lower tube temperature, and cooking time. No redundant features are included."
changing_variables = ["variable_upper_tube_temperature", "variable_function_selection", "variable_lower_tube_temperature", "variable_time_adjustment"]
goal_state = Simulator()
# "adjust_upper_tube_temperature", step 1, variable_upper_tube_temperature
goal_state.variable_upper_tube_temperature.set_current_value(230)
# "select_cooking_function", step 1, variable_function_selection
goal_state.variable_function_selection.set_current_value("upper and lower heating tube")
# "adjust_lower_tube_temperature", step 1, variable_lower_tube_temperature
goal_state.variable_lower_tube_temperature.set_current_value(110)
# "adjust_cooking_time", step 1, variable_time_adjustment
goal_state.variable_time_adjustment.set_current_value(40) # each number represents minutes.