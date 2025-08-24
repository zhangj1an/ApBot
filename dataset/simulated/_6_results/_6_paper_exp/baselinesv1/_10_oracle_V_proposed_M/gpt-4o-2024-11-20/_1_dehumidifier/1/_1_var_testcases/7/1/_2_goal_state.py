feature_sequence = ["power_on_off", "humidity_level_adjustment"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'humidity_level_adjustment' is required to adjust the humidity setting to 60%."
changing_variables = ["variable_power_on_off", "variable_humidity_level"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "humidity_level_adjustment", step 1, variable_humidity_level
goal_state.variable_humidity_level.set_current_value(60)