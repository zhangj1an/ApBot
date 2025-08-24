feature_sequence = ["microwave_cook"]
feature_choice_reason = "The feature 'microwave_cook' allows setting both the cooking time and power level, which are required to achieve the goal."
changing_variables = ["variable_time_cook_time", "variable_power"]
goal_state = ExtendedSimulator()
# "microwave_cook", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:09:00")  # 9 minutes
# "microwave_cook", step 4, variable_power
goal_state.variable_power.set_current_value("PL6")  # 60% power