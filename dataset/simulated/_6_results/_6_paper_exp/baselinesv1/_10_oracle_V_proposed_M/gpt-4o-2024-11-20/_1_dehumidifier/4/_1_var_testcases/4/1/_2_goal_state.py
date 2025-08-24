feature_sequence = ["power_on_off", "adjust_microbe_shield_night_mode"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'adjust_microbe_shield_night_mode' is required to set the mode to 'night_mode'."
changing_variables = ["variable_power_on_off", "variable_microbe_shield_night_mode"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_microbe_shield_night_mode", step 1, variable_microbe_shield_night_mode
goal_state.variable_microbe_shield_night_mode.set_current_value("night_mode")