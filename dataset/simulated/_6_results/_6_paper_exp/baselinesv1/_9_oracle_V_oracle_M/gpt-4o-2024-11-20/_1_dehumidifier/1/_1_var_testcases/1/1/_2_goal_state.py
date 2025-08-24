feature_sequence = ["power", "humidity_setting"]
feature_choice_reason = "The 'power' feature is required to turn on the dehumidifier. The 'humidity_setting' feature is needed to set the humidity to 50%."
changing_variables = ["variable_power_on_off", "variable_humidity"]
goal_state = Simulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "humidity_setting", step 1, variable_humidity
goal_state.variable_humidity.set_current_value(50)