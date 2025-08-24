feature_sequence = ["set_weight_defrost", "toggle_child_lock"]
feature_choice_reason = "Feature 'set_weight_defrost' is used to set the weight defrost to 20 oz and start the appliance. Feature 'toggle_child_lock' is used to activate the child lock after starting the appliance."
changing_variables = ["variable_weight_defrost", "variable_start_running", "variable_child_lock"]
goal_state = ExtendedSimulator()
# "set_weight_defrost", step 2, variable_weight_defrost
goal_state.variable_weight_defrost.set_current_value(20) # weight in oz
# "set_weight_defrost", step 3, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "toggle_child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("locked")