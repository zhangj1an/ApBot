feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature is chosen because it allows setting the defrost time and adjusting the power level, which are both required to achieve the goal. The appliance will start automatically after setting these configurations."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:10:00") # The number represents minutes and seconds.
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL6")
# "time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")