feature_sequence = ["set_cooking_mode", "set_preset_timer", "start_running"]
feature_choice_reason = "Feature 'set_cooking_mode' is used to set the cooking mode to 'soup'. Feature 'set_preset_timer' is used to set the timer to 6 hours. Feature 'start_running' is used to start the machine after all configurations are set."
changing_variables = ["variable_cooking_mode", "variable_preset_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_cooking_mode", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("soup")
# "set_preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(360) # each number represents minutes.
# "start_running", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")