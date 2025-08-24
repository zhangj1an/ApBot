feature_sequence = ["adjust_function_dial", "adjust_temperature_dial", "adjust_selector_dial", "adjust_timer_dial"]
feature_choice_reason = "Feature 'adjust_function_dial' is required to set the function dial to 'Convection'. Feature 'adjust_temperature_dial' is required to set the temperature dial to '250°C'. Feature 'adjust_selector_dial' is required to set the selector dial to 'Bottom Heating'. Feature 'adjust_timer_dial' is required to set the timer to '40 minutes' and automatically start the microwave."
changing_variables = ["variable_function_dial", "variable_temperature_dial", "variable_selector_dial", "variable_timer_dial", "variable_start_running"]
goal_state = ExtendedSimulator()
# "adjust_function_dial", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "adjust_temperature_dial", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("250°C")
# "adjust_selector_dial", step 1, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Bottom Heating")
# "adjust_timer_dial", step 1, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("40 minutes")
# "adjust_timer_dial", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")