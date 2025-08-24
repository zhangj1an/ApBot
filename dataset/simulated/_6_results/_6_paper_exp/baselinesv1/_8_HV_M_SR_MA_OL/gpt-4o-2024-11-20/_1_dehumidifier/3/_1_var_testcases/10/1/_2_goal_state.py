feature_sequence = ["adjust_fan_speed_mode", "power_control"]
feature_choice_reason = "Feature 'adjust_fan_speed_mode' is required to set the appliance to Turbo mode. However, the appliance must be turned on to operate, which is achieved using the 'power_control' feature."
changing_variables = ["variable_fan_speed_mode", "variable_power_on_off"]
goal_state = ExtendedSimulator()
# "adjust_fan_speed_mode", step 1, variable_fan_speed_mode
goal_state.variable_fan_speed_mode.set_current_value("Turbo")
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")