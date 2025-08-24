feature_sequence = ["general_cooking"]
feature_choice_reason = "The feature 'general_cooking' is sufficient to set all the required variables: variable_temperature_dial, variable_function_dial, variable_selector_dial, and variable_timer_dial. This feature also ensures the appliance starts running automatically after setting the timer."
changing_variables = ["variable_temperature_dial", "variable_function_dial", "variable_selector_dial", "variable_timer_dial", "variable_start_running"]
goal_state = ExtendedSimulator()
# "general_cooking", step 1, variable_temperature_dial
goal_state.variable_temperature_dial.set_current_value("200°C")
# "general_cooking", step 2, variable_function_dial
goal_state.variable_function_dial.set_current_value("Convection")
# "general_cooking", step 3, variable_selector_dial
goal_state.variable_selector_dial.set_current_value("Top & Bottom Heating")
# "general_cooking", step 4, variable_timer_dial
goal_state.variable_timer_dial.set_current_value("20 minutes")
# Automatically set to running state
goal_state.variable_start_running.set_current_value("on")