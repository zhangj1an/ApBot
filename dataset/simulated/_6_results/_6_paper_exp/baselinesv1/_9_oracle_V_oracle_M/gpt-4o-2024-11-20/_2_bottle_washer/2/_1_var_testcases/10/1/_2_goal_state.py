feature_sequence = ["turn_on_off", "select_bottle_type", "select_initial_temp", "select_volume"]
feature_choice_reason = "The appliance must be turned on first. Then, the bottle type, initial temperature, and volume need to be set sequentially to achieve the goal."
changing_variables = ["variable_power_on_off", "variable_bottle_type", "variable_initial_temp", "variable_volume"]
goal_state = Simulator()
# "turn_on_off", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "select_bottle_type", step 1, variable_bottle_type
goal_state.variable_bottle_type.set_current_value("Milk bag")
# "select_initial_temp", step 1, variable_initial_temp
goal_state.variable_initial_temp.set_current_value("Room- 25℃ (77℉)")
# "select_volume", step 1, variable_volume
goal_state.variable_volume.set_current_value("4-6 fl-oz")