feature_sequence = ["power_on_off", "adjust_humidity"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'adjust_humidity' is required to set the humidity level to 50%."
changing_variables = ["variable_power_on_off", "variable_humidity_level"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_humidity", step 1, variable_humidity_level
goal_state.variable_humidity_level.set_current_value(50)