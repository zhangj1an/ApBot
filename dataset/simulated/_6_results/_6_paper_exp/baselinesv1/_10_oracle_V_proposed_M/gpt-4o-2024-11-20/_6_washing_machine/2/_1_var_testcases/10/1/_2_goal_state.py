feature_sequence = ["turn_power_on_off", "set_program", "set_load_size", "adjust_wash_time", "adjust_rinse_times", "adjust_spin_time", "start_pause_operation"]
feature_choice_reason = "Feature 'turn_power_on_off' is required to turn on the washer. Feature 'set_program' is needed to set the program to 'Soak'. Feature 'set_load_size' is required to set the load size to medium. Feature 'adjust_wash_time' is needed to set the wash time to 14 minutes. Feature 'adjust_rinse_times' is required to set the rinse times to twice. Feature 'adjust_spin_time' is needed to set the spin time to 5 minutes. Finally, feature 'start_pause_operation' is required to start the washer."
changing_variables = ["variable_power_on_off", "variable_program", "variable_load_size", "variable_wash_time", "variable_rinse_times", "variable_spin_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "turn_power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Soak")
# "set_load_size", step 1, variable_load_size
goal_state.variable_load_size.set_current_value("2---medium")
# "adjust_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(14) # each number represents minutes.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value(2) # each number represents times.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(5) # each number represents minutes.
# "start_pause_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")