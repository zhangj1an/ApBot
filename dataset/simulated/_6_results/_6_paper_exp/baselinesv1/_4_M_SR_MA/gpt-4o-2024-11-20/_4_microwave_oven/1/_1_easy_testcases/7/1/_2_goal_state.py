feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature allows setting the defrosting time and adjusting the power level, which are both required to achieve the goal."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:20:00")  # 20 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL2")  # 20% power
# "time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")