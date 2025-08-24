feature_sequence = ["time_defrost"]
feature_choice_reason = "The 'time_defrost' feature is used to set the defrost time and adjust the power level. This feature is sufficient to achieve the goal of defrosting for 20 minutes with 100% power and starting the appliance."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:20:00")  # 20 minutes
# "time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL10")  # 100% power
# "time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")  # Start the appliance