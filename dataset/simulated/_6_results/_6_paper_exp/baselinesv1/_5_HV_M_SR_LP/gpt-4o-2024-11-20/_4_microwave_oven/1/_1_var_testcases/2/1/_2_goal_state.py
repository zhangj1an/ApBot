feature_sequence = ["microwave_cook"]
feature_choice_reason = "The 'microwave_cook' feature allows setting the cooking time and adjusting the power level, which are both required to achieve the goal."
changing_variables = ["variable_time_cook_time", "variable_power"]
goal_state = ExtendedSimulator()
# "microwave_cook", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:06:00")  # 6 minutes
# "microwave_cook", step 4, variable_power
goal_state.variable_power.set_current_value("PL8")  # 80% power