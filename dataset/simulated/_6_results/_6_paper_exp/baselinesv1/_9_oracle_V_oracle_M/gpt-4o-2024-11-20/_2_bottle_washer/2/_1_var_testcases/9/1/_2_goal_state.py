feature_sequence = ["turn_on_off", "select_bottle_type", "select_initial_temp", "select_volume"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'select_bottle_type' is needed to set the bottle type to silicone. Feature 'select_initial_temp' is required to set the initial temperature to frozen (0℃). Feature 'select_volume' is needed to set the volume to 1-3 fl-oz."
changing_variables = ["variable_power_on_off", "variable_bottle_type", "variable_initial_temp", "variable_volume"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_bottle_type", step 1, variable_bottle_type
goal_state.variable_bottle_type.set_current_value("Silicone")
# "select_initial_temp", step 1, variable_initial_temp
goal_state.variable_initial_temp.set_current_value("Frozen- 0℃ (32℉)")
# "select_volume", step 1, variable_volume
goal_state.variable_volume.set_current_value("1-3 fl-oz")