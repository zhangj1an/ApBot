feature_sequence = ["toggle_power", "select_program", "adjust_water_level", "adjust_preset_timer", "start_operation", "set_child_lock"]
feature_choice_reason = "The sequence starts with toggling the power to turn on the appliance. Then, the Soak program is selected for heavily soiled clothes. The water level is adjusted to 20 L, followed by setting the preset timer to 8 hours. The operation is started, and finally, the child lock is activated to ensure safety."
changing_variables = ["variable_power_on_off", "variable_program_selection", "variable_water_level", "variable_preset_timer", "variable_start_running", "variable_child_lock"]
goal_state = ExtendedSimulator()
# "toggle_power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program_selection
goal_state.variable_program_selection.set_current_value("6 Soak")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("20 L")
# "adjust_preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(8) # each number represents an hour.
# "start_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "set_child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("on")