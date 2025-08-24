feature_sequence = ["power_on_off", "select_program", "adjust_load_size", "adjust_wash_time", "adjust_rinse_times", "adjust_spin_time", "start_pause_cycle"]
feature_choice_reason = "The washer must be powered on first using 'power_on_off'. The 'select_program' feature is needed to set the program to 'Rapid'. The 'adjust_load_size' feature is required to set the load size to large. The 'adjust_wash_time' feature is used to set the wash time to 8 minutes. The 'adjust_rinse_times' feature is necessary to set the rinse times to 2. The 'adjust_spin_time' feature is needed to set the spin time to 3 minutes. Finally, the 'start_pause_cycle' feature is required to start the washing cycle."
changing_variables = ["variable_power_on_off", "variable_program", "variable_load_size", "variable_wash_time", "variable_rinse_times", "variable_spin_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("Rapid")
# "adjust_load_size", step 1, variable_load_size
goal_state.variable_load_size.set_current_value("3---large")
# "adjust_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(8) # each number represents minutes.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value(2) # each number represents times.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(3) # each number represents minutes.
# "start_pause_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")