feature_sequence = ["turn_on_off", "fan_speed_mode"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the appliance if it is off. Feature 'fan_speed_mode' is required to set the fan speed to Level 3 for strong airflow."
changing_variables = ["variable_power_on_off", "variable_fan_speed_mode"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "fan_speed_mode", step 1, variable_fan_speed_mode
goal_state.variable_fan_speed_mode.set_current_value("3")