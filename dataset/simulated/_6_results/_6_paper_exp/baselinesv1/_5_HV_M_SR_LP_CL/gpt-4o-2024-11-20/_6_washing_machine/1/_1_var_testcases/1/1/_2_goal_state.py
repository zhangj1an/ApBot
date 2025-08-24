feature_sequence = ["power_adjust", "adjust_cycle_selector", "adjust_temperature", "adjust_spin_speed", "adjust_options", "adjust_delay_end", "start_pause_cycle"]
feature_choice_reason = "The power_adjust feature is required to turn on the machine. The adjust_cycle_selector feature is needed to set the cycle to Cotton. The adjust_temperature feature is required to set the temperature to 30°C. The adjust_spin_speed feature is needed to set the spin speed to 800 rpm. The adjust_options feature is required to set the option to Prewash. The adjust_delay_end feature is needed to set the delay to 5 hours. Finally, the start_pause_cycle feature is required to start the machine."
changing_variables = ["variable_power_on_off", "variable_cycle_selector", "variable_temperature", "variable_spin_speed", "variable_option", "variable_delay_end", "variable_start_running"]
goal_state = ExtendedSimulator()
# "power_adjust", step 1, variable_power_on_off
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