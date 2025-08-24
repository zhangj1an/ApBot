feature_sequence = ["microwave_cook"]
feature_choice_reason = "The 'microwave_cook' feature is sufficient to set the cooking time, power level, and start the appliance."
changing_variables = ["variable_time_cook_time", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "microwave_cook", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:05:00") # 5 minutes
# "microwave_cook", step 4, variable_power
goal_state.variable_power.set_current_value("PL7") # 70% power
# "microwave_cook", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")