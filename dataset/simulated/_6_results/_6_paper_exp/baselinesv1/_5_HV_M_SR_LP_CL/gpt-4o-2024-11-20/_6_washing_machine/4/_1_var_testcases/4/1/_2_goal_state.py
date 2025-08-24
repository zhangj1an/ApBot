feature_sequence = ["power_on_off", "adjust_program", "adjust_wash_time", "adjust_water_level", "adjust_spin_time", "adjust_rinse_type", "start_pause"]
feature_choice_reason = "The sequence starts with turning on the washing machine (power_on_off). Then, the program is set to Soak mode (adjust_program). Washing time is adjusted to 18 minutes (adjust_wash_time), followed by setting the water level to 30 L (adjust_water_level). Spin time is set to 3 minutes (adjust_spin_time), and rinse type is set to 'Normal Rinse 2 times' (adjust_rinse_type). Finally, the machine is started (start_pause)."
changing_variables = ["variable_power_on_off", "variable_program", "variable_washing_time", "variable_water_level", "variable_spin_time", "variable_rinse_type", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_program", step 1, variable_program
goal_state.variable_program.set_current_value("P5 (Soak)")
# "adjust_wash_time", step 1, variable_washing_time
goal_state.variable_washing_time.set_current_value(18) # each number represents minutes.
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value(30) # each number represents liters.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(3) # each number represents minutes.
# "adjust_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Normal Rinse 2 times")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")