feature_sequence = ["power_on_off", "auto_mode", "storage_function"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'auto_mode' is needed to set the 60-minute auto cycle. Feature 'storage_function' is required to activate storage mode post-operation."
changing_variables = ["variable_power_on_off", "variable_auto_mode_duration", "variable_storage_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "auto_mode", step 1, variable_auto_mode_duration
goal_state.variable_auto_mode_duration.set_current_value("60 minutes")
# "storage_function", step 1, variable_storage_mode
goal_state.variable_storage_mode.set_current_value("on")