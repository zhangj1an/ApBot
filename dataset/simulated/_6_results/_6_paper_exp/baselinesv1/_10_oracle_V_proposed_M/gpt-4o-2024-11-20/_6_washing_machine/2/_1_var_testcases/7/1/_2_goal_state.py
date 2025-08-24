feature_sequence = ["turn_power_on_off", "set_program", "set_load_size", "adjust_wash_time", "adjust_rinse_times", "adjust_spin_time", "start_pause_operation"]
feature_choice_reason = "Feature 'turn_power_on_off' is required to turn on the machine. Feature 'set_program' is needed to set the washing program to 'Gentle'. Feature 'set_load_size' is required to set the load size to 'Large'. Feature 'adjust_wash_time' is needed to set the wash time to 18 minutes. Feature 'adjust_rinse_times' is required to set the rinse times to 3. Feature 'adjust_spin_time' is needed to set the spin time to 7 minutes. Finally, feature 'start_pause_operation' is required to start the washing cycle."
changing_variables = ["variable_power_on_off", "variable_program", "variable_load_size", "variable_wash_time", "variable_rinse_times", "variable_spin_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "turn_power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Gentle")
# "set_load_size", step 1, variable_load_size
goal_state.variable_load_size.set_current_value("3---large")
# "adjust_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(18) # The number represents minutes.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value(3) # The number represents times.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(7) # The number represents minutes.
# "start_pause_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")