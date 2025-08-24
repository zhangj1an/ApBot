feature_sequence = ["power", "mode_selection"]
feature_choice_reason = "Feature 'power' is required to turn on the dehumidifier. Feature 'mode_selection' is required to set the dehumidifier to ventilation mode."
changing_variables = ["variable_power_on_off", "variable_mode"]
goal_state = Simulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "mode_selection", step 1, variable_mode
goal_state.variable_mode.set_current_value("ventilation")