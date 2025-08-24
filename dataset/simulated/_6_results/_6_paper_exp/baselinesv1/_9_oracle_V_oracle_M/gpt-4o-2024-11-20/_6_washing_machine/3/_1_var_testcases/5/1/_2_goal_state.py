feature_sequence = ["turn_on_off", "program_selection", "water_level_selection", "preset_time", "start_pause", "child_lock"]
feature_choice_reason = "The 'turn_on_off' feature is required to turn on the appliance. The 'program_selection' feature is needed to set the Blanket program. The 'water_level_selection' feature is required to set the water level to 29 L. The 'preset_time' feature is needed to set the operation to finish in 5 hours. The 'start_pause' feature is required to start the appliance. Finally, the 'child_lock' feature is needed to activate the child lock."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_preset", "variable_start_running", "variable_child_lock"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "program_selection", step 1, variable_program
goal_state.variable_program.set_current_value("5 Blanket")
# "water_level_selection", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("29 L")
# "preset_time", step 1, variable_preset
goal_state.variable_preset.set_current_value(5) # each number represents an hour.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("on")