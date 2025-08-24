feature_sequence = ["cooking_program_selection", "preset_time", "start_function"]
feature_choice_reason = "Feature 'cooking_program_selection' is used to set the cooking program to 'brown_rice'. Feature 'preset_time' is used to set the preset finish time to 9 hours. Feature 'start_function' is used to start the machine."
changing_variables = ["variable_cooking_program", "variable_preset_time", "variable_start_running"]
goal_state = Simulator()
# "cooking_program_selection", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("brown_rice")
# "preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value("09:00:00") # each number represents hours, minutes, and seconds
# "start_function", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")