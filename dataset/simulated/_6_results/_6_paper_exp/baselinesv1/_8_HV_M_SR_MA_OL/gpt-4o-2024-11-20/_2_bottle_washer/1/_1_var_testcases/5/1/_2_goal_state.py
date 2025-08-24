feature_sequence = ["activate_sterilizer", "dryer_only_time"]
feature_choice_reason = "Feature 'activate_sterilizer' is required to turn on the appliance. Feature 'dryer_only_time' is required to set the drying time to 30 minutes."
changing_variables = ["variable_power_on_off", "variable_dryer_only_time"]
goal_state = ExtendedSimulator()
# "activate_sterilizer", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "dryer_only_time", step 1, variable_dryer_only_time
goal_state.variable_dryer_only_time.set_current_value("30")