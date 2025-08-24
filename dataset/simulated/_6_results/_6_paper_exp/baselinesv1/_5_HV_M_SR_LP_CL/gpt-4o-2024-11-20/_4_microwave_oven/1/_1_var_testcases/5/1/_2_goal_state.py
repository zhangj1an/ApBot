feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature is sufficient to set the defrost time to 20 minutes and the power level to 100% (PL10). It also includes the ability to start the appliance."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:20:00")  # 20 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL10")
# "time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")