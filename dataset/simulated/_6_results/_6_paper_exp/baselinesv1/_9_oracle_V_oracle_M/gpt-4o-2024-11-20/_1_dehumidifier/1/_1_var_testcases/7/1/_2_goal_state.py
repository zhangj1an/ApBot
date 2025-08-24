feature_sequence = ["power", "humidity_setting"]
feature_choice_reason = "Feature 'power' is required to turn on the dehumidifier. Feature 'humidity_setting' is required to adjust the humidity to 60%."
changing_variables = ["variable_power_on_off", "variable_humidity"]
goal_state = Simulator()
# "power", step 1, variable_power_on_off
goal_state.variable_power_on_off.set_current_value("on")
# "humidity_setting", step 1, variable_humidity
goal_state.variable_humidity.set_current_value(60)