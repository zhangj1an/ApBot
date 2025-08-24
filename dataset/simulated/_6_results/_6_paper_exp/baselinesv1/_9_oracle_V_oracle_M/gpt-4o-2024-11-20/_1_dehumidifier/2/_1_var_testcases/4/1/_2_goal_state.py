feature_sequence = ["turn_on_off", "adjust_cool_mode_temperature"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'adjust_cool_mode_temperature' is needed to set the temperature to 30°C in Cool Mode."
changing_variables = ["variable_power_on_off", "variable_operating_mode", "variable_cool_mode_temperature"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_cool_mode_temperature", step 1, variable_operating_mode
goal_state.variable_operating_mode.set_current_value("COOL")
# "adjust_cool_mode_temperature", step 2, variable_cool_mode_temperature
goal_state.variable_cool_mode_temperature.set_current_value(30)