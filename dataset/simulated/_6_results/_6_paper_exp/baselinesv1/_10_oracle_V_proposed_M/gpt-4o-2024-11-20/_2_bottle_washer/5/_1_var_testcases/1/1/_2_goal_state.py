feature_sequence = ["power_on_off", "sterilise_only"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'sterilise_only' is required to set the sterilization time to 10 minutes."
changing_variables = ["variable_power_on_off", "variable_sterilise_only_time"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "sterilise_only", step 1, variable_sterilise_only_time
goal_state.variable_sterilise_only_time.set_current_value("10_minutes")