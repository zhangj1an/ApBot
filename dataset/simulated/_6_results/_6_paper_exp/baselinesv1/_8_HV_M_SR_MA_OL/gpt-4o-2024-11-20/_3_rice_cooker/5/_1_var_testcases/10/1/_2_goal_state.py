feature_sequence = ["start_appliance", "select_cooking_program", "adjust_timer", "start_appliance"]
feature_choice_reason = "The first 'start_appliance' feature is used to turn on the appliance. The 'select_cooking_program' feature is used to set the cooking program to 'soup_congee'. The 'adjust_timer' feature is used to set the timer to 90 minutes. The second 'start_appliance' feature is used to start the machine after all configurations are set."
changing_variables = ["variable_start_running", "variable_cooking_program", "variable_timer"]

goal_state = ExtendedSimulator()
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("soup_congee")
# "adjust_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value(90)  # The number represents minutes.
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")