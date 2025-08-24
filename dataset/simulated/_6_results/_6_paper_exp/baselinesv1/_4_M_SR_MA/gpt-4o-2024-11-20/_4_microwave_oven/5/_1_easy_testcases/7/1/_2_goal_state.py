feature_sequence = ["general_cooking"]
feature_choice_reason = "The 'general_cooking' feature is sufficient to set all the required variables: temperature, function dial, selector dial, and timer."
changing_variables = ["variable_temperature_dial", "variable_function_dial", "variable_selector_dial", "variable_timer_dial"]
goal_state = ExtendedSimulator()
# "general_cooking", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("250°C")
# "general_cooking", step 2, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "general_cooking", step 3, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Top & Bottom Heating")
# "general_cooking", step 4, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("40 minutes")