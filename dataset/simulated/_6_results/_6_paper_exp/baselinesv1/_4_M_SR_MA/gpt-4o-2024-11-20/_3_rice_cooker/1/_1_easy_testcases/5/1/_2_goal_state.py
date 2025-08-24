feature_sequence = ["set_cooking_mode", "set_preset_time", "start_appliance"]
feature_choice_reason = "Feature 'set_cooking_mode' is used to set the variable_cooking_mode to 'Soup'. Feature 'set_preset_time' is used to set the preset timer to 4 hours. Finally, feature 'start_appliance' is used to start the appliance."
changing_variables = ["variable_cooking_mode", "variable_preset_time_hr", "variable_preset_time_min", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_cooking_mode", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("Soup")
# "set_preset_time", step 2, variable_preset_time_hr
goal_state.variable_preset_time_hr.set_current_value(4) # each number represents an hour.
# "set_preset_time", step 3, variable_preset_time_min
goal_state.variable_preset_time_min.set_current_value(0) # each number represents a minute.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")