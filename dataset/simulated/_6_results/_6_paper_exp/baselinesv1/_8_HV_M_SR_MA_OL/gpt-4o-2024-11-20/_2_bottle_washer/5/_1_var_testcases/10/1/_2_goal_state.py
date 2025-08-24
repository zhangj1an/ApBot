feature_sequence = ["power_on_off", "drying_only_function", "storage_function"]
feature_choice_reason = "The appliance must be turned on first, so 'power_on_off' is included. Then, 'drying_only_function' is used to set the drying duration to 30 minutes. Finally, 'storage_function' is included to enable storage mode."
changing_variables = ["variable_power_on_off", "variable_drying_only_duration", "variable_storage_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "drying_only_function", step 1, variable_drying_only_duration
goal_state.variable_drying_only_duration.set_current_value("30 minutes")
# "storage_function", step 1, variable_storage_mode
goal_state.variable_storage_mode.set_current_value("on")