feature_sequence = ["power_control", "select_program", "adjust_delay_timer", "adjust_water_level", "adjust_washing_time", "adjust_rinse_type", "start_pause_control"]
feature_choice_reason = "Feature 'power_control' is required to turn on the washing machine. Feature 'select_program' is needed to set the machine to Fuzzy. Feature 'adjust_delay_timer' is required to set the delay start to 5 hours. Feature 'adjust_water_level' is needed to set the water level to 40 L. Feature 'adjust_washing_time' is required to set the wash time to 15 minutes. Feature 'adjust_rinse_type' is needed to set the rinse type to 'Water-Injection Rinse 1 time'. Finally, feature 'start_pause_control' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_delay_timer", "variable_water_level", "variable_washing_time", "variable_rinse_type", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P1 (Fuzzy)")
# "adjust_delay_timer", step 1, variable_delay_timer
goal_state.variable_delay_timer.set_current_value(5) # The number represents hours.
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value(40) # The number represents liters.
# "adjust_washing_time", step 1, variable_washing_time
goal_state.variable_washing_time.set_current_value(15) # The number represents minutes.
# "adjust_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Water-Injection Rinse 1 time")
# "start_pause_control", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")