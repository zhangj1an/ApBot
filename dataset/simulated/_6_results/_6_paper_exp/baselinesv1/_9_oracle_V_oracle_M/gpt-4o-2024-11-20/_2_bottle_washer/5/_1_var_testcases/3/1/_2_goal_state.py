feature_sequence = ["turn_on_off", "drying_only"]
feature_choice_reason = "Feature 'turn_on_off' is required to power up the appliance. Feature 'drying_only' is required to set the drying time to 40 minutes."
changing_variables = ["variable_power_on_off", "variable_drying_only_time"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "drying_only", step 1, variable_drying_only_time
goal_state.variable_drying_only_time.set_current_value("40")