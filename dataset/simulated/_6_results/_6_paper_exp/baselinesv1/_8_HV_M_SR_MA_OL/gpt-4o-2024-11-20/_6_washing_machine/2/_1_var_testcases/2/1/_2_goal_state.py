feature_sequence = ["power_on_off", "select_program", "adjust_load_size", "adjust_wash_time", "adjust_rinse_times", "adjust_spin_time", "start_pause_cycle"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'select_program' is needed to set the washing program to 'Gentle'. Feature 'adjust_load_size' is required to set the load size to 'medium'. Feature 'adjust_wash_time' is needed to set the wash time to 10 minutes. Feature 'adjust_rinse_times' is required to set the rinse times to 1. Feature 'adjust_spin_time' is needed to set the spin time to 4 minutes. Finally, 'start_pause_cycle' is required to start the washing cycle."
changing_variables = ["variable_power_on_off", "variable_program", "variable_load_size", "variable_wash_time", "variable_rinse_times", "variable_spin_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("Gentle")
# "adjust_load_size", step 1, variable_load_size
goal_state.variable_load_size.set_current_value("2---medium")
# "adjust_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(10) # each number represents a minute.
# "adjust_rinse_times", step 1, variable_rinse_times
goal_state.variable_rinse_times.set_current_value(1) # each number represents the number of rinse cycles.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(4) # each number represents a minute.
# "start_pause_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")