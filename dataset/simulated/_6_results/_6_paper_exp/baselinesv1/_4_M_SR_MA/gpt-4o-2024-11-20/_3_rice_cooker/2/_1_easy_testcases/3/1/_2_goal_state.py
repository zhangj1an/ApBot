feature_sequence = ["select_cooking_mode", "adjust_preset_timer", "start_cooking"]
feature_choice_reason = "Feature 'select_cooking_mode' is used to set the cooking mode to 'congee'. Feature 'adjust_preset_timer' is used to set the preset timer to 12 hours (720 minutes). Feature 'start_cooking' is used to start the machine."
changing_variables = ["variable_cooking_mode", "variable_preset_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_mode", step 1, variable_cooking_mode
goal_state.variable_cooking_mode.set_current_value("congee")
# "adjust_preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(720) # The number represents minutes.
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")