feature_sequence = ["power_on_off", "microbe_shield_night_mode"]
feature_choice_reason = "The 'power_on_off' feature is required to turn on the appliance. The 'microbe_shield_night_mode' feature is needed to set the appliance to 'night_mode'."
changing_variables = ["variable_power_on_off", "variable_microbe_shield_night_mode"]
goal_state = Simulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "microbe_shield_night_mode", step 1, variable_microbe_shield_night_mode
goal_state.variable_microbe_shield_night_mode.set_current_value("night_mode")