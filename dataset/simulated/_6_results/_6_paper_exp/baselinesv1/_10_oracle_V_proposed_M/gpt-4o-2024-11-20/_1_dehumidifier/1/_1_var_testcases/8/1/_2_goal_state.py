feature_sequence = ["power_on_off", "mode_selection"]
feature_choice_reason = "The 'power_on_off' feature is required to turn on the dehumidifier. The 'mode_selection' feature is needed to set the mode to 'purification'."
changing_variables = ["variable_power_on_off", "variable_mode_selection"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "mode_selection", step 1, variable_mode_selection
goal_state.variable_mode_selection.set_current_value("purification")