feature_sequence = ["turn_on_off", "auto_mode"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the appliance. Feature 'auto_mode' is required to set the 35-minute auto cycle."
changing_variables = ["variable_power_on_off", "variable_auto_mode_time"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "auto_mode", step 1, variable_auto_mode_time
goal_state.variable_auto_mode_time.set_current_value("35")