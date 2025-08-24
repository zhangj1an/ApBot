feature_sequence = ["start_appliance", "select_cooking_program", "adjust_preset_time", "start_appliance"]
feature_choice_reason = "Feature 'start_appliance' is required to turn on the appliance. Feature 'select_cooking_program' is needed to set the cooking program to jasmine rice. Feature 'adjust_preset_time' is required to set the preset time to 4 hours. Finally, 'start_appliance' is used again to start the machine after all configurations are set."
changing_variables = ["variable_start_running", "variable_cooking_program", "variable_preset_time"]

goal_state = ExtendedSimulator()
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("jasmine_rice")
# "adjust_preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value(240)
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")