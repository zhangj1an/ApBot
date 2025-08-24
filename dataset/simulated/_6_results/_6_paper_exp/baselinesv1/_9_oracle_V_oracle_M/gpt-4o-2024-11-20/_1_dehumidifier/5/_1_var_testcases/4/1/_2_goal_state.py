feature_sequence = ["turn_on_off", "activate_sleep_mode"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'activate_sleep_mode' is required to activate the sleep mode."
changing_variables = ["variable_power_on_off", "variable_sleep_mode"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "activate_sleep_mode", step 1, variable_sleep_mode
goal_state.variable_sleep_mode.set_current_value("on")