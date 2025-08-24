feature_sequence = ["power_control", "select_program", "adjust_water_level", "adjust_rinse_type", "adjust_washing_time", "start_pause_control"]
feature_choice_reason = "Feature 'power_control' is required to turn on the machine. Feature 'select_program' is needed to choose the Tub Clean program. Feature 'adjust_water_level' is required to set the water level to the maximum. Feature 'adjust_rinse_type' is needed to set the rinse setting to 'Normal Rinse 1 time'. Feature 'adjust_washing_time' is required to set the washing time to 3 minutes. Finally, feature 'start_pause_control' is required to start the machine running."
changing_variables = ["variable_power_on_off", "variable_program", "variable_water_level", "variable_rinse_type", "variable_washing_time", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_program", step 1, variable_program
goal_state.variable_program.set_current_value("P6 (Tub Clean)")
# "adjust_water_level", step 1, variable_water_level
goal_state.variable_water_level.set_current_value(59) # The number represents liters.
# "adjust_rinse_type", step 1, variable_rinse_type
goal_state.variable_rinse_type.set_current_value("Normal Rinse 1 time")
# "adjust_washing_time", step 1, variable_washing_time
goal_state.variable_washing_time.set_current_value(3) # The number represents minutes.
# "start_pause_control", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("start")