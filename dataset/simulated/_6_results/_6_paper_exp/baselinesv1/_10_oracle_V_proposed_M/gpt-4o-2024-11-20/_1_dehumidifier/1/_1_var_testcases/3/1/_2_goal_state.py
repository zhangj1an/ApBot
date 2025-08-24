feature_sequence = ["power_on_off", "internal_drying"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the dehumidifier. Feature 'internal_drying' is required to initiate the internal drying function."
changing_variables = ["variable_power_on_off", "variable_internal_drying"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "internal_drying", step 1, variable_internal_drying
goal_state.variable_internal_drying.set_current_value("on")