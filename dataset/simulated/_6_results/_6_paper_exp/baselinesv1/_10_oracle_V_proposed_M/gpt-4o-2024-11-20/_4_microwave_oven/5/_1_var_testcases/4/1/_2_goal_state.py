feature_sequence = ["adjust_function_dial", "adjust_temperature_dial", "adjust_selector_dial", "adjust_timer_dial"]
feature_choice_reason = "Each feature is necessary to independently set the respective variables: function dial, temperature dial, selector dial, and timer dial. These features are sufficient to achieve the goal without redundancy."
changing_variables = ["variable_function_dial", "variable_temperature_dial", "variable_selector_dial", "variable_timer_dial"]
goal_state = ExtendedSimulator()
# "adjust_function_dial", step 1, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "adjust_temperature_dial", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("150°C")
# "adjust_selector_dial", step 1, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Top & Bottom Heating")
# "adjust_timer_dial", step 1, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("10 minutes")