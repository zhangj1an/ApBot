feature_sequence = ["power_on_off", "sterilise_only", "storage_mode"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'sterilise_only' is needed to set sterilisation to 35 minutes. Feature 'storage_mode' is required to enable storage mode."
changing_variables = ["variable_power_on_off", "variable_sterilise_only_time", "variable_storage_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "sterilise_only", step 1, variable_sterilise_only_time
goal_state.variable_sterilise_only_time.set_current_value("35_minutes")
# "storage_mode", step 1, variable_storage_mode
goal_state.variable_storage_mode.set_current_value("on")