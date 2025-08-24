feature_sequence = ["set_auto_menu", "set_crust_color", "set_loaf_size", "set_timer", "set_gluten_free_mode", "start_or_cancel"]
feature_choice_reason = "Each feature is necessary to set the required configurations: 'set_auto_menu' for French bread, 'set_crust_color' for medium crust, 'set_loaf_size' for 900g loaf size, 'set_timer' for a 3-hour delay, 'set_gluten_free_mode' to enable gluten-free mode, and 'start_or_cancel' to start the appliance."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_timer_setting", "variable_gluten_free_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("French")
# "set_crust_color", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Medium")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "set_timer", step 1, variable_timer_setting
goal_state.variable_timer_setting.set_value_ranges_steps([(0, 54000, 600)], 10800) # 10800 seconds represent 3 hours.
# "set_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "start_or_cancel", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")