feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature is sufficient to set the defrost time, adjust the power level, and start the appliance."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:05:00") # The number represents minutes and seconds.
# "time_defrost", step 3, variable_power
goal_state.variable_power.set_current_value("PL3")
# "time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")