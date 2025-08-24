feature_sequence = ["power_on_off", "mode_selection"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'mode_selection' is required to activate continuous dehumidification mode."
changing_variables = ["variable_power_on_off", "variable_mode_selection"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "mode_selection", step 1, variable_mode_selection
goal_state.variable_mode_selection.set_current_value("continuous_dehumidification")