feature_sequence = ["set_cooking_mode", "set_preset_timer", "start_running"]
feature_choice_reason = "Feature 'set_cooking_mode' is required to set the mode to 'cake'. Feature 'set_preset_timer' is required to set the timer to seven hours. Feature 'start_running' is required to start the machine after setting the configurations."
changing_variables = ["variable_cooking_mode", "variable_preset_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_cooking_mode", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("cake")
# "set_preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(420) # The number represents minutes.
# "start_running", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")