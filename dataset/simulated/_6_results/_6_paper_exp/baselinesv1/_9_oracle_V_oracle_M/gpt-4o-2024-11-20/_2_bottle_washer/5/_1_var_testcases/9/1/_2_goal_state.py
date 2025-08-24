feature_sequence = ["turn_on_off", "auto_mode", "storage_mode"]
feature_choice_reason = "Feature 'turn_on_off' is required to activate the appliance. Feature 'auto_mode' is needed to set the 60-minute auto cycle. Feature 'storage_mode' is required to ensure items are stored post-operation."
changing_variables = ["variable_power_on_off", "variable_auto_mode_time", "variable_storage_mode"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "auto_mode", step 1, variable_auto_mode_time
goal_state.variable_auto_mode_time.set_current_value("60")
# "storage_mode", step 1, variable_storage_mode
goal_state.variable_storage_mode.set_current_value("on")