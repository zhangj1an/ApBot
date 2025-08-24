feature_sequence = ["start_appliance", "select_cooking_program", "adjust_preset_time", "start_appliance"]
feature_choice_reason = "The first 'start_appliance' feature is needed to turn on the machine. The 'select_cooking_program' feature is required to set the cooking program to 'brown_rice'. The 'adjust_preset_time' feature is necessary to set the preset finish time to 9 hours. Finally, the second 'start_appliance' feature is needed to start the machine after all configurations are set."
changing_variables = ["variable_start_running", "variable_cooking_program", "variable_preset_time"]

goal_state = ExtendedSimulator()
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("brown_rice")
# "adjust_preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value(540)  # The number represents minutes.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")