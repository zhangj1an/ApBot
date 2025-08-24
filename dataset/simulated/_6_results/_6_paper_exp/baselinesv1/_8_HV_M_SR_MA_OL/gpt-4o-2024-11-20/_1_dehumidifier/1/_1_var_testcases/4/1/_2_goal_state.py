feature_sequence = ["power_on_off", "adjust_anion_function"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'adjust_anion_function' is required to engage the anion function."
changing_variables = ["variable_power_on_off", "variable_anion_function"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_anion_function", step 1, variable_anion_function
goal_state.variable_anion_function.set_current_value("on")