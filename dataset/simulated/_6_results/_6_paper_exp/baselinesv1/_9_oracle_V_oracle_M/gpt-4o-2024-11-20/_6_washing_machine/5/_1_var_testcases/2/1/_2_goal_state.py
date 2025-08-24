feature_sequence = ["turn_on_off", "set_program", "set_water_level", "set_time_manager", "set_rinse", "set_spin", "start_pause"]
feature_choice_reason = "The washer needs to be powered on first. Then, the 'Delicates' program is selected. Next, the water level is set to 'Mid'. The time manager is adjusted to 30 minutes. The rinse is set to '3 Times', and the spin is maintained at 'Short'. Finally, the washer is started to run."
changing_variables = ["variable_on_off", "variable_program", "variable_water_level", "variable_time_manager", "variable_rinse", "variable_spin", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Delicates")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("Mid")
# "set_time_manager", step 1, variable_time_manager
goal_state.variable_time_manager.set_current_value(30) # The number represents minutes.
# "set_rinse", step 1, variable_rinse
goal_state.variable_rinse.set_current_value("3 Times")
# "set_spin", step 1, variable_spin
goal_state.variable_spin.set_current_value("Short")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")