feature_sequence = ["time_defrost", "microwave_cook"]
feature_choice_reason = "Feature 'time_defrost' is used to set the defrost time and power level. However, the appliance needs to be started after setting these configurations, which is handled by 'microwave_cook'."
changing_variables = ["variable_time_defrost", "variable_power", "variable_time_cook_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:20:00")  # 20 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL10")  # 100% power
# "microwave_cook", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:20:00")  # 20 minutes
# "microwave_cook", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")