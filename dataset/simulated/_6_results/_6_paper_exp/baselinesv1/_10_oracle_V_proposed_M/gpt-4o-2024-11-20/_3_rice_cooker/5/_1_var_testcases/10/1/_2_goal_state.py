feature_sequence = ["select_cooking_program", "adjust_timer", "start_running"]
feature_choice_reason = "Feature 'select_cooking_program' is used to set the variable_cooking_program to 'soup_congee'. Feature 'adjust_timer' is used to set the variable_timer to 90 minutes. Feature 'start_running' is used to turn on the appliance and start the cooking process."
changing_variables = ["variable_cooking_program", "variable_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("soup_congee")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(90)  # The number represents minutes.
# "start_running", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")