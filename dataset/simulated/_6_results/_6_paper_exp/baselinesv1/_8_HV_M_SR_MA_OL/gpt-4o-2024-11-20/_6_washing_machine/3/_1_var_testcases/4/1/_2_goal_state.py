feature_sequence = ["toggle_power", "select_program", "adjust_water_level", "adjust_preset_timer", "start_operation", "set_child_lock"]
feature_choice_reason = "Firstly, toggle the power to turn on the machine. Then, select the Normal program to set the desired washing mode. Adjust the water level to 32 L as required. Set the preset timer to 3 hours to finish the operation in the specified time. Start the operation to begin the washing process. Finally, activate the child lock for safety."
changing_variables = ["variable_power_on_off", "variable_program_selection", "variable_water_level", "variable_preset_timer", "variable_start_running", "variable_child_lock"]
goal_state = ExtendedSimulator()
# "toggle_power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program_selection
goal_state.variable_program_selection.set_current_value("1 Normal")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("32 L")
# "adjust_preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(3) # each number represents an hour.
# "start_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "set_child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("on")