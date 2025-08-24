feature_sequence = ["activate_gluten_free_mode", "set_auto_menu", "adjust_timer", "adjust_loaf_size", "adjust_crust_color", "start_or_cancel_program"]
feature_choice_reason = "Feature 'activate_gluten_free_mode' is required to enable gluten-free mode. Feature 'set_auto_menu' is needed to select the Sweet menu. Feature 'adjust_timer' is necessary to set a 3-hour delay. Feature 'adjust_loaf_size' is required to set the loaf size to 900g. Feature 'adjust_crust_color' is needed to set the crust color to Medium. Finally, 'start_or_cancel_program' is required to start the appliance."
changing_variables = ["variable_gluten_free_mode", "variable_menu_index", "variable_menu_setting", "variable_timer", "variable_loaf_size", "variable_crust_color", "variable_start_running"]
goal_state = ExtendedSimulator()
# "activate_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Sweet")
# "set_auto_menu", step 1, variable_menu_setting
goal_state.variable_menu_setting = goal_state.menu_setting_dict["Sweet"]
goal_state.variable_menu_setting.set_current_value("03:27:00") # each number represents seconds.
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("03:00:00") # each number represents seconds.
# "adjust_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "adjust_crust_color", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("Medium")
# "start_or_cancel_program", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")