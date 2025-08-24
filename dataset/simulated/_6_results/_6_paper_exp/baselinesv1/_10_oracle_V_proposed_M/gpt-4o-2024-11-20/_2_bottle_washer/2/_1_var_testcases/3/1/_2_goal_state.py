feature_sequence = ["power_toggle_or_start_warming", "adjust_bottle_type", "adjust_initial_temp", "adjust_volume", "power_toggle_or_start_warming"]
feature_choice_reason = "Firstly, turn on the appliance using 'power_toggle_or_start_warming'. Then, adjust the bottle type to 'Silicone' using 'adjust_bottle_type'. Next, set the initial temperature to 'Frozen' using 'adjust_initial_temp'. After that, set the volume to '7+ fl-oz' using 'adjust_volume'. Finally, start the warming process using 'power_toggle_or_start_warming'."
changing_variables = ["variable_power_on_off", "variable_bottle_type", "variable_initial_temp", "variable_volume", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_toggle_or_start_warming", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_bottle_type", step 1, variable_bottle_type
goal_state.variable_bottle_type.set_current_value("Silicone")
# "adjust_initial_temp", step 1, variable_initial_temp
goal_state.variable_initial_temp.set_current_value("Frozen")
# "adjust_volume", step 1, variable_volume
goal_state.variable_volume.set_current_value("7+ fl-oz")
# "power_toggle_or_start_warming", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")