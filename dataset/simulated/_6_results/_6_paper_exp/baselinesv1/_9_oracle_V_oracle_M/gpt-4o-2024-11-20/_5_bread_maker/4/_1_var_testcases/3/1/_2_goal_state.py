feature_sequence = ["menu_selection", "crust_colour_selection", "loaf_size_selection", "gluten_free_selection", "timer_adjustment", "start_cancel_function"]
feature_choice_reason = "The menu_selection feature is required to set the menu to Whole Wheat. The crust_colour_selection feature is needed to set the crust color to Dark. The loaf_size_selection feature is necessary to set the loaf size to 900g. The gluten_free_selection feature is required to turn on the gluten-free setting. The timer_adjustment feature is needed to set a 3-hour delay. Finally, the start_cancel_function feature is required to start the appliance."
changing_variables = ["variable_menu_index", "variable_crust_colour", "variable_loaf_size", "variable_gluten_free", "variable_timer", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("3 Whole Wheat")
# "crust_colour_selection", step 1, variable_crust_colour
goal_state.variable_crust_colour.set_current_value("Dark")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("900g")
# "gluten_free_selection", step 1, variable_gluten_free
goal_state.variable_gluten_free.set_current_value("on")
# "timer_adjustment", step 1, variable_timer
goal_state.variable_timer.set_current_value(3) # each number represents an hour.
# "start_cancel_function", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")