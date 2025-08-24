feature_sequence = ["power_on_off", "set_operating_mode"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'set_operating_mode' is required to set the operating mode to DRY."
changing_variables = ["variable_power_on_off", "variable_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_operating_mode", step 1, variable_mode
goal_state.variable_mode.set_current_value("DRY")