feature_sequence = ["power_adjust", "adjust_cycle_selector", "adjust_temperature", "adjust_spin_speed", "adjust_options", "adjust_delay_end", "start_pause_cycle"]
feature_choice_reason = "Feature 'power_adjust' is needed to turn on the machine. Feature 'adjust_cycle_selector' is required to set the cycle to 'Wool'. Feature 'adjust_temperature' is needed to set the temperature to 'Cold water'. Feature 'adjust_spin_speed' is required to set the spin speed to '1200 rpm'. Feature 'adjust_options' is needed to set the option to 'Soak + Rinse+'. Feature 'adjust_delay_end' is required to set the delay to 5 hours. Finally, feature 'start_pause_cycle' is needed to start the machine."
changing_variables = ["variable_power_on_off", "variable_cycle_selector", "variable_temperature", "variable_spin_speed", "variable_option", "variable_delay_end", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_adjust", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_cycle_selector", step 1, variable_cycle_selector
goal_state.variable_cycle_selector.set_current_value("Wool")
# "adjust_temperature", step 1, variable_temperature
goal_state.variable_temperature.set_current_value("Cold water")
# "adjust_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("1200")
# "adjust_options", step 1, variable_option
goal_state.variable_option.set_current_value("Soak + Rinse+")
# "adjust_delay_end", step 1, variable_delay_end
goal_state.variable_delay_end.set_current_value(5) # The number represents hours.
# "start_pause_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")