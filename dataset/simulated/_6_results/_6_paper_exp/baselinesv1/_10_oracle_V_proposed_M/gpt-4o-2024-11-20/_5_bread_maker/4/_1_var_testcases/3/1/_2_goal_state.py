feature_sequence = ["set_auto_menu", "set_crust_color", "set_loaf_size", "set_gluten_free_mode", "set_timer", "start_or_cancel"]
feature_choice_reason = "Feature 'set_auto_menu' is required to select the 'Whole Wheat' menu. Feature 'set_crust_color' is needed to set the crust color to 'Dark'. Feature 'set_loaf_size' is necessary to set the loaf size to 900g. Feature 'set_gluten_free_mode' is included to enable the gluten-free setting. Feature 'set_timer' is required to set a 3-hour delay. Finally, 'start_or_cancel' is needed to start the appliance."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_gluten_free_mode", "variable_timer_setting", "variable_start_running"]

goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Whole Wheat")
# "set_crust_color", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Dark")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "set_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "set_timer", step 1, variable_timer_setting
goal_state.variable_timer_setting.set_value_ranges_steps([(0, 54000, 600)], 10800) # Adjusting range and step to match 10800 seconds (3 hours, 10 minutes per step)
# "start_or_cancel", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")