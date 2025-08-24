feature_sequence = ["power", "mode_selection"]
feature_choice_reason = "The 'power' feature is required to turn on the dehumidifier. The 'mode_selection' feature is needed to set the dehumidifier to continuous dehumidification mode."
changing_variables = ["variable_power_on_off", "variable_mode"]
goal_state = Simulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "mode_selection", step 1, variable_mode
goal_state.variable_mode.set_current_value("continuous dehumidification")