feature_sequence = ["turn_on_off", "program_selection", "water_level_selection", "preset_time", "start_pause", "child_lock"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'program_selection' is needed to set the program to 'Normal'. Feature 'water_level_selection' is required to set the water level to '20 L'. Feature 'preset_time' is needed to set the finish time to 9 hours. Feature 'start_pause' is required to start the appliance. Feature 'child_lock' is needed to activate the child lock."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_preset", "variable_start_running", "variable_child_lock"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "program_selection", step 1, variable_program
goal_state.variable_program.set_current_value("1 Normal")
# "water_level_selection", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("20 L")
# "preset_time", step 1, variable_preset
goal_state.variable_preset.set_current_value(9) # each number represents an hour.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("on")