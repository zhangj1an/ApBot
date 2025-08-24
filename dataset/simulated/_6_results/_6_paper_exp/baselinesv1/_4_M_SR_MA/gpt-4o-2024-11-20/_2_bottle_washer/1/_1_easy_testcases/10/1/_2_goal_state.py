feature_sequence = ["activate_sterilizer", "automatic_sterilize_dry_time"]
feature_choice_reason = "Feature 'activate_sterilizer' is required to turn on the appliance. Feature 'automatic_sterilize_dry_time' is needed to set the drying time to 60 minutes for the automatic sterilize and dry function."
changing_variables = ["variable_power_on_off", "variable_dry_time"]
goal_state = ExtendedSimulator()
# "activate_sterilizer", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "automatic_sterilize_dry_time", step 1, variable_dry_time
goal_state.variable_dry_time.set_current_value("60")