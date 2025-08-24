feature_sequence = ["power_and_start_warming", "select_bottle_type", "select_initial_temperature", "select_volume", "power_and_start_warming"]
feature_choice_reason = "The first 'power_and_start_warming' is needed to turn on the appliance. 'select_bottle_type' is required to set the bottle type to 'Milk bag'. 'select_initial_temperature' is needed to set the initial temperature to 'Room'. 'select_volume' is required to set the volume to '4-6 fl-oz'. The final 'power_and_start_warming' is needed to start the warming process."
changing_variables = ["variable_power_on_off", "variable_bottle_type", "variable_initial_temp", "variable_volume", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_and_start_warming", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_bottle_type", step 1, variable_bottle_type
goal_state.variable_bottle_type.set_current_value("Milk bag")
# "select_initial_temperature", step 1, variable_initial_temp
goal_state.variable_initial_temp.set_current_value("Room")
# "select_volume", step 1, variable_volume
goal_state.variable_volume.set_current_value("4-6 fl-oz")
# "power_and_start_warming", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")