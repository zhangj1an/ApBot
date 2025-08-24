feature_sequence = ["power_on_off", "select_program", "adjust_load_size", "adjust_wash_time", "adjust_rinse_times", "adjust_spin_time", "start_pause_cycle"]
feature_choice_reason = "The sequence starts with turning on the washer (power_on_off). Then, the washing program is selected (select_program). The load size is adjusted (adjust_load_size). Next, the wash time is set (adjust_wash_time), followed by setting the rinse times (adjust_rinse_times) and spin time (adjust_spin_time). Finally, the washing cycle is started (start_pause_cycle). Each feature is necessary to achieve the goal and does not duplicate functionality."
changing_variables = ["variable_power_on_off", "variable_program", "variable_load_size", "variable_wash_time", "variable_rinse_times", "variable_spin_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("Heavy")
# "adjust_load_size", step 1, variable_load_size
goal_state.variable_load_size.set_current_value("1---small")
# "adjust_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(5) # each number represents minutes.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value(1) # each number represents times.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(8) # each number represents minutes.
# "start_pause_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")