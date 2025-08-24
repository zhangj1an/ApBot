feature_sequence = ["turn_on_off", "adjust_fan_speed"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'adjust_fan_speed' is required to set the fan speed to HIGH."
changing_variables = ["variable_power_on_off", "variable_fan_speed"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_fan_speed", step 1, variable_fan_speed
goal_state.variable_fan_speed.set_current_value("HIGH")