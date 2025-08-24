feature_sequence = ["select_cooking_program", "adjust_timer", "start_appliance"]
feature_choice_reason = "Feature 'select_cooking_program' is used to set the rice cooker to cook congee. However, the timer needs to be adjusted, which cannot be done in this feature. Therefore, 'adjust_timer' is added to set the timer to 2 hours. Finally, 'start_appliance' is included to turn on the machine and start cooking."
changing_variables = ["variable_cooking_program", "variable_timer", "variable_start_running"]
goal_state = ExtendedSimulator()
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("soup_congee")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(120)  # The number represents minutes.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")