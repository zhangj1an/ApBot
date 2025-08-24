feature_sequence = ["set_time_defrost"]
feature_choice_reason = "The feature 'set_time_defrost' allows setting the defrosting time, microwave power, and starting the appliance, which are all required to achieve the goal."
changing_variables = ["variable_time_defrost", "variable_power", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_time_defrost", step 2, variable_time_defrost
goal_state.variable_time_defrost.set_current_value("00:10:00")  # 10 minutes in HH:MM:SS format
# "set_time_defrost", step 4, variable_power
goal_state.variable_power.set_current_value("PL6")  # 60% power level
# "set_time_defrost", step 5, variable_start_running
goal_state.variable_start_running.set_current_value("on")  # Start the appliance