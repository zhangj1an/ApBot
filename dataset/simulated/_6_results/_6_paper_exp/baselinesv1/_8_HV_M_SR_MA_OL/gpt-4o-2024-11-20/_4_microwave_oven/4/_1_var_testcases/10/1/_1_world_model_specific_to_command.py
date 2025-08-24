# The requested user command and the given code's features are consistent with each other and correspond
# The sequence of features needed to achieve the user command is as follows:
# 1. "set_function_knob" - Use the function knob to set the appliance to "Upper Heater" function
# 2. "adjust_upper_heater_temperature" - Adjust the upper heater temperature to 190 °C
# 3. "adjust_lower_heater_temperature" - Adjust the lower heater temperature to 190 °C
# 4. "set_timer" - Adjust the timer to 20 minutes

# Relevant user manual text verifies functionality:
# - Feature "set_function_knob": "Function knob: □ Operates the upper heater"
# - Feature "adjust_upper_heater_temperature": "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# - Feature "adjust_lower_heater_temperature": "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# - Feature "set_timer": "Timer: The electric oven beeps when the timer reaches '0'."

# The following variable values are the goal for the user command:
# variable_function_knob = "Upper Heater"
# variable_upper_heater_temperature = 190
# variable_lower_heater_temperature = 190
# variable_timer = "20"

class ExtendedSimulator(Simulator): 
    pass