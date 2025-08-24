feature_sequence = ["power_on_off", "automatic_sterilize_dry"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'automatic_sterilize_dry' is required to set the drying time to 30 minutes for sterilization and drying."
changing_variables = ["variable_power_on_off", "variable_dry_time"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "automatic_sterilize_dry", step 1, variable_dry_time
goal_state.variable_dry_time.set_current_value("30")