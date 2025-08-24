feature_sequence = ["cooking", "adjust_cooking_time", "start"]
feature_choice_reason = "Feature 'cooking' is chosen to set the menu to 'Bean'. Feature 'adjust_cooking_time' is added to set the cooking time to 40 minutes. Feature 'start' is required to start the cooking process."
changing_variables = ["variable_menu_index", "variable_cooking_time_hour", "variable_cooking_time_minute", "variable_start_running"]
goal_state = Simulator()
# "cooking", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Bean")
# "adjust_cooking_time", step 2, variable_cooking_time_hour
goal_state.variable_cooking_time_hour.set_current_value(0) # The number represents hours.
# "adjust_cooking_time", step 3, variable_cooking_time_minute
goal_state.variable_cooking_time_minute.set_current_value(40) # The number represents minutes.
# "start", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")