feature_sequence = ["select_cooking_program", "adjust_preset_time", "start_appliance"]
feature_choice_reason = "Feature 'select_cooking_program' is needed to set the cooking program to 'white_rice'. However, the preset finishing time cannot be set in this feature, so 'adjust_preset_time' is added to set the preset time to 8 hours. Finally, 'start_appliance' is required to start the machine."
changing_variables = ["variable_cooking_program", "variable_preset_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("white_rice")
# "adjust_preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value(480) # each number represents a minute.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")