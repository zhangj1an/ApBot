feature_sequence = ["power_control", "set_program", "adjust_water_level", "adjust_time_manager", "adjust_rinse_times", "adjust_spin_speed", "start_pause"]
feature_choice_reason = "The 'power_control' feature is required to turn on the appliance. The 'set_program' feature is needed to select the 'Mixed' program. The 'adjust_water_level' feature is used to set the water level to 'Low'. The 'adjust_time_manager' feature is required to set the time manager to 35 minutes. The 'adjust_rinse_times' feature is used to set rinse times to '2 Times'. The 'adjust_spin_speed' feature is required to set the spin speed to 'Short'. Finally, the 'start_pause' feature is needed to start the washing cycle."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse_times", "variable_spin_speed", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Mixed")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("1")
# "adjust_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value("2") # each number represents a predefined time duration.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("2 times")
# "adjust_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Low")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")