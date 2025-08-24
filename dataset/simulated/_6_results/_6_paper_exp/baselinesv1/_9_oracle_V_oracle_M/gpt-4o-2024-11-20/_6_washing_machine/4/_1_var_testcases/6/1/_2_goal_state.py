feature_sequence = ["turn_on_off", "select_program", "set_water_level", "set_wash_time", "set_spin_time", "set_rinse_type", "start_pause"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the washing machine. Feature 'select_program' is needed to set the program to Energy Save. Feature 'set_water_level' is required to set the water level to 30L. Feature 'set_wash_time' is needed to set the wash time to 9 minutes. Feature 'set_spin_time' is required to set the spin time to 6 minutes. Feature 'set_rinse_type' is needed to set the rinse type to 'Normal Rinse 2 times'. Finally, feature 'start_pause' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_wash_time", "variable_spin_time", "variable_rinse_type", "variable_start_running"]

goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P8. Energy Save")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("30 L")
# "set_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(9) # The number represents minutes.
# "set_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(6) # The number represents minutes.
# "set_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Normal Rinse 2 times")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")