feature_sequence = ["microwave_cook"]
feature_choice_reason = "The feature 'microwave_cook' allows setting both the cooking time and power level, which are required to achieve the goal. No additional features are needed as this feature is sufficient to set the appliance to run."
changing_variables = ["variable_time_cook_time", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "microwave_cook", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:08:00")  # 8 minutes
# "microwave_cook", step 4, variable_power
goal_state.variable_power.set_current_value("PL9")  # 90% power
# "microwave_cook", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")