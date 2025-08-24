feature_sequence = ["delay_timer", "menu", "start"]
feature_choice_reason = "Feature 'delay_timer' is chosen to adjust the delay time to 30 minutes. Feature 'menu' is chosen to set the rice cooker to White Rice mode and adjust the cooking time. Feature 'start' is chosen to start running the rice cooker."
changing_variables = ["variable_delay_timer", "variable_menu_selection", "variable_cooking_time", "variable_start_running"]
goal_state = Simulator()
# "delay_timer", step 2, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(0.5) # each number represents 30 minutes.
# "menu", step 1, variable_menu_selection
goal_state.variable_menu_selection.set_current_value("White Rice")
# "menu", step 2, variable_cooking_time
goal_state.variable_cooking_time.set_current_value(30) # each number represents minutes.
# "start", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")