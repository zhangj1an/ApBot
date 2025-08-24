feature_sequence = ["weight_defrost", "child_lock"]
feature_choice_reason = "Feature 'weight_defrost' is chosen to set the weight of the chicken to 20 oz and start the appliance. Feature 'child_lock' is added to activate the child lock after starting the appliance."
changing_variables = ["variable_weight_defrost", "variable_child_lock"]
goal_state = Simulator()
# "weight_defrost", step 2, variable_weight_defrost
goal_state.variable_weight_defrost.set_current_value(20) # The number represents ounces.
# "child_lock", step 1, variable_child_lock
goal_state.variable_child_lock.set_current_value("locked")