feature_sequence = ["on_off", "set_program", "set_water_level", "set_time_manager", "set_rinse_times", "set_spin_speed", "start_pause_operation"]
feature_choice_reason = "Feature 'on_off' is required to turn on the appliance. Feature 'set_program' is needed to configure the washer to 'Wool' setting. Feature 'set_water_level' is required to set the water level to 'High'. Feature 'set_time_manager' is needed to set the time manager to 25 minutes. Feature 'set_rinse_times' is required to set the rinse times to '2 Times'. Feature 'set_spin_speed' is required to set the spin speed to 'Regular'. Finally, 'start_pause_operation' is required to start the washer after all configurations are set."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse_times", "variable_spin_speed", "variable_start_running"]
goal_state = ExtendedSimulator()
# "on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Wool")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("5")
# "set_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value("2")
# "set_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("2 times")
# "set_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Medium")
# "start_pause_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")