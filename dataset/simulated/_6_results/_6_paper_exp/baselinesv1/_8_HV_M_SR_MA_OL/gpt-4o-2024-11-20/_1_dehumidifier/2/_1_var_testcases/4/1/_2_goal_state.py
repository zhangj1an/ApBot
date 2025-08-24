feature_sequence = ["power_on_off", "set_operating_mode", "set_temperature"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'set_operating_mode' is needed to set the mode to Cool. Feature 'set_temperature' is required to set the temperature to 30°C."
changing_variables = ["variable_power_on_off", "variable_mode", "variable_temperature_setting"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_operating_mode", step 1, variable_mode
goal_state.variable_mode.set_current_value("COOL")
# "set_temperature", step 1, variable_temperature_setting
goal_state.variable_temperature_setting.set_current_value(30)