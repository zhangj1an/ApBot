feature_sequence = ["power_control", "choose_wash_mode", "start_cycle"]
feature_choice_reason = "Feature 'power_control' is required to turn on the appliance. Feature 'choose_wash_mode' is needed to set the wash mode to 'Wash Only'. Feature 'start_cycle' is required to start the appliance after setting the desired mode."
changing_variables = ["variable_power_on_off", "variable_wash_mode", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "choose_wash_mode", step 1, variable_wash_mode
goal_state.variable_wash_mode.set_current_value("Wash Only")
# "start_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")