feature_sequence = ["turn_on_off", "select_program", "set_delay_time", "set_water_level", "set_wash_time", "set_rinse_type", "start_pause"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the machine. Feature 'select_program' is needed to set the program to Fuzzy. Feature 'set_delay_time' is required to set the delay start time. Feature 'set_water_level' is needed to set the water level. Feature 'set_wash_time' is required to set the wash time. Feature 'set_rinse_type' is required to set the rinse type. Finally, feature 'start_pause' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_delay_time", "variable_water_level", "variable_wash_time", "variable_rinse_type", "variable_start_running"]

goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P1. Fuzzy")
# "set_delay_time", step 1, variable_delay_time
goal_state.variable_delay_time.set_current_value(5) # The number represents hours.
# "set_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value("40 L")
# "set_wash_time", step 1, variable_wash_time
goal_state.variable_wash_time.set_current_value(15) # The number represents minutes.
# "set_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Water-Injection Rinse 1 time")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")