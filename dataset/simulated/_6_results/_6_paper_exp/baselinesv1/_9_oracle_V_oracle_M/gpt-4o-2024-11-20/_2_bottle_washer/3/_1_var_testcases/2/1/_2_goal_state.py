feature_sequence = ["turn_on_off", "select_wash_mode", "start_pause"]
feature_choice_reason = "Feature 'turn_on_off' is required to power up the appliance. Feature 'select_wash_mode' is needed to choose the 'Wash, Sterilize, Dry' cycle. Feature 'start_pause' is required to start the appliance after setting the desired mode."
changing_variables = ["variable_power_on_off", "variable_wash_mode", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_wash_mode", step 1, variable_wash_mode
goal_state.variable_wash_mode.set_current_value("Wash, Sterilize, Dry")
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")