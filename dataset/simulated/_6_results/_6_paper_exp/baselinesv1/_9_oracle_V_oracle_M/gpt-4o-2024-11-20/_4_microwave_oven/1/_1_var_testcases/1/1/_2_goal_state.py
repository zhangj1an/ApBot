feature_sequence = ["microwave_cook"]
feature_choice_reason = "The 'microwave_cook' feature allows setting both the cooking time and the power level, which are required to achieve the goal."
changing_variables = ["variable_microwave_cooking_time", "variable_microwave_power_level"]
goal_state = Simulator()
# "microwave_cook", step 2, variable_microwave_cooking_time
goal_state.variable_microwave_cooking_time.set_current_value("00:08:00")  # 8 minutes
# "microwave_cook", step 4, variable_microwave_power_level
goal_state.variable_microwave_power_level.set_current_value("PL9")  # 90% power