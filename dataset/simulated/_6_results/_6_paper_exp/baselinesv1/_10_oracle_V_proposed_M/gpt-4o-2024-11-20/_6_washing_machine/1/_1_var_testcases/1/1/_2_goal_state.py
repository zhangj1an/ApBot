feature_sequence = ["power_on_off", "adjust_cycle_selector", "adjust_temperature", "adjust_spin_speed", "adjust_options", "adjust_delay_end", "start_pause_cycle"]
feature_choice_reason = "The machine must be turned on first. Then, the cycle selector is adjusted to 'Cotton'. Next, the temperature is set to '30°C', followed by setting the spin speed to '800 rpm'. The prewash option is selected, and the delay end is set to 5 hours. Finally, the machine is started to begin the wash cycle."
changing_variables = ["variable_power_on_off", "variable_cycle_selector", "variable_temperature", "variable_spin_speed", "variable_option", "variable_delay_end", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_cycle_selector", step 1, variable_cycle_selector
goal_state.variable_cycle_selector.set_current_value("Cotton")
# "adjust_temperature", step 1, variable_temperature
goal_state.variable_temperature.set_current_value("30°C")
# "adjust_spin_speed", step 1, variable_spin_speed
goal_state.variable_spin_speed.set_current_value("800")
# "adjust_options", step 1, variable_option
goal_state.variable_option.set_current_value("Prewash")
# "adjust_delay_end", step 1, variable_delay_end
goal_state.variable_delay_end.set_current_value(5) # The number represents hours.
# "start_pause_cycle", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")