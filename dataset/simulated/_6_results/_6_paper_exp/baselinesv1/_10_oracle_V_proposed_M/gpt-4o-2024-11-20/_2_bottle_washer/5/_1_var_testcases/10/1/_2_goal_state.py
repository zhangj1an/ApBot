feature_sequence = ["power_on_off", "drying_only", "storage_mode"]
feature_choice_reason = "The appliance must be turned on first, so 'power_on_off' is included. Then, 'drying_only' is selected to set the drying time to 30 minutes. Finally, 'storage_mode' is included to enable storage mode."
changing_variables = ["variable_power_on_off", "variable_drying_only_time", "variable_storage_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "drying_only", step 1, variable_drying_only_time
goal_state.variable_drying_only_time.set_current_value("30_minutes")
# "storage_mode", step 1, variable_storage_mode
goal_state.variable_storage_mode.set_current_value("on")