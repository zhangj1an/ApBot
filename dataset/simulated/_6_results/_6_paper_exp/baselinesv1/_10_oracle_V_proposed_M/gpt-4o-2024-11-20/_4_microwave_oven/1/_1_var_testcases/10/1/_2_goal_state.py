feature_sequence = ["set_time_defrost"]
feature_choice_reason = "The feature 'set_time_defrost' allows setting both the defrost time and the power level, which are required to achieve the goal. No additional features are needed as this feature is sufficient to set all necessary variables."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:05:00")  # 5 minutes
# "set_time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL3")  # 30% power
# "set_time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")