feature_sequence = ["power_on_off", "sterilise_only_function"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the steriliser. Feature 'sterilise_only_function' is required to set the sterilisation duration to 10 minutes."
changing_variables = ["variable_power_on_off", "variable_sterilise_only_duration"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "sterilise_only_function", step 1, variable_sterilise_only_duration
goal_state.variable_sterilise_only_duration.set_current_value("10 minutes")