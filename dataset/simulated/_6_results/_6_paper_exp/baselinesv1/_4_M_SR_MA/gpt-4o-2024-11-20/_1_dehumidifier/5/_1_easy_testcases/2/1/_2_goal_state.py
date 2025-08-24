feature_sequence = ["power_control", "control_ion_generator"]
feature_choice_reason = "Feature 'power_control' is required to turn on the appliance by setting variable_power_on_off to 'on'. Feature 'control_ion_generator' is required to toggle the ion generator to 'on' by setting variable_ion_generator to 'on'."
changing_variables = ["variable_power_on_off", "variable_ion_generator"]
goal_state = ExtendedSimulator()
# "power_control", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "control_ion_generator", step 1, variable_ion_generator
goal_state.variable_ion_generator.set_current_value("on")