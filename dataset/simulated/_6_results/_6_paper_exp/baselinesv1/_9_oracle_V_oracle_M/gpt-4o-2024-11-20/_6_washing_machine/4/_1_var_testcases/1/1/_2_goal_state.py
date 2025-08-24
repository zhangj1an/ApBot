feature_sequence = ["turn_on_off", "select_program", "set_wash_time", "set_water_level", "set_spin_time", "set_rinse_type", "start_pause"]
feature_choice_reason = "The washing machine must be turned on first. Then, the program is set to Powerful. The wash time, water level, spin time, and rinse type are configured sequentially. Finally, the machine is started to run."
changing_variables = ["variable_power_on_off", "variable_program", "variable_wash_time", "variable_water_level", "variable_spin_time", "variable_rinse_type", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P2. Powerful")
# "set_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(18) # The number represents minutes.
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("59 L")
# "set_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(9) # The number represents minutes.
# "set_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Water-Injection Rinse 2 times")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")