feature_sequence = ["turn_on_off", "select_program", "set_water_level", "set_rinse_type", "set_wash_time", "start_pause"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the machine. Feature 'select_program' is needed to choose the Tub Clean program. Feature 'set_water_level' is required to set the water level to maximum. Feature 'set_rinse_type' is needed to set the rinse setting to 'Normal Rinse 1 time'. Feature 'set_wash_time' is required to set the wash time to 3 minutes. Finally, feature 'start_pause' is needed to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_rinse_type", "variable_wash_time", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P6. Tub Clean")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("59 L")
# "set_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Normal Rinse 1 time")
# "set_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(3) # each number represents minutes.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")