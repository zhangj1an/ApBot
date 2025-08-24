feature_sequence = ["turn_on_off", "dry_only"]
feature_choice_reason = "Feature 'turn_on_off' is required to activate the device. Feature 'dry_only' is required to set the drying cycle to 30 minutes."
changing_variables = ["variable_on_off", "variable_drying_cycle"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "dry_only", step 1, variable_drying_cycle
goal_state.variable_drying_cycle.set_current_value("30")