feature_sequence = ["power_on_off", "adjust_mode", "adjust_temperature"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'adjust_mode' is needed to set the mode to 'COOL'. Feature 'adjust_temperature' is required to set the temperature to 24°C."
changing_variables = ["variable_power_on_off", "variable_mode", "variable_temperature_setting"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_mode", step 1, variable_mode
goal_state.variable_mode.set_current_value("COOL")
# "adjust_temperature", step 1, variable_temperature_setting
goal_state.variable_temperature_setting.set_current_value(24)