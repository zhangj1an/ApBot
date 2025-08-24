feature_sequence = ["set_cooking_mode", "adjust_cooking_time", "start_appliance"]
feature_choice_reason = "Feature 'set_cooking_mode' is required to select the 'Steam' function. Feature 'adjust_cooking_time' is needed to set the cooking time to 10 minutes. Feature 'start_appliance' is necessary to start the appliance after setting the configurations."
changing_variables = ["variable_cooking_mode", "variable_cooking_time_hr", "variable_cooking_time_min", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_cooking_mode", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("Steam")
# "adjust_cooking_time", step 2, variable_cooking_time_hr
goal_state.variable_cooking_time_hr.set_current_value(0) # each number represents an hour.
# "adjust_cooking_time", step 3, variable_cooking_time_min
goal_state.variable_cooking_time_min.set_current_value(10) # each number represents a minute.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")