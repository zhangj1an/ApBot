feature_sequence = ["power", "air_swing"]
feature_choice_reason = "Feature 'power' is required to turn on the dehumidifier. Feature 'air_swing' is required to start the air swing function."
changing_variables = ["variable_power_on_off", "variable_swing"]
goal_state = Simulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "air_swing", step 1, variable_swing
goal_state.variable_swing.set_current_value("on")