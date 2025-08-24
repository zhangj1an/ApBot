feature_sequence = ["turn_power_on_off", "set_program", "set_load_size", "adjust_wash_time", "adjust_rinse_times", "adjust_spin_time", "start_pause_operation"]
feature_choice_reason = "The sequence starts with turning on the washing machine. Then, the 'set_program' feature is used to select the 'Soak' program. The 'set_load_size' feature is used to set the load size to medium. The 'adjust_wash_time' feature is used to set the wash time to 20 minutes. The 'adjust_rinse_times' feature is used to set the rinse times to 3. The 'adjust_spin_time' feature is used to set the spin time to 9 minutes. Finally, the 'start_pause_operation' feature is used to begin the washing process."
changing_variables = ["variable_power_on_off", "variable_program", "variable_load_size", "variable_wash_time", "variable_rinse_times", "variable_spin_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "turn_power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_program", step 1, variable_program
goal_state.variable_program.set_current_value("Soak")
# "set_load_size", step 1, variable_load_size
goal_state.variable_load_size.set_current_value("2---medium")
# "adjust_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(20) # each number represents minutes.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value(3) # each number represents times.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(9) # each number represents minutes.
# "start_pause_operation", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")