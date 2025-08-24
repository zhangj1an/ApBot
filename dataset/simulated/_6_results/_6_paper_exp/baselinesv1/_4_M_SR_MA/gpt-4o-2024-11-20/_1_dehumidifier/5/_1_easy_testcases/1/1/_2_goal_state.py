feature_sequence = ["power_control", "adjust_fan_speed"]
feature_choice_reason = "Feature 'power_control' is required to turn on the appliance by setting variable_power_on_off to 'on'. Feature 'adjust_fan_speed' is required to set the fan speed to 'mid' by adjusting variable_fan_speed."
changing_variables = ["variable_power_on_off", "variable_fan_speed"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_fan_speed", step 1, variable_fan_speed
goal_state.variable_fan_speed.set_current_value("2")