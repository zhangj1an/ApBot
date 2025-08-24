feature_sequence = ["power_on_off", "sterilize_only"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the machine. Feature 'sterilize_only' is required to start the sterilize-only function."
changing_variables = ["variable_power_on_off"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")