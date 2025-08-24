feature_sequence = ["menu_selection", "loaf_size_selection", "crust_colour_selection", "timer_adjustment", "gluten_free_selection", "start_cancel_function"]
feature_choice_reason = "Feature 'menu_selection' is required to set the menu to whole wheat. Feature 'loaf_size_selection' is required to set the loaf size to 680g. Feature 'crust_colour_selection' is required to set the crust to medium. Feature 'timer_adjustment' is required to set the timer to 2 hours. Feature 'gluten_free_selection' is required to enable the gluten-free setting. Feature 'start_cancel_function' is required to start the appliance."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_colour", "variable_timer", "variable_gluten_free", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("3 Whole Wheat")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("680g")
# "crust_colour_selection", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Medium")
# "timer_adjustment", step 1, variable_timer
goal_state.variable_timer.set_current_value(2) # The number represents hours.
# "gluten_free_selection", step 1, variable_gluten_free
goal_state.variable_gluten_free.set_current_value("on")
# "start_cancel_function", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")