feature_sequence = ["time_defrost"]
feature_choice_reason = "Feature 'time_defrost' is used to set the defrosting time, power level, and start the appliance. This feature is sufficient to achieve the goal without requiring additional features."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:10:00")  # 10 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL6")  # 60% power
# "time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")