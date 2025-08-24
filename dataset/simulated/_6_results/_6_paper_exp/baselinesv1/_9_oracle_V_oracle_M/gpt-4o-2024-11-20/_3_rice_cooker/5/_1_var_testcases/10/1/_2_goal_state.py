feature_sequence = ["cooking_program_selection", "timer", "start_function"]
feature_choice_reason = "Feature cooking_program_selection is used to set the variable_cooking_program to congee mode. Feature timer is used to set the variable_timer to 1.5 hours. Feature start_function is used to start the machine."
changing_variables = ["variable_cooking_program", "variable_timer", "variable_start_running"]
goal_state = Simulator()
# "cooking_program_selection", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("soup_congee")
# "timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("01:30:00")  # The number represents hours, minutes, and seconds
# "start_function", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")