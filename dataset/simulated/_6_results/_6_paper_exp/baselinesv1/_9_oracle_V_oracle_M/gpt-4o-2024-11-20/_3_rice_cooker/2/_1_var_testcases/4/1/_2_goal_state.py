feature_sequence = ["cooking_mode_selection", "preset_timer", "start_cooking"]
feature_choice_reason = "Feature cooking_mode_selection is required to set the mode to white rice. Feature preset_timer is required to set the timer for 2 hours. Feature start_cooking is required to start the machine."
changing_variables = ["variable_cooking_mode", "variable_preset_timer", "variable_start_running"]
goal_state = Simulator()
# "cooking_mode_selection", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("White rice")
# "preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(2) # The number represents hours.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")