feature_sequence = ["select_cooking_program", "adjust_preset_time", "start_running"]
feature_choice_reason = "Feature 'select_cooking_program' is used to set the cooking program to 'jasmine_rice'. Feature 'adjust_preset_time' is used to set the preset time to 240 minutes (4 hours). Feature 'start_running' is used to turn on the machine and start cooking."
changing_variables = ["variable_cooking_program", "variable_preset_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("jasmine_rice")
# "adjust_preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value(240) # The number represents minutes.
# "start_running", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")