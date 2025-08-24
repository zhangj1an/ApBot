feature_sequence = ["power_on_off", "microbe_shield_night_mode"]
feature_choice_reason = "The appliance must be turned on first, so 'power_on_off' is included. Then, 'microbe_shield_night_mode' is included to set the mode to 'microbe_shield'."
changing_variables = ["variable_power_on_off", "variable_microbe_shield_night_mode"]
goal_state = Simulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "microbe_shield_night_mode", step 1, variable_microbe_shield_night_mode
goal_state.variable_microbe_shield_night_mode.set_current_value("microbe_shield")