feature_sequence = ["adjust_temperature_dial", "adjust_function_dial", "adjust_selector_dial", "adjust_timer_dial"]
feature_choice_reason = "Feature 'adjust_temperature_dial' is chosen to set the temperature to 100°C. Feature 'adjust_function_dial' is chosen to set the function dial to 'Convection'. Feature 'adjust_selector_dial' is chosen to set the selector dial to 'Bottom Heating'. Feature 'adjust_timer_dial' is chosen to set the timer to '40 minutes'."
changing_variables = ["variable_temperature_dial", "variable_function_dial", "variable_selector_dial", "variable_timer_dial"]
goal_state = ExtendedSimulator()
# "adjust_temperature_dial", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("100°C")
# "adjust_function_dial", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "adjust_selector_dial", step 1, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Bottom Heating")
# "adjust_timer_dial", step 1, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("40 minutes")