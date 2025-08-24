feature_sequence = ["rotisserie_use"]
feature_choice_reason = "The feature 'rotisserie_use' is sufficient to set all the required variables: variable_function_dial, variable_temperature_dial, variable_selector_dial, and variable_timer_dial."
changing_variables = ["variable_function_dial", "variable_temperature_dial", "variable_selector_dial", "variable_timer_dial"]
goal_state = ExtendedSimulator()
# "rotisserie_use", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Rotisserie")
# "rotisserie_use", step 2, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("250°C")
# "rotisserie_use", step 3, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Top Heating")
# "rotisserie_use", step 4, variable_timer_dial
goal_state.variable_timer_dial.set_current_value(60) # The number represents minutes.