feature_sequence = ["delay_timer", "menu", "start"]
feature_choice_reason = "Feature 'delay_timer' is used to set the delay timer to 1.5 hours. Feature 'menu' is used to select 'Steel Cut Oats' and adjust the cooking time. Feature 'start' is used to start the appliance."
changing_variables = ["variable_delay_timer", "variable_menu_selection", "variable_cooking_time", "variable_start_running"]
goal_state = Simulator()
# "delay_timer", step 2, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(1.5) # each number represents an hour.
# "menu", step 1, variable_menu_selection
goal_state.variable_menu_selection.set_current_value("Steel Cut Oats")
# "menu", step 2, variable_cooking_time
goal_state.variable_cooking_time.set_current_value(30) # each number represents minutes.
# "start", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")