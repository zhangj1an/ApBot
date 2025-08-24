feature_sequence = ["turn_on_off", "menu"]
feature_choice_reason = "Feature 'turn_on_off' is required to power on the appliance. Feature 'menu' is required to select the sterilizing function and set the time to 15 minutes."
changing_variables = ["variable_power_on_off", "variable_menu_index", "variable_menu_time"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("sterilize")
# "menu", step 2, variable_menu_time
goal_state.variable_menu_time = goal_state.menu_time_dict["sterilize"]
goal_state.variable_menu_time.set_current_value(15) # The number represents minutes.