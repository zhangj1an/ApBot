feature_sequence = ["turn_on_off", "program_selection", "water_level_selection", "preset_time", "start_pause", "child_lock"]
feature_choice_reason = "The sequence starts with turning on the appliance. Then, the Baby-care program is selected using the program_selection feature. The water level is set to 37 L using the water_level_selection feature. The preset time is set to 6 hours using the preset_time feature. The appliance is started using the start_pause feature. Finally, the child lock is activated using the child_lock feature."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_preset", "variable_start_running", "variable_child_lock"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "program_selection", step 1, variable_program
goal_state.variable_program.set_current_value("3 Baby-care")
# "water_level_selection", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("37 L")
# "preset_time", step 1, variable_preset
goal_state.variable_preset.set_current_value(6) # each number represents an hour.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("on")