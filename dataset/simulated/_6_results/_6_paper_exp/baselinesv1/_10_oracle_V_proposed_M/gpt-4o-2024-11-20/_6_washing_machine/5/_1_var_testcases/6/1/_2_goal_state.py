feature_sequence = ["power_control", "set_program", "adjust_water_level", "adjust_time_manager", "adjust_rinse_times", "adjust_spin_speed", "start_pause"]
feature_choice_reason = "Feature 'power_control' is required to turn on the washing machine. Feature 'set_program' is needed to set the program to 'Bedding'. Feature 'adjust_water_level' is required to set the water level to 'High'. Feature 'adjust_time_manager' is needed to allocate 40 minutes. Feature 'adjust_rinse_times' is required to set rinse to '3 Times'. Feature 'adjust_spin_speed' is required to set spin to 'Short'. Finally, 'start_pause' is required to start the washing machine."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse_times", "variable_spin_speed", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Bedding")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("6")  # Assuming "High" corresponds to the highest value in the range
# "adjust_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value("4")  # Assuming "40 minutes" corresponds to "4" in the range
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("3 times")
# "adjust_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Low")  # Assuming "Short" corresponds to "Low" in the range
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")