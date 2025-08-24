feature_sequence = ["power_on_off", "mode_selection"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'mode_selection' is required to set the mode to ventilation. Additionally, variable_child_lock is included in 'mode_selection' and must be set to its default value."
changing_variables = ["variable_power_on_off", "variable_mode_selection", "variable_child_lock"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "mode_selection", step 1, variable_mode_selection
goal_state.variable_mode_selection.set_current_value("ventilation")
# "mode_selection", step 2, variable_child_lock
goal_state.variable_child_lock.set_current_value("off")