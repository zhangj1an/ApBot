feature_sequence = ["cooking_program_selection", "timer", "start_function"]
feature_choice_reason = "Feature 'cooking_program_selection' is used to set the cooking mode to 'slow_cook_stew'. Feature 'timer' is required to set the cooking time to 3 hours. Feature 'start_function' is necessary to start the machine after all configurations are set."
changing_variables = ["variable_cooking_program", "variable_timer", "variable_start_running"]
goal_state = Simulator()
# "cooking_program_selection", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("slow_cook_stew")
# "timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("03:00:00")  # The number represents hours.
# "start_function", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")