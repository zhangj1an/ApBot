feature_sequence = ["menu_selection", "loaf_size_selection", "crust_color_selection", "timer_delay", "start_stop"]
feature_choice_reason = "Feature 'menu_selection' is used to set the menu to '3 Wholewheat'. Feature 'loaf_size_selection' is used to set the loaf size to 'small'. Feature 'crust_color_selection' is used to set the crust color to 'dark'. Feature 'timer_delay' is used to set the timer delay to 2 hours. Finally, feature 'start_stop' is used to start the bread maker."
changing_variables = ["variable_menu_index", "variable_loaf_size", "variable_crust_color", "variable_timer_delay", "variable_start_running"]
goal_state = Simulator()
# "menu_selection", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("3 Wholewheat")
# "loaf_size_selection", step 1, variable_loaf_size
goal_state.variable_loaf_size.set_current_value("small")
# "crust_color_selection", step 1, variable_crust_color
goal_state.variable_crust_color.set_current_value("dark")
# "timer_delay", step 1, variable_timer_delay
goal_state.variable_timer_delay.set_current_value(2) # each number represents an hour.
# "start_stop", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")