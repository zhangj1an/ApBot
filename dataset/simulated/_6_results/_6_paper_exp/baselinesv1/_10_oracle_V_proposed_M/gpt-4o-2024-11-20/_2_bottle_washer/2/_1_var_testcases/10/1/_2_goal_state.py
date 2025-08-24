feature_sequence = ["power_toggle_or_start_warming", "adjust_bottle_type", "adjust_initial_temp", "adjust_volume"]
feature_choice_reason = "The first feature is required to turn on the appliance. The second feature adjusts the bottle type to 'Milk bag'. The third feature adjusts the initial temperature to 'Room'. The fourth feature adjusts the volume to '4-6 fl-oz'."
changing_variables = ["variable_power_on_off", "variable_bottle_type", "variable_initial_temp", "variable_volume"]
goal_state = ExtendedSimulator()
# "power_toggle_or_start_warming", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_bottle_type", step 1, variable_bottle_type
goal_state.variable_bottle_type.set_current_value("Milk bag")
# "adjust_initial_temp", step 1, variable_initial_temp
goal_state.variable_initial_temp.set_current_value("Room")
# "adjust_volume", step 1, variable_volume
goal_state.variable_volume.set_current_value("4-6 fl-oz")