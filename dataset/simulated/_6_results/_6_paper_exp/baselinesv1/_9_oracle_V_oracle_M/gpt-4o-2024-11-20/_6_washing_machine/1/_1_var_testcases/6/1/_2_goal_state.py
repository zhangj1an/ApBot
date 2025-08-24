feature_sequence = ["turn_on_off", "set_cycle", "set_temperature", "set_spin_speed", "set_option", "set_delay_end", "start_pause"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'set_cycle' is needed to select the Stain Away cycle. Feature 'set_temperature' is required to set the temperature to 60 °C. Feature 'set_spin_speed' is needed to set the spin speed to 1400 rpm. Feature 'set_option' is required to set the option to Soak + Rinse+. Feature 'set_delay_end' is required to set the delay to 5 hours. Finally, feature 'start_pause' is required to start the machine."
changing_variables = ["variable_power_on_off", "variable_cycle_selector", "variable_temperature", "variable_spin_speed", "variable_option", "variable_delay_end", "variable_start_running"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_cycle", step 1, variable_cycle_selector
goal_state.variable_cycle_selector.set_current_value("Stain Away")
# "set_temperature", step 1, variable_temperature
goal_state.variable_temperature.set_current_value("60 °C")
# "set_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("1400")
# "set_option", step 1, variable_option
goal_state.variable_option.set_current_value("Soak + Rinse+")
# "set_delay_end", step 1, variable_delay_end
goal_state.variable_delay_end.set_current_value(5) # The number represents hours.
# "start_pause", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")