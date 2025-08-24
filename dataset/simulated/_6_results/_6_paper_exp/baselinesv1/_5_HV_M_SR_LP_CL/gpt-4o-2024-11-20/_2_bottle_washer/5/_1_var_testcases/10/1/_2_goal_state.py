feature_sequence = ["power_on_off", "drying_only_function", "storage_function"]
feature_choice_reason = "The 'power_on_off' feature is required to turn on the appliance if it is off. The 'drying_only_function' feature is needed to set the drying duration to 30 minutes. The 'storage_function' feature is required to enable storage mode."
changing_variables = ["variable_power_on_off", "variable_drying_only_duration", "variable_storage_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "drying_only_function", step 1, variable_drying_only_duration
goal_state.variable_drying_only_duration.set_current_value("30 minutes")
# "storage_function", step 1, variable_storage_mode
goal_state.variable_storage_mode.set_current_value("on")