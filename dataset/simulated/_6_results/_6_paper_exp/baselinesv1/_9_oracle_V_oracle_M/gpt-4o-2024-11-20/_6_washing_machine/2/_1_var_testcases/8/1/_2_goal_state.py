feature_sequence = ["turn_on_off", "select_washing_program", "set_load_size", "set_wash_time", "set_rinse_times", "set_spin_time", "start_pause_cycle"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the washer. Feature 'select_washing_program' is needed to set the washing program to 'Normal'. Feature 'set_load_size' is required to set the load size to medium. Feature 'set_wash_time' is required to set the wash time to 11 minutes. Feature 'set_rinse_times' is required to set the rinse times to 2. Feature 'set_spin_time' is required to set the spin time to 3 minutes. Finally, 'start_pause_cycle' is required to start the washing cycle."
changing_variables = ["variable_on_off", "variable_washing_program", "variable_load_size", "variable_wash_time", "variable_rinse_times", "variable_spin_time", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "select_washing_program", step 1, variable_washing_program
goal_state.variable_washing_program.set_current_value("Normal")
# "set_load_size", step 1, variable_load_size
goal_state.variable_load_size.set_current_value("2")
# "set_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(11) # each number represents minutes.
# "set_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value(2) # each number represents times.
# "set_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(3) # each number represents minutes.
# "start_pause_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")