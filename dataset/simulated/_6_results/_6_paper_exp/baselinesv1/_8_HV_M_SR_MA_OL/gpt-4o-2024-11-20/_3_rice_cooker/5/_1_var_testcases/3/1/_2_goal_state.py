feature_sequence = ["start_appliance", "select_cooking_program", "adjust_preset_time"]
feature_choice_reason = "Feature 'start_appliance' is required to turn on the appliance. Feature 'select_cooking_program' is needed to set the cooking mode to 'brown_rice'. Feature 'adjust_preset_time' is necessary to set the preset time to 5 hours."
changing_variables = ["variable_start_running", "variable_cooking_program", "variable_preset_time"]
goal_state = ExtendedSimulator()
# "start_appliance", step 1, variable_start_running
goal_state.variable_start_running.set_current_value("on")
# "select_cooking_program", step 1, variable_cooking_program
goal_state.variable_cooking_program.set_current_value("brown_rice")
# "adjust_preset_time", step 1, variable_preset_time
goal_state.variable_preset_time.set_current_value(300) # The number represents minutes.