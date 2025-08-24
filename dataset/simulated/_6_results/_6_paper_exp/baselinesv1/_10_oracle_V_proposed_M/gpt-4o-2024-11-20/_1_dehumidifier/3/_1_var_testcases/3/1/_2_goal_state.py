feature_sequence = ["power_on_off", "set_timer", "fan_speed_mode_control"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'set_timer' is needed to set the timer to 1 hour. Feature 'fan_speed_mode_control' is necessary to switch the fan to Turbo mode."
changing_variables = ["variable_power_on_off", "variable_timer", "variable_fan_speed_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("1H")
# "fan_speed_mode_control", step 1, variable_fan_speed_mode
goal_state.variable_fan_speed_mode.set_current_value("Turbo")