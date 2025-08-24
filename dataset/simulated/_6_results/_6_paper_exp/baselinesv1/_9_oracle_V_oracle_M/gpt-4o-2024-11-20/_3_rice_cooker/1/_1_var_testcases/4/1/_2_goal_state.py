feature_sequence = ["cooking", "preset_timer", "start"]
feature_choice_reason = "Feature 'cooking' is chosen to set the menu to 'Glutinous rice'. Feature 'preset_timer' is chosen to set the preset timer to 3 hours. Feature 'start' is chosen to start the cooking process."
changing_variables = ["variable_menu_index", "variable_preset_timer_hour", "variable_preset_timer_minute", "variable_start_running"]
goal_state = Simulator()
# "cooking", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Glutinous rice")
# "preset_timer", step 2, variable_preset_timer_hour
goal_state.variable_preset_timer_hour.set_current_value(3) # each number represents an hour.
# "preset_timer", step 3, variable_preset_timer_minute
goal_state.variable_preset_timer_minute.set_current_value(0) # each number represents minutes.
# "start", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")