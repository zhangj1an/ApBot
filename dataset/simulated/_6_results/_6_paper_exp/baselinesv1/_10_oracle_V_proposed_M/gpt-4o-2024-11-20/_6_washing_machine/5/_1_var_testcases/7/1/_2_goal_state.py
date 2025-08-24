feature_sequence = ["power_control", "set_program", "adjust_water_level", "adjust_time_manager", "adjust_rinse_times", "adjust_spin_speed"]
feature_choice_reason = "Feature 'power_control' is required to turn on the machine. Feature 'set_program' is needed to select 'Quick Wash'. Feature 'adjust_water_level' is required to set the water level to 'Low'. Feature 'adjust_time_manager' is needed to set the washing time to 15 minutes. Feature 'adjust_rinse_times' is required to set rinse to '2 Times'. Feature 'adjust_spin_speed' is needed to set spinning speed to 'Regular'."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse_times", "variable_spin_speed"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Quick Wash")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("2")
# "adjust_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value("3")
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("2 times")
# "adjust_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Medium")