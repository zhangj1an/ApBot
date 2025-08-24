# The current code accurately models the features required to achieve the user command. 

# Sequence of features needed:
# 1. "set_function_knob" - To set the function knob to the "Convection" function.
# 2. "adjust_upper_heater_temperature" - To adjust the upper heater temperature to 190 °C.
# 3. "adjust_lower_heater_temperature" - To adjust the lower heater temperature to 190 °C.
# 4. "set_timer" - To set the timer to 20 minutes.

# Raw user manual text relevant to the features:
# - "Turn the function knob to: ⌛ Convection (Lower & upper heater heating)."
# - "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# - "Timer: To set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."

# Relevant feature_list names in the given code:
# - "set_function_knob"
# - "adjust_upper_heater_temperature"
# - "adjust_lower_heater_temperature"
# - "set_timer"

# Goal variable values to achieve the command:
# - Set `variable_function_knob` to "Convection".
# - Set `variable_upper_heater_temperature` to 190.
# - Set `variable_lower_heater_temperature` to 190.
# - Set `variable_timer` to "20".

class ExtendedSimulator(Simulator): 
    pass