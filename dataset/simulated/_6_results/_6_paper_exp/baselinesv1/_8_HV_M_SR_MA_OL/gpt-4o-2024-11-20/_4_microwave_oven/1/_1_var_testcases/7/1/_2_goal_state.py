feature_sequence = ["time_defrost"]
feature_choice_reason = "The feature 'time_defrost' is sufficient to set both the defrosting time and the power level as required by the user instruction."
changing_variables = ["variable_time_defrost", "variable_power"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:20:00")  # 20 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL2")