feature_sequence = ["power_on_off", "fan_speed"]
feature_choice_reason = "The appliance must be turned on first, so 'power_on_off' is included. Then, the fan speed needs to be set to 'low', which is achieved through the 'fan_speed' feature."
changing_variables = ["variable_power_on_off", "variable_fan_speed"]
goal_state = Simulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "fan_speed", step 1, variable_fan_speed
goal_state.variable_fan_speed.set_current_value("low")