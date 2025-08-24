feature_sequence = ["set_auto_menu", "set_crust_color", "set_loaf_size", "set_timer", "set_gluten_free_mode", "start_or_cancel"]
feature_choice_reason = "Feature 'set_auto_menu' is needed to set the menu to 'French'. Feature 'set_crust_color' is required to set the crust color to 'Medium'. Feature 'set_loaf_size' is necessary to set the loaf size to '680g'. Feature 'set_timer' is required to set a 2-hour delay. Feature 'set_gluten_free_mode' is needed to enable the gluten-free setting. Finally, 'start_or_cancel' is required to start the Bread Maker."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_timer_setting", "variable_gluten_free_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("French")
# "set_crust_color", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Medium")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("680g")
# "set_timer", step 1, variable_timer_setting
goal_state.variable_timer_setting.set_value_ranges_steps([(0, 54000, 600)], 7200) # Adjusting range and step to match 2 hours (7200 seconds)
# "set_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "start_or_cancel", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")