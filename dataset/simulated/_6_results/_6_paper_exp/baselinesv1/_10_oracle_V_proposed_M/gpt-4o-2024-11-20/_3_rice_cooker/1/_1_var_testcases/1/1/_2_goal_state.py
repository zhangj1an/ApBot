feature_sequence = ["select_menu_option", "set_cooking_time", "start_cooking"]
feature_choice_reason = "Feature 'select_menu_option' is used to set the menu to 'Bean'. Feature 'set_cooking_time' is used to set the cooking time to 40 minutes. Feature 'start_cooking' is used to start the cooking process."
changing_variables = ["variable_menu_index", "variable_cooking_time_hours", "variable_cooking_time_minutes", "variable_start_cooking"]
goal_state = ExtendedSimulator()
# "select_menu_option", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Bean")
# "set_cooking_time", step 2, variable_cooking_time_hours
goal_state.variable_cooking_time_hours.set_current_value(0) # each number represents hours.
# "set_cooking_time", step 3, variable_cooking_time_minutes
goal_state.variable_cooking_time_minutes.set_current_value(40) # each number represents minutes.
# "start_cooking", step 1, variable_start_cooking
goal_state.variable_start_cooking.set_current_value("on")