feature_sequence = ["menu", "start"]
feature_choice_reason = "Feature 'menu' is used to set the cooking mode to Quinoa and adjust the cooking time to 35 minutes. Feature 'start' is used to start the appliance after the settings are configured."
changing_variables = ["variable_menu_selection", "variable_cooking_time", "variable_start_running"]
goal_state = Simulator()
# "menu", step 1, variable_menu_selection
goal_state.variable_menu_selection.set_current_value("Quinoa")
# "menu", step 2, variable_cooking_time
goal_state.variable_cooking_time.set_current_value(35) # The number represents minutes.
# "start", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")