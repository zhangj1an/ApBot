feature_sequence = ["microwave_cook"]
feature_choice_reason = "The feature 'microwave_cook' is sufficient to set the cooking time and power level, as well as start the appliance."
changing_variables = ["variable_time_cook_time", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "microwave_cook", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:05:00")  # The number represents minutes and seconds.
# "microwave_cook", step 4, variable_power
goal_state.variable_power.set_current_value("PL7")
# "microwave_cook", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")