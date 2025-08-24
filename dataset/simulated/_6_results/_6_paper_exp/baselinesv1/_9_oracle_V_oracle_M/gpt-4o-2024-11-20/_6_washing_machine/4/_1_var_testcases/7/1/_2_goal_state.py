feature_sequence = ["turn_on_off", "select_program", "set_water_level", "set_wash_time", "set_rinse_type", "set_spin_time", "start_pause"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the machine. Feature 'select_program' is needed to set the program to 'Small Load'. Feature 'set_water_level' is required to set the water level to 25 L. Feature 'set_wash_time' is needed to set the wash time to 9 minutes. Feature 'set_rinse_type' is required to set the rinse type to 'Water-Injection Rinse 2 times'. Feature 'set_spin_time' is needed to set the spin duration to 1 minute. Finally, feature 'start_pause' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_wash_time", "variable_rinse_type", "variable_spin_time", "variable_start_running"]

goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P9. Small Load")
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("25 L (Auto)")
# "set_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(9) # The number represents minutes.
# "set_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Water-Injection Rinse 2 times")
# "set_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(1) # The number represents minutes.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")