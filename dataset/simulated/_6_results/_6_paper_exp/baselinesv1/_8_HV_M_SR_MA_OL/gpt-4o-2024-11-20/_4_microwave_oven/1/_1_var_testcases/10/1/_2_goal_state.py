feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature allows setting the defrost time and adjusting the power level, which are both required for this task."
changing_variables = ["variable_time_defrost", "variable_power"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:05:00") # The number represents minutes and seconds.
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL3")