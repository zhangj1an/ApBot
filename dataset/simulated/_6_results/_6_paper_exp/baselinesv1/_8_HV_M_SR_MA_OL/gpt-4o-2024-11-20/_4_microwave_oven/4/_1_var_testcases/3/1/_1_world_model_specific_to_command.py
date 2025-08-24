# The given code correctly models the features and variables needed to achieve the user command:
# "Turn on the microwave to reheat leftover pizza. Set the upper heater temperature to 190 °C, 
# the lower heater temperature to 190 °C, the timer to 40 minutes, and use the convection function."

# Sequence of features needed to achieve the command:
# 1. "set_function_knob" - Set the function knob to "Convection".
# 2. "adjust_upper_heater_temperature" - Set the upper heater temperature to 190 °C.
# 3. "adjust_lower_heater_temperature" - Set the lower heater temperature to 190 °C.
# 4. "set_timer" - Set the timer to 40 minutes.

# Relevant raw user manual texts:
# ● Function knob:
# ⌛ Convection (Lower & upper heater heating)
# ● Upper and lower heaters temperature knobs:
# Temperature range: 70 °C - 230 °C
# ● Timer:
# The electric oven beeps when the timer reaches "0". Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time.

# Corresponding feature_list names:
# - "set_function_knob"
# - "adjust_upper_heater_temperature"
# - "adjust_lower_heater_temperature"
# - "set_timer"

# Goal variable values to achieve this command:
# - variable_function_knob: "Convection"
# - variable_upper_heater_temperature: 190
# - variable_lower_heater_temperature: 190
# - variable_timer: "40"

class ExtendedSimulator(Simulator):
    pass