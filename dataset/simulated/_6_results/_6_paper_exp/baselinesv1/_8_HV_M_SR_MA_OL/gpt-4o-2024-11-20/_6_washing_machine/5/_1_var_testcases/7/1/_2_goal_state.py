feature_sequence = ["on_off", "set_program", "set_water_level", "set_rinse_times", "set_spin_speed"]
feature_choice_reason = "The 'on_off' feature is required to turn on the washing machine. The 'set_program' feature is needed to select the 'Quick Wash' program. The 'set_water_level' feature is required to set the water level to 'Low' (assumed as level 2). The 'set_rinse_times' feature is needed to set the rinse cycle to '2 Times.' The 'set_spin_speed' feature is required to set the spin speed to 'Regular' (assumed as 'Medium')."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_rinse_times", "variable_spin_speed"]
goal_state = ExtendedSimulator()
# "on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Quick Wash")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("2")
# "set_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value("2 times")
# "set_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("Medium")