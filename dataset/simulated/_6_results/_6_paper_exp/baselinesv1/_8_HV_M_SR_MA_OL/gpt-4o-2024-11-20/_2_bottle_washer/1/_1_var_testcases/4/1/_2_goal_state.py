feature_sequence = ["activate_sterilizer", "sterilize_only"]
feature_choice_reason = "Feature 'activate_sterilizer' is required to turn on the machine. Feature 'sterilize_only' is required to start the sterilize-only function."
changing_variables = ["variable_power_on_off"]
goal_state = ExtendedSimulator()
# "activate_sterilizer", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")