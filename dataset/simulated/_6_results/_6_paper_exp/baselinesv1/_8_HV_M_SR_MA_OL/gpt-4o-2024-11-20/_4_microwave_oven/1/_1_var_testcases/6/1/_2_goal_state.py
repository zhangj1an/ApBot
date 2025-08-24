feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature is sufficient to set the defrosting time to 15 minutes and power to 30%, and it also starts the appliance."
changing_variables = ["variable_time_defrost", "variable_power"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:15:00")  # 15 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL3")  # 30% power