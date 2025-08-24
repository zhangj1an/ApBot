feature_sequence = ["power_on_off", "adjust_air_swing"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'adjust_air_swing' is required to start the air swing function."
changing_variables = ["variable_power_on_off", "variable_air_swing"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_air_swing", step 1, variable_air_swing
goal_state.variable_air_swing.set_current_value("on")