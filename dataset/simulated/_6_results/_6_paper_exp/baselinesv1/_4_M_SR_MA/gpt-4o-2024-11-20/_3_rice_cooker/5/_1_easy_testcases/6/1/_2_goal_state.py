feature_sequence = ["adjust_preset_time", "select_cooking_program", "start_appliance"]
feature_choice_reason = "Feature 'adjust_preset_time' is included to set the variable_preset_time to 7 hours (420 minutes). Feature 'select_cooking_program' is included to set the variable_cooking_program to 'jasmine_rice'. Feature 'start_appliance' is included to set the variable_start_running to 'on' and start the machine."
changing_variables = ["variable_preset_time", "variable_cooking_program", "variable_start_running"]
goal_state = ExtendedSimulator()
# "adjust_preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value(420)
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("jasmine_rice")
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")