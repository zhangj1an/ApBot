feature_sequence = ["power_on_off", "drying_only_function"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the steriliser. Feature 'drying_only_function' is required to set the drying duration to 40 minutes."
changing_variables = ["variable_power_on_off", "variable_drying_only_duration"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "drying_only_function", step 1, variable_drying_only_duration
goal_state.variable_drying_only_duration.set_current_value("40 minutes")