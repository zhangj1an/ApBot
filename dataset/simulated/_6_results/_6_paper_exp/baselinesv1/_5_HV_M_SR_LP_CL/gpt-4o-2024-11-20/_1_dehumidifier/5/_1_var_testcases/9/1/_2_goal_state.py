feature_sequence = ["power_control", "enable_sleep_mode"]
feature_choice_reason = "Feature 'power_control' is required to turn the unit on. Feature 'enable_sleep_mode' is required to ensure the sleep mode is 'off.'"
changing_variables = ["variable_power_on_off", "variable_sleep_mode"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "enable_sleep_mode", step 1, variable_sleep_mode
goal_state.variable_sleep_mode.set_current_value("off")