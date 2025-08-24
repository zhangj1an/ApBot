feature_sequence = ["set_menu", "start_cooking"]
feature_choice_reason = "Feature 'set_menu' is used to set the menu to 'Quinoa' and adjust the cooking time to 35 minutes. Feature 'start_cooking' is required to start the cooking process."
changing_variables = ["variable_menu_index", "variable_menu_setting", "variable_start_running"]
goal_state = ExtendedSimulator()
# "set_menu", step 1, variable_menu_index
goal_state.variable_menu_index.set_current_value("Quinoa")
# "set_menu", step 2, variable_menu_setting
goal_state.variable_menu_setting = goal_state.menu_setting_dict["Quinoa"]
goal_state.variable_menu_setting.set_current_value(35) # the number represents minutes
# "start_cooking", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")