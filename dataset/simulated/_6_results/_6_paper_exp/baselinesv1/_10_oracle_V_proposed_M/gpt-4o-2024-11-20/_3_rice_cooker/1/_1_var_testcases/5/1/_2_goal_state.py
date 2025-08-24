feature_sequence = ["select_menu_option", "set_preset_timer", "start_cooking"]
feature_choice_reason = "Feature 'select_menu_option' is used to set the menu to 'Soup'. Feature 'set_preset_timer' is required to set the preset timer to 4 hours. Feature 'start_cooking' is necessary to start the cooking process."
changing_variables = ["variable_menu_index", "variable_preset_timer_hours", "variable_preset_timer_minutes", "variable_start_cooking"]
goal_state = ExtendedSimulator()
# "select_menu_option", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Soup")
# "set_preset_timer", step 2, variable_preset_timer_hours
goal_state.variable_preset_timer_hours.set_current_value(4) # The number represents hours.
# "set_preset_timer", step 3, variable_preset_timer_minutes
goal_state.variable_preset_timer_minutes.set_current_value(0) # The number represents minutes.
# "start_cooking", step 1, variable_start_cooking
goal_state.variable_start_cooking.set_current_value("on")