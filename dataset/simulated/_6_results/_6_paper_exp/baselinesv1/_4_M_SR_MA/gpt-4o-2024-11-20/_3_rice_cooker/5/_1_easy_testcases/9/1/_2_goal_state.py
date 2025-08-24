feature_sequence = ["select_cooking_program", "adjust_timer", "start_appliance"]
feature_choice_reason = "Feature 'select_cooking_program' is needed to set the variable_cooking_program to 'quick_cooking_steam'. Feature 'adjust_timer' is required to set the variable_timer to 20 minutes. Feature 'start_appliance' is necessary to turn on the machine and start the cooking process."
changing_variables = ["variable_cooking_program", "variable_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("quick_cooking_steam")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(20) # The number represents minutes.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")