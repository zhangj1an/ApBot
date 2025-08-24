feature_sequence = ["start_appliance", "select_cooking_program", "adjust_timer"]
feature_choice_reason = "Feature 'start_appliance' is required to turn on the machine. Feature 'select_cooking_program' is needed to set the cooking program to congee mode. Feature 'adjust_timer' is required to set the timer to 1.5 hours."
changing_variables = ["variable_start_running", "variable_cooking_program", "variable_timer"]
goal_state = ExtendedSimulator()
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("soup_congee")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(90)  # The number represents minutes.