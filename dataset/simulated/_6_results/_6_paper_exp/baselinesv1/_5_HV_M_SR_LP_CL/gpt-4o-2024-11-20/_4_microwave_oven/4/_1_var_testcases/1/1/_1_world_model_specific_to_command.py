# The current code correctly models the appliance features to achieve the requested user command.

# Sequence of features needed:
# 1. "set_function_knob": To select the lower & upper heater function.
# 2. "adjust_upper_heater_temperature": To set the upper heater temperature to 110 °C.
# 3. "adjust_lower_heater_temperature": To set the lower heater temperature to 110 °C.
# 4. "set_timer": To set the timer to 20 minutes.

# Relevant raw user manual text:
# ● Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C
# ● Timer: The electric oven beeps when the timer reaches "0". Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time. In case of “Stay On” mode, you have to disable the timer manually as the latter cannot be adjusted automatically.
# ● Function knob:
#   □ Operates the lower heater
#   □ Operates the upper heater
#   □ Operates the lower & upper heater at the same time
#   ⌛ Convection (Lower & upper heater heating)

# Feature names from the given code:
# 1. "set_function_knob"
# 2. "adjust_upper_heater_temperature"
# 3. "adjust_lower_heater_temperature"
# 4. "set_timer"

# Goal variable values:
# 1. variable_function_knob: "Lower & Upper Heater"
# 2. variable_upper_heater_temperature: 110 °C
# 3. variable_lower_heater_temperature: 110 °C
# 4. variable_timer: "20"

class ExtendedSimulator(Simulator): 
    pass