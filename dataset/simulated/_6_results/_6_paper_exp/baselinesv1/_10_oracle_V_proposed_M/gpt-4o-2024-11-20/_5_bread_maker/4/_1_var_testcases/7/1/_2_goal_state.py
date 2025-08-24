feature_sequence = ["set_auto_menu", "set_crust_color", "set_loaf_size", "set_timer", "set_gluten_free_mode", "start_or_cancel"]
feature_choice_reason = "Feature 'set_auto_menu' is required to set the menu to 'Basic'. Feature 'set_crust_color' is required to set the crust color to 'Rapid'. Feature 'set_loaf_size' is required to set the loaf size to '680g'. Feature 'set_timer' is required to set a 3-hour delay. Feature 'set_gluten_free_mode' is required to enable gluten-free mode. Feature 'start_or_cancel' is required to start the appliance."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_timer_setting", "variable_gluten_free_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_auto_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Basic")
# "set_crust_color", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Rapid")
# "set_loaf_size", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("680g")
# "set_timer", step 1, variable_timer_setting
goal_state.variable_timer_setting.set_current_value(600) # 600 seconds represent 10 minutes.
goal_state.variable_timer_setting.next() # Increment to 20 minutes.
goal_state.variable_timer_setting.next() # Increment to 30 minutes.
goal_state.variable_timer_setting.next() # Increment to 40 minutes.
goal_state.variable_timer_setting.next() # Increment to 50 minutes.
goal_state.variable_timer_setting.next() # Increment to 60 minutes.
goal_state.variable_timer_setting.next() # Increment to 70 minutes.
goal_state.variable_timer_setting.next() # Increment to 80 minutes.
goal_state.variable_timer_setting.next() # Increment to 90 minutes.
goal_state.variable_timer_setting.next() # Increment to 100 minutes.
goal_state.variable_timer_setting.next() # Increment to 110 minutes.
goal_state.variable_timer_setting.next() # Increment to 120 minutes.
goal_state.variable_timer_setting.next() # Increment to 130 minutes.
goal_state.variable_timer_setting.next() # Increment to 140 minutes.
goal_state.variable_timer_setting.next() # Increment to 150 minutes.
goal_state.variable_timer_setting.next() # Increment to 160 minutes.
goal_state.variable_timer_setting.next() # Increment to 170 minutes.
goal_state.variable_timer_setting.next() # Increment to 180 minutes (3 hours).
# "set_gluten_free_mode", step 1, variable_gluten_free_mode
goal_state.variable_gluten_free_mode.set_current_value("on")
# "start_or_cancel", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")