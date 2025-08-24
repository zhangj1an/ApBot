feature_sequence = ["power_on_off", "sterilise_only_function", "storage_function"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'sterilise_only_function' is needed to set the sterilization duration to 35 minutes. Feature 'storage_function' is required to enable storage mode."
changing_variables = ["variable_power_on_off", "variable_sterilise_only_duration", "variable_storage_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "sterilise_only_function", step 1, variable_sterilise_only_duration
goal_state.variable_sterilise_only_duration.set_current_value("35 minutes")
# "storage_function", step 1, variable_storage_mode
goal_state.variable_storage_mode.set_current_value("on")