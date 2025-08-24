feature_sequence = ["weight_defrost", "child_lock_control"]
feature_choice_reason = "Feature 'weight_defrost' is used to set the weight of the chicken to 20 oz and start the appliance. Feature 'child_lock_control' is used to activate the child lock after starting the appliance."
changing_variables = ["variable_weight_defrost", "variable_start_running", "variable_child_lock"]
goal_state = ExtendedSimulator()
# "weight_defrost", step 2, variable_weight_defrost
goal_state.variable_weight_defrost.set_current_value(20) # weight in oz
# "weight_defrost", step 3, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "child_lock_control", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("locked")