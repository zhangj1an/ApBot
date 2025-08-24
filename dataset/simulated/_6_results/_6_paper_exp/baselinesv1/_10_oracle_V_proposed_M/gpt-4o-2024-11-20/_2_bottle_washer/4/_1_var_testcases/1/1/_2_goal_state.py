feature_sequence = ["power_on_off", "set_menu_and_adjust_setting"]
feature_choice_reason = "Feature 'power_on_off' is required to turn on the appliance. Feature 'set_menu_and_adjust_setting' is required to set the menu to 'Quick' and adjust the time to 3 minutes."
changing_variables = ["variable_power_on_off", "variable_menu_index", "variable_menu_setting"]

goal_state = ExtendedSimulator()
# "power_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_menu_and_adjust_setting", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Quick")
# "set_menu_and_adjust_setting", step 2, variable_menu_setting
goal_state.variable_menu_setting = goal_state.variable_menu_setting_quick
goal_state.variable_menu_setting.set_current_value(3)  # The number represents minutes.