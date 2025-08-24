feature_sequence = ["toggle_power", "adjust_fan_speed"]
feature_choice_reason = "Feature 'toggle_power' is required to turn on the appliance. Feature 'adjust_fan_speed' is required to set the fan speed to 'low'."
changing_variables = ["variable_power_on_off", "variable_fan_speed"]
goal_state = ExtendedSimulator()
# "toggle_power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_fan_speed", step 1, variable_fan_speed
goal_state.variable_fan_speed.set_current_value("1")