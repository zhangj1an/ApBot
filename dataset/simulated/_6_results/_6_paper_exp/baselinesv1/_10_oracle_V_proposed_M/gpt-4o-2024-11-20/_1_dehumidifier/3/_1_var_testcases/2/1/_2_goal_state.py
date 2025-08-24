feature_sequence = ["power_on_off", "fan_speed_mode_control"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'fan_speed_mode_control' is needed to set the fan speed to level 1."
changing_variables = ["variable_power_on_off", "variable_fan_speed_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "fan_speed_mode_control", step 1, variable_fan_speed_mode
goal_state.variable_fan_speed_mode.set_current_value("1")