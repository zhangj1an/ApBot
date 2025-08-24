feature_sequence = ["power_and_start_warming", "select_bottle_type", "select_initial_temperature", "select_volume"]
feature_choice_reason = "Feature 'power_and_start_warming' is required to turn on the appliance. Feature 'select_bottle_type' is needed to set the bottle type to 'Silicone'. Feature 'select_initial_temperature' is required to set the initial temperature to 'Frozen'. Feature 'select_volume' is needed to set the volume to '7+ fl-oz'."
changing_variables = ["variable_power_on_off", "variable_bottle_type", "variable_initial_temp", "variable_volume"]
goal_state = ExtendedSimulator()
# "power_and_start_warming", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_bottle_type", step 1, variable_bottle_type
goal_state.variable_bottle_type.set_current_value("Silicone")
# "select_initial_temperature", step 1, variable_initial_temp
goal_state.variable_initial_temp.set_current_value("Frozen")
# "select_volume", step 1, variable_volume
goal_state.variable_volume.set_current_value("7+ fl-oz")