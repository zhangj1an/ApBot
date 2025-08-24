feature_sequence = ["on_off", "set_program", "set_water_level", "set_time_manager", "set_rinse_times", "set_spin_speed"]
feature_choice_reason = "Feature 'on_off' is required to power up the washer. Feature 'set_program' is needed to select 'Delicates' mode. Feature 'set_water_level' is required to set the water level to 'Mid'. Feature 'set_time_manager' is necessary to adjust the time manager to 30 minutes. Feature 'set_rinse_times' is needed to select '3 Times' rinse. Feature 'set_spin_speed' is required to maintain a 'Short' spin."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse_times", "variable_spin_speed"]
goal_state = ExtendedSimulator()
# "on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Delicates")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("3")
# "set_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value("3")
# "set_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("3 times")
# "set_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Low")