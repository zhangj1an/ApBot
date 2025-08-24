feature_sequence = ["set_auto_menu", "adjust_loaf_size", "adjust_crust_color", "adjust_timer", "activate_gluten_free_mode", "start_or_cancel_program"]
feature_choice_reason = "Feature 'set_auto_menu' is required to set the menu to 'Sweet'. Feature 'adjust_loaf_size' is needed to set the loaf size to '900g'. Feature 'adjust_crust_color' is necessary to set the crust color to 'Light'. Feature 'adjust_timer' is required to set a 3-hour delay. Feature 'activate_gluten_free_mode' is needed to enable the gluten-free setting. Finally, 'start_or_cancel_program' is required to start the appliance."
changing_variables = ["variable_menu_index", "variable_menu_setting", "variable_loaf_size", "variable_crust_color", "variable_timer", "variable_gluten_free_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Sweet")
# "set_auto_menu", step 1, variable_menu_setting
goal_state.variable_menu_setting = goal_state.menu_setting_dict["Sweet"]
goal_state.variable_menu_setting.set_current_value("03:27:00") # each number represents seconds.
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Light")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("03:00:00") # each number represents seconds.
# "activate_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "start_or_cancel_program", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")