feature_sequence = ["on_off", "set_program", "set_water_level", "set_time_manager", "set_rinse_times", "set_spin_speed"]
feature_choice_reason = "The washer must be turned on first using the 'on_off' feature. The 'set_program' feature is required to select the 'Mixed' program. The 'set_water_level' feature is needed to set the water level to 'Low'. The 'set_time_manager' feature is used to adjust the time manager to the closest applicable value for 35 minutes. The 'set_rinse_times' feature is required to set rinse to '2 Times'. Finally, the 'set_spin_speed' feature is needed to set the spin speed to 'Low'."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse_times", "variable_spin_speed"]
goal_state = ExtendedSimulator()
# "on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Mixed")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("2")
# "set_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value("3")
# "set_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("2 times")
# "set_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Low")