feature_sequence = ["power_control", "set_program", "adjust_water_level", "adjust_time_manager", "adjust_rinse_times", "adjust_spin_speed", "start_pause"]
feature_choice_reason = "The washing machine must be turned on first using 'power_control'. Then, the 'set_program' feature is used to set the program to 'Regular'. The 'adjust_water_level' feature is used to set the water level to 'High'. The 'adjust_time_manager' feature is used to allocate 45 minutes. The 'adjust_rinse_times' feature is used to set rinse times to '2 Times'. The 'adjust_spin_speed' feature is used to set the spin speed to 'Regular'. Finally, the 'start_pause' feature is used to start the washing machine."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse_times", "variable_spin_speed", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Regular")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("6")
# "adjust_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value("3") # Assuming each step represents 15 minutes, 3 steps = 45 minutes.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("2 times")
# "adjust_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Medium") # Assuming "Regular" corresponds to "Medium" in the spin speed options.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")