feature_sequence = ["set_microwave_cook_time_power"]
feature_choice_reason = "The feature 'set_microwave_cook_time_power' allows setting both the cooking time and power level, which are required to achieve the goal. No additional features are needed as this feature is sufficient to set all necessary variables and start the appliance."
changing_variables = ["variable_time_cook_time", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_microwave_cook_time_power", step 2, variable_time_cook_time
goal_state.variable_time_cook_time.set_current_value("00:08:00") # The number represents minutes and seconds.
# "set_microwave_cook_time_power", step 4, variable_power
goal_state.variable_power.set_current_value("PL9")
# "set_microwave_cook_time_power", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")