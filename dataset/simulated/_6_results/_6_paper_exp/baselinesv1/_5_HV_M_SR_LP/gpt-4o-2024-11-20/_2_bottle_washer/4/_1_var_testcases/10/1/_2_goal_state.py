feature_sequence = ["turn_on_off_appliance", "set_and_adjust_menu"]
feature_choice_reason = "Feature 'turn_on_off_appliance' is required to switch the appliance on. Feature 'set_and_adjust_menu' is required to select the 'Steam' menu and adjust the steam time to 18 minutes."
changing_variables = ["variable_power_on_off", "variable_menu_index", "variable_menu_setting"]
goal_state = ExtendedSimulator()
# "turn_on_off_appliance", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_and_adjust_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Steam")
# "set_and_adjust_menu", step 2, variable_menu_setting
goal_state.variable_menu_setting = goal_state.variable_menu_setting_steam
goal_state.variable_menu_setting.set_current_value(18) # The number represents minutes.