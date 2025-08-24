feature_sequence = ["power_on_off", "adjust_program", "delay_timer", "adjust_water_level", "adjust_wash_time", "adjust_rinse_type", "start_pause"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the washing machine. Feature 'adjust_program' is needed to set the machine to Fuzzy. Feature 'delay_timer' is required to set the delay start by 5 hours. Feature 'adjust_water_level' is needed to set the water level to 40 L. Feature 'adjust_wash_time' is required to set the washing time to 15 minutes. Feature 'adjust_rinse_type' is needed to set the rinse type to 'Water-Injection Rinse 1 time'. Finally, feature 'start_pause' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_delay_timer", "variable_water_level", "variable_washing_time", "variable_rinse_type", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_program", step 1, variable_program
goal_state.variable_program.set_current_value("P1 (Fuzzy)")
# "delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(5) # each number represents an hour.
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value(40) # each number represents liters.
# "adjust_wash_time", step 1, variable_washing_time
goal_state.variable_washing_time.set_current_value(15) # each number represents minutes.
# "adjust_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Water-Injection Rinse 1 time")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")