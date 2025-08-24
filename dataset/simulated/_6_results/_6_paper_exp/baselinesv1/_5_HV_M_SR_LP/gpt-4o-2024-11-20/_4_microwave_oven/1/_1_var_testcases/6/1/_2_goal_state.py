feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature is chosen because it allows setting the defrost time and power level, which are required to achieve the goal."
changing_variables = ["variable_time_defrost", "variable_power"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:15:00")  # 15 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL3")  # 30% power