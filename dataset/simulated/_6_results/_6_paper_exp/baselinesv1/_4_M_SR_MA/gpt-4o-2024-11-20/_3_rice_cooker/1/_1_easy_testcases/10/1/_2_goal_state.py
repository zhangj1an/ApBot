feature_sequence = ["set_cooking_mode", "adjust_cooking_time", "start_appliance"]
feature_choice_reason = "Feature 'set_cooking_mode' is used to set the cooking mode to 'Glutinous rice'. Feature 'adjust_cooking_time' is used to set the cooking time to 1 hour and 10 minutes. Feature 'start_appliance' is used to start the appliance after all configurations are set."
changing_variables = ["variable_cooking_mode", "variable_cooking_time_hr", "variable_cooking_time_min", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_cooking_mode", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("Glutinous rice")
# "adjust_cooking_time", step 2, variable_cooking_time_hr
goal_state.variable_cooking_time_hr.set_current_value(1) # each number represents an hour.
# "adjust_cooking_time", step 3, variable_cooking_time_min
goal_state.variable_cooking_time_min.set_current_value(10) # each number represents a minute.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")