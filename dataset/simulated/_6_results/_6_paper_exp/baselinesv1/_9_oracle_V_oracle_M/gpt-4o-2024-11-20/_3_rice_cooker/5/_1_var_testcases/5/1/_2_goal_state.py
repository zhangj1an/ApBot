feature_sequence = ["cooking_program_selection", "preset_time", "start_function"]
feature_choice_reason = "The feature 'cooking_program_selection' is required to set the cooking mode to 'glutinous_rice'. The feature 'preset_time' is required to set the preset time to 6 hours. Finally, the feature 'start_function' is required to start the machine."
changing_variables = ["variable_cooking_program", "variable_preset_time", "variable_start_running"]
goal_state = Simulator()
# "cooking_program_selection", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("glutinous_rice")
# "preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value("06:00:00") # each number represents hours:minutes:seconds
# "start_function", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")