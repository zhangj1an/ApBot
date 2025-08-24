feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature is chosen because it allows setting the defrosting time and microwave power level, which are required to achieve the goal."
changing_variables = ["variable_time_defrost", "variable_microwave_power_level"]
goal_state = Simulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:10:00")  # 10 minutes
# "time_defrost", step 4, variable_microwave_power_level
goal_state.variable_microwave_power_level.set_current_value("PL6")  # 60% power