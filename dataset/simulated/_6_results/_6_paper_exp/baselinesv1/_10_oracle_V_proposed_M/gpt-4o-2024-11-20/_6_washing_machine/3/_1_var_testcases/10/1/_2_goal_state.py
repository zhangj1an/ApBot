feature_sequence = ["power", "select_program", "adjust_water_level", "set_preset_timer", "start_operation", "child_lock"]
feature_choice_reason = "Feature 'power' is required to turn on the appliance. Feature 'select_program' is needed to set the Normal program. Feature 'adjust_water_level' is required to select a water level of 20 L. Feature 'set_preset_timer' is needed to set the timer to 9 hours. Feature 'start_operation' is required to start the appliance. Feature 'child_lock' is needed to activate the child lock."
changing_variables = ["variable_power_on_off", "variable_program_selection", "variable_water_level", "variable_preset_timer", "variable_start_running", "variable_child_lock"]
goal_state = ExtendedSimulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program_selection
goal_state.variable_program_selection.set_current_value("1 Normal")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("20 L")
# "set_preset_timer", step 1, variable_preset_timer
goal_state.variable_preset_timer.set_current_value(9) # each number represents an hour.
# "start_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("on")