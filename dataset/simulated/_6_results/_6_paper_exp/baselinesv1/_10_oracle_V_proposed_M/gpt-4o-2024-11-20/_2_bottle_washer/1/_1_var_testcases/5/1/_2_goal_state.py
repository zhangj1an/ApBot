feature_sequence = ["power_on_off", "dryer_only"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'dryer_only' is required to set the dry-only function for 30 minutes."
changing_variables = ["variable_power_on_off", "variable_dryer_only_time"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "dryer_only", step 1, variable_dryer_only_time
goal_state.variable_dryer_only_time.set_current_value("30")