feature_sequence = ["menu_selection", "crust_colour_selection", "loaf_size_selection", "gluten_free_selection", "timer_adjustment", "start_cancel_function"]
feature_choice_reason = "Feature 'menu_selection' is required to set the menu to 'Basic'. Feature 'crust_colour_selection' is needed to set the crust to 'Rapid'. Feature 'loaf_size_selection' is required to set the loaf size to '680g'. Feature 'gluten_free_selection' is necessary to enable the gluten-free setting. Feature 'timer_adjustment' is required to set the 3-hour delay. Finally, 'start_cancel_function' is needed to start the appliance."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_gluten_free", "variable_timer", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("1 Basic")
# "crust_colour_selection", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Rapid")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("680g")
# "gluten_free_selection", step 1, variable_gluten_free
goal_state.variable_gluten_free.set_current_value("on")
# "timer_adjustment", step 1, variable_timer
goal_state.variable_timer.set_current_value(3) # The number represents hours.
# "start_cancel_function", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")