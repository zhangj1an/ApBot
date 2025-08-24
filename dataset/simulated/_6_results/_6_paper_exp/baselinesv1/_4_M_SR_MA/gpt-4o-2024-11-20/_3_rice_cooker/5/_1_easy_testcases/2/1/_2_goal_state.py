feature_sequence = ["select_cooking_program", "adjust_timer", "start_appliance"]
feature_choice_reason = "Feature 'select_cooking_program' is used to set variable_cooking_program to 'slow_cook_stew'. Feature 'adjust_timer' is used to set variable_timer to 180 minutes. Feature 'start_appliance' is used to set variable_start_running to 'on'."
changing_variables = ["variable_cooking_program", "variable_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("slow_cook_stew")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(180)
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")