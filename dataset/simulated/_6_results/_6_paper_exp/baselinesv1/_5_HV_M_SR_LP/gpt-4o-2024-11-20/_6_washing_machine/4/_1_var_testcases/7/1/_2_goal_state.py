feature_sequence = ["power_on_off", "adjust_program", "adjust_water_level", "adjust_wash_time", "adjust_rinse_type", "adjust_spin_time", "start_pause"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the washing machine. Feature 'adjust_program' is needed to select the 'Small Load' program. Feature 'adjust_water_level' is required to set the water limit to 25 L. Feature 'adjust_wash_time' is needed to set the wash cycle to 9 minutes. Feature 'adjust_rinse_type' is required to set the rinse type to 'Water-Injection Rinse 2 times'. Feature 'adjust_spin_time' is needed to set the spin duration to 1 minute. Finally, feature 'start_pause' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_washing_time", "variable_rinse_type", "variable_spin_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_program", step 1, variable_program
goal_state.variable_program.set_current_value("P9 (Small Load)")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value(25) # The number represents liters.
# "adjust_wash_time", step 1, variable_washing_time
goal_state.variable_washing_time.set_current_value(9) # The number represents minutes.
# "adjust_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Water-Injection Rinse 2 times")
# "adjust_spin_time", step 1, variable_spin_time
goal_state.variable_spin_time.set_current_value(1) # The number represents minutes.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")