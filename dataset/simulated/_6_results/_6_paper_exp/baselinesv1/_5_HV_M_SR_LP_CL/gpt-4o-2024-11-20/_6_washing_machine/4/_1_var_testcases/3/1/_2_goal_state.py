feature_sequence = ["power_on_off", "adjust_program", "adjust_wash_time", "adjust_water_level", "adjust_spin_time", "adjust_rinse_type", "start_pause"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the washing machine. Feature 'adjust_program' is needed to select the Fragrance program. Feature 'adjust_wash_time' is required to set the washing time to 15 minutes. Feature 'adjust_water_level' is needed to set the water level to the lowest (25 L). Feature 'adjust_spin_time' is required to set the spin time to 3 minutes. Feature 'adjust_rinse_type' is needed to set the rinse type to 'Water-Injection Rinse 1 time'. Finally, feature 'start_pause' is required to start the washing machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_washing_time", "variable_water_level", "variable_spin_time", "variable_rinse_type", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_program", step 1, variable_program
goal_state.variable_program.set_current_value("P4 (Fragrance)")
# "adjust_wash_time", step 1, variable_washing_time
goal_state.variable_washing_time.set_current_value(15) # each number represents minutes.
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value(25) # each number represents liters.
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(3) # each number represents minutes.
# "adjust_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Water-Injection Rinse 1 time")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")