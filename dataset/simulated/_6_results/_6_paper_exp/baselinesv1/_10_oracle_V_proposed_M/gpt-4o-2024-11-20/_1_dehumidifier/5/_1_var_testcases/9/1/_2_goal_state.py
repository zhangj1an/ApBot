feature_sequence = ["toggle_power", "toggle_sleep_mode_or_reset_filter_timer"]
feature_choice_reason = "Feature 'toggle_power' is required to turn the appliance on. Feature 'toggle_sleep_mode_or_reset_filter_timer' is required to ensure the sleep mode is set to 'off'."
changing_variables = ["variable_power_on_off", "variable_sleep_mode"]
goal_state = ExtendedSimulator()
# "toggle_power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "toggle_sleep_mode_or_reset_filter_timer", step 1, variable_sleep_mode
goal_state.variable_sleep_mode.set_current_value("off")