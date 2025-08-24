feature_sequence = ["select_cooking_program", "adjust_preset_time", "start_appliance"]
feature_choice_reason = "Feature 'select_cooking_program' is used to set variable_cooking_program to 'white_rice'. Feature 'adjust_preset_time' is used to set variable_preset_time to 480 (8 hours in minutes). Feature 'start_appliance' is used to set variable_start_running to 'on' to start the machine."
changing_variables = ["variable_cooking_program", "variable_preset_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("white_rice")
# "adjust_preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value(480) # The number represents minutes.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")