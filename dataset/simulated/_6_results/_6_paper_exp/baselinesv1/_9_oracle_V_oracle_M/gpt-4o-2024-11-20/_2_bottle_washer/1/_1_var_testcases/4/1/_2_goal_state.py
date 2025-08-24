feature_sequence = ["turn_on_off", "sterilize_only"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the appliance. Feature 'sterilize_only' is required to start the sterilization cycle."
changing_variables = ["variable_on_off", "variable_sterilization_cycle"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "sterilize_only", step 1, variable_sterilization_cycle
goal_state.variable_sterilization_cycle.set_current_value("running")