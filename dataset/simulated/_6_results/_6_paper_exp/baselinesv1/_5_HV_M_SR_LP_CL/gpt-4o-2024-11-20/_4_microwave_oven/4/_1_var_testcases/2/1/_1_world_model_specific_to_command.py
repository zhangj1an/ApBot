# The code already models the necessary variables and features to fulfill the requested user command.
# User command is to turn on the appliance, set the upper heater temperature to 70 °C, the lower heater temperature to 70 °C, 
# the timer to 20 minutes, and use the lower heater function.

# Relevant user manual text:
# 1. "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# 2. "Timer: The electric oven beeps when the timer reaches '0'. Tips: to set baking time less than 20 minutes, 
# turn up the knob beyond 40 minutes then return to the desired time."
# 3. "Function knob: □ Operates the lower heater"

# The relevant feature_list names in the given code:
# - "set_function_knob": To set the function knob to "Lower Heater".
# - "adjust_upper_heater_temperature": To set the upper heater temperature.
# - "adjust_lower_heater_temperature": To set the lower heater temperature.
# - "set_timer": To set the timer.

# Required sequence to achieve this command:
# 1. Adjust "set_function_knob" feature: Set variable_function_knob to "Lower Heater".
# 2. Adjust "adjust_upper_heater_temperature" feature: Set variable_upper_heater_temperature to 70 °C.
# 3. Adjust "adjust_lower_heater_temperature" feature: Set variable_lower_heater_temperature to 70 °C.
# 4. Adjust "set_timer" feature: Set variable_timer to "20".

# Goal variable values:
# - variable_function_knob: "Lower Heater"
# - variable_upper_heater_temperature: 70
# - variable_lower_heater_temperature: 70
# - variable_timer: "20"

class ExtendedSimulator(Simulator): 
    pass