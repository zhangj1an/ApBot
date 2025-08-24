feature_sequence = ["power", "anion_function"]
feature_choice_reason = "Feature 'power' is required to turn on the dehumidifier. Feature 'anion_function' is required to engage the anion function."
changing_variables = ["variable_power_on_off", "variable_anion"]
goal_state = Simulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "anion_function", step 1, variable_anion
goal_state.variable_anion.set_current_value("on")