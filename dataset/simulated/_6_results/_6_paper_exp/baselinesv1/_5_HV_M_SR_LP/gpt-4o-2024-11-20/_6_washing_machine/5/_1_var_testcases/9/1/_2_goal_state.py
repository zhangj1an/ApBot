feature_sequence = ["on_off", "set_program", "set_water_level", "set_rinse_times", "set_spin_speed", "start_pause_operation"]
feature_choice_reason = "Feature 'on_off' is required to turn on the machine. Feature 'set_program' is needed to set the program to 'Wool'. Feature 'set_water_level' is required to set the water level to 'High'. Feature 'set_rinse_times' is needed to set the rinse to '3 Times'. Feature 'set_spin_speed' is required to set the spin speed to 'Medium' (closest valid value to 'Regular'). Finally, 'start_pause_operation' is required to start the washing machine."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_rinse_times", "variable_spin_speed", "variable_start_running"]
goal_state = ExtendedSimulator()
# "on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Wool")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("6")
# "set_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("3 times")
# "set_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Medium")
# "start_pause_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")