feature_sequence = ["power_on_off", "adjust_timer_setting"]
feature_choice_reason = "Feature 'power_on_off' is required to switch on the dehumidifier. Feature 'adjust_timer_setting' is required to set the programmable timer to 3 hours."
changing_variables = ["variable_power_on_off", "variable_timer_setting"]
goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "adjust_timer_setting", step 1, variable_timer_setting
goal_state.variable_timer_setting.set_current_value(3) # each number represents an hour.