feature_sequence = ["menu_selection", "loaf_size_selection", "crust_color_selection", "timer_delay", "start_stop"]
feature_choice_reason = "Feature 'menu_selection' is required to set the menu to 'Basic White'. Feature 'loaf_size_selection' is required to set the loaf size to 'large'. Feature 'crust_color_selection' is required to set the crust color to 'medium'. Feature 'timer_delay' is required to set the timer delay to 5 hours. Feature 'start_stop' is required to start the bread maker."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_timer_delay", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("1 Basic White")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("large")
# "crust_color_selection", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("medium")
# "timer_delay", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value(5) # each number represents an hour.
# "start_stop", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")