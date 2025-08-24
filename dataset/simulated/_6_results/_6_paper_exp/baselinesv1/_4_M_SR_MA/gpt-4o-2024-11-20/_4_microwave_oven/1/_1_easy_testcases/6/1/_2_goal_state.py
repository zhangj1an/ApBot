feature_sequence = ["time_defrost", "speedy_cooking"]
feature_choice_reason = "Feature 'time_defrost' is used to set the defrost time and power level. Feature 'speedy_cooking' is used to start the appliance after the settings are configured."
changing_variables = ["variable_time_defrost", "variable_power", "variable_time_cook_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:15:00")  # 15 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL3")  # 30% power
# "speedy_cooking", step 1, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:15:00")  # 15 minutes
# "speedy_cooking", step 2, variable_start_running
goal_state.variable_start_running.set_current_value("on")