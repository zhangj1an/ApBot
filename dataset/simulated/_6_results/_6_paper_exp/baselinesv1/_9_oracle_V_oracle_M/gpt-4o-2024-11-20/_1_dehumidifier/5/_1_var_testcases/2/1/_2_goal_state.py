feature_sequence = ["turn_on_off", "toggle_ion_generator"]
feature_choice_reason = "Feature 'turn_on_off' is required to turn on the appliance. Feature 'toggle_ion_generator' is required to set the ion generator to 'on'."
changing_variables = ["variable_power_on_off", "variable_ion_generator"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "toggle_ion_generator", step 1, variable_ion_generator
goal_state.variable_ion_generator.set_current_value("on")