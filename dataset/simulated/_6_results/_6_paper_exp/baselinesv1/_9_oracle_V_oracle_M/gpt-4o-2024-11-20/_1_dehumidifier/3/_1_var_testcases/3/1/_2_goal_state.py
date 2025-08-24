feature_sequence = ["turn_on_off", "set_timer", "fan_speed_mode"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'set_timer' is needed to set the timer to 1 hour. Feature 'fan_speed_mode' is required to switch the fan to Turbo mode."
changing_variables = ["variable_power_on_off", "variable_timer", "variable_fan_speed_mode"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_timer", step 1, variable_timer
goal_state.variable_timer.set_current_value("1")
# "fan_speed_mode", step 1, variable_fan_speed_mode
goal_state.variable_fan_speed_mode.set_current_value("Turbo")