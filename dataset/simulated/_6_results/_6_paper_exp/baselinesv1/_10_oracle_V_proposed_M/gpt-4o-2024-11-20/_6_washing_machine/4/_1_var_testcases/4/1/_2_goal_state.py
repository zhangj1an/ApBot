feature_sequence = ["power_control", "select_program", "adjust_washing_time", "adjust_water_level", "adjust_spin_time", "adjust_rinse_type", "start_pause_control"]
feature_choice_reason = "Feature 'power_control' is required to turn on the washing machine. Feature 'select_program' is needed to set the program to 'P5 (Soak)'. Feature 'adjust_washing_time' is required to set the washing time to 18 minutes. Feature 'adjust_water_level' is needed to set the water level to 30 L. Feature 'adjust_spin_time' is required to set the spin time to 3 minutes. Feature 'adjust_rinse_type' is needed to set the rinse type to 'Normal Rinse 2 times'. Finally, feature 'start_pause_control' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_washing_time", "variable_water_level", "variable_spin_time", "variable_rinse_type", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P5 (Soak)")
# "adjust_washing_time", step 1, variable_washing_time
goal_state.variable_washing_time.set_current_value(18) # each number represents minutes.
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value(30) # each number represents liters.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(3) # each number represents minutes.
# "adjust_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Normal Rinse 2 times")
# "start_pause_control", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")