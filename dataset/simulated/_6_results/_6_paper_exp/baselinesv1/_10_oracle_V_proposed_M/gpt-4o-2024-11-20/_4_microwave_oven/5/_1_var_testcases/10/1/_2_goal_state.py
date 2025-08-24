feature_sequence = ["adjust_function_dial", "adjust_temperature_dial", "adjust_selector_dial", "adjust_timer_dial"]
feature_choice_reason = "Feature 'adjust_function_dial' is required to set the function dial to 'Convection'. Feature 'adjust_temperature_dial' is required to set the temperature dial to '200°C'. Feature 'adjust_selector_dial' is required to set the selector dial to 'Top & Bottom Heating'. Feature 'adjust_timer_dial' is required to set the timer dial to '20 minutes'."
changing_variables = ["variable_function_dial", "variable_temperature_dial", "variable_selector_dial", "variable_timer_dial"]
goal_state = ExtendedSimulator()
# "adjust_function_dial", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "adjust_temperature_dial", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("200°C")
# "adjust_selector_dial", step 1, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Top & Bottom Heating")
# "adjust_timer_dial", step 1, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("20 minutes")