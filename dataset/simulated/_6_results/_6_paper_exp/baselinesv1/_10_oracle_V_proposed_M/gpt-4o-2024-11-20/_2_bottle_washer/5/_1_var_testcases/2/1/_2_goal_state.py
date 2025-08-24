feature_sequence = ["power_on_off", "auto_mode"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'auto_mode' is required to set the 35-minute auto cycle."
changing_variables = ["variable_power_on_off", "variable_auto_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "auto_mode", step 1, variable_auto_mode
goal_state.variable_auto_mode.set_current_value("35_minutes")