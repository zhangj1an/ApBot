feature_sequence = ["power_on_off", "fan_speed"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'fan_speed' is required to set the fan speed to 'medium'."
changing_variables = ["variable_power_on_off", "variable_fan_speed"]
goal_state = Simulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "fan_speed", step 1, variable_fan_speed
goal_state.variable_fan_speed.set_current_value("medium")