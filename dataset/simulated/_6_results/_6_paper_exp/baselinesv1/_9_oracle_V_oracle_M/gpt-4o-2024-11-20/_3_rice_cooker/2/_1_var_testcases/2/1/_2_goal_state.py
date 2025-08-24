feature_sequence = ["cooking_mode_selection", "preset_timer", "start_cooking"]
feature_choice_reason = "Feature cooking_mode_selection is used to set the cooking mode to soup. Feature preset_timer is used to set the timer to 4 hours. Feature start_cooking is used to start the machine."
changing_variables = ["variable_cooking_mode", "variable_preset_timer", "variable_start_running"]
goal_state = Simulator()
# "cooking_mode_selection", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("Soup")
# "preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(4) # each number represents an hour.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")