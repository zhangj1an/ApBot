feature_sequence = ["rotisserie_use"]
feature_choice_reason = "The feature 'rotisserie_use' is chosen because it allows setting the function dial to 'Rotisserie', temperature dial to '250°C', selector dial to 'Top Heating', and timer to '60'. All required variables can be set within this feature."
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