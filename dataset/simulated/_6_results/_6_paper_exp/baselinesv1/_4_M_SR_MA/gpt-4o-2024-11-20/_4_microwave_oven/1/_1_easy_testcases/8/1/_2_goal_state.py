feature_sequence = ["time_defrost"]
feature_choice_reason = "The feature 'time_defrost' allows setting the defrosting time and adjusting the power level, which are both required for this goal."
changing_variables = ["variable_time_defrost", "variable_power"]
goal_state = ExtendedSimulator()
# "time_defrost", step 1, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:10:00")  # 10 minutes
# "time_defrost", step 2, variable_power
goal_state.variable_power.set_current_value("PL6")  # 60% power