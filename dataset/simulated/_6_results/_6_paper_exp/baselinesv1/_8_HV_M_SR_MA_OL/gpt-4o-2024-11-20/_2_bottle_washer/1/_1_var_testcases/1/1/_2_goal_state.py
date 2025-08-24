feature_sequence = ["activate_sterilizer"]
feature_choice_reason = "The feature 'activate_sterilizer' is sufficient to turn on the machine and set it to automatic sterilize and dry for 30 minutes."
changing_variables = ["variable_power_on_off", "variable_automatic_dry_time"]
goal_state = ExtendedSimulator()
# "activate_sterilizer", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "activate_sterilizer", step 2, variable_automatic_dry_time
goal_state.variable_automatic_dry_time.set_current_value("30")