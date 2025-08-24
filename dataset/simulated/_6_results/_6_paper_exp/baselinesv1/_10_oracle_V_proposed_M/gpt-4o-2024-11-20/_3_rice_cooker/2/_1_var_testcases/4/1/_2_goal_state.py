feature_sequence = ["set_cooking_mode", "set_preset_timer", "start_running"]
feature_choice_reason = "Feature 'set_cooking_mode' is used to set the cooking mode to 'white rice'. However, the preset timer needs to be set for delayed cooking, which cannot be done in 'set_cooking_mode'. Therefore, 'set_preset_timer' is added to set the timer to 2 hours. Finally, 'start_running' is required to start the machine."
changing_variables = ["variable_cooking_mode", "variable_preset_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_cooking_mode", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("white rice")
# "set_preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(120) # The number represents minutes.
# "start_running", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")