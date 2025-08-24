feature_sequence = ["set_auto_menu", "set_crust_color", "set_loaf_size", "set_timer", "set_gluten_free_mode", "start_or_cancel"]
feature_choice_reason = "Feature 'set_auto_menu' is used to set the menu to French. Feature 'set_crust_color' is used to set the crust color to Dark. Feature 'set_loaf_size' is used to set the loaf size to 450g. Feature 'set_timer' is used to set a 3-hour delay. Feature 'set_gluten_free_mode' is used to activate the gluten-free setting. Feature 'start_or_cancel' is used to start the bread maker."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_timer_setting", "variable_gluten_free_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("French")
# "set_crust_color", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Dark")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("450g")
# "set_timer", step 1, variable_timer_setting
goal_state.variable_timer_setting.set_current_value(600) # The number represents seconds. Adjusted to the closest valid value within the range.
# "set_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "start_or_cancel", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")