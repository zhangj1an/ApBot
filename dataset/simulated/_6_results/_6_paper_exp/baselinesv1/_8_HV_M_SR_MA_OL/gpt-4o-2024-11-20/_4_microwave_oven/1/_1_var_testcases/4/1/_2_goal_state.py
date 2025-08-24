feature_sequence = ["microwave_cook", "speedy_cooking"]
feature_choice_reason = "Feature 'microwave_cook' is used to set the cooking time and power level. Feature 'speedy_cooking' is used to start the appliance."
changing_variables = ["variable_time_cook_time", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "microwave_cook", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:09:00")  # 9 minutes
# "microwave_cook", step 4, variable_power
goal_state.variable_power.set_current_value("PL6")  # 60% power
# "speedy_cooking", step 2, variable_start_running
goal_state.variable_start_running.set_current_value("on")