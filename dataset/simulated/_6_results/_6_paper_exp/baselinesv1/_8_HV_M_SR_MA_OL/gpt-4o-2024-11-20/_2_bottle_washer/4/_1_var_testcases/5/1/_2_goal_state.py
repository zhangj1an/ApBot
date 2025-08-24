feature_sequence = ["turn_on_off_appliance", "set_and_adjust_menu"]
feature_choice_reason = "Feature 'turn_on_off_appliance' is required to turn on the appliance. Feature 'set_and_adjust_menu' is required to select the 'Steam' function and set the steam time to 13 minutes."
changing_variables = ["variable_power_on_off", "variable_menu_index", "variable_menu_setting"]
goal_state = ExtendedSimulator()
# "turn_on_off_appliance", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "set_and_adjust_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Steam")
# "set_and_adjust_menu", step 2, variable_menu_setting
goal_state.variable_menu_setting = goal_state.variable_menu_setting_steam
goal_state.variable_menu_setting.set_current_value(13) # The number represents minutes.