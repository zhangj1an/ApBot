feature_sequence = ["turn_on_off", "automatic_sterilize_dry"]
feature_choice_reason = "The appliance must be turned on first, which is achieved using the 'turn_on_off' feature. Then, the 'automatic_sterilize_dry' feature is used to set the drying time and start the sterilization cycle."
changing_variables = ["variable_on_off", "variable_drying_time", "variable_sterilization_cycle"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_on_off
goal_state.variable_on_off.set_current_value("on")
# "automatic_sterilize_dry", step 1, variable_drying_time
goal_state.variable_drying_time.set_current_value("60")
# "automatic_sterilize_dry", step 1, variable_sterilization_cycle
goal_state.variable_sterilization_cycle.set_current_value("running")