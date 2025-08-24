feature_sequence = ["set_time_defrost"]
feature_choice_reason = "The feature 'set_time_defrost' is sufficient to set the defrost time to 20 minutes and adjust the power to 100% (PL10). It also starts the appliance as part of its process."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:20:00")  # 20 minutes
# "set_time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL10")
# "set_time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")