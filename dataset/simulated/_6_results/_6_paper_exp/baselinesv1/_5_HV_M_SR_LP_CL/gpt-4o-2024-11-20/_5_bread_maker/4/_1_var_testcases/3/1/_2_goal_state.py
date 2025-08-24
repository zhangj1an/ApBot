feature_sequence = ["set_auto_menu", "adjust_crust_color", "adjust_loaf_size", "activate_gluten_free_mode", "adjust_timer", "start_or_cancel_program"]
feature_choice_reason = "Feature 'set_auto_menu' is used to set the menu to 'Whole Wheat'. Feature 'adjust_crust_color' is used to set the crust color to 'Dark'. Feature 'adjust_loaf_size' is used to set the loaf size to '900g'. Feature 'activate_gluten_free_mode' is used to turn on the gluten-free mode. Feature 'adjust_timer' is used to set a 3-hour delay. Feature 'start_or_cancel_program' is used to start the appliance."
changing_variables = ["variable_menu_index", "variable_crust_color", "variable_loaf_size", "variable_gluten_free_mode", "variable_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Whole Wheat")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Dark")
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "activate_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("03:00:00")  # The number represents hours, minutes, and seconds.
# "start_or_cancel_program", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")