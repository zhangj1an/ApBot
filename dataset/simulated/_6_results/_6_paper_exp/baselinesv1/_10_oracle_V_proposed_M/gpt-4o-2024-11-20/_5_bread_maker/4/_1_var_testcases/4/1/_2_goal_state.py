feature_sequence = ["set_auto_menu", "set_crust_color", "set_loaf_size", "set_gluten_free_mode", "set_timer", "start_or_cancel"]
feature_choice_reason = "Feature 'set_auto_menu' is required to select the 'Sweet' menu. Feature 'set_crust_color' is required to set the crust color to 'Rapid'. Feature 'set_loaf_size' is required to set the loaf size to '450g'. Feature 'set_gluten_free_mode' is required to enable the gluten-free setting. Feature 'set_timer' is required to set the delay timer to 1 hour. Feature 'start_or_cancel' is required to start the appliance."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_gluten_free_mode", "variable_timer_setting", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Sweet")
# "set_crust_color", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Rapid")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("450g")
# "set_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "set_timer", step 1, variable_timer_setting
goal_state.variable_timer_setting.set_current_value(600) # The number represents seconds.
# "start_or_cancel", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")