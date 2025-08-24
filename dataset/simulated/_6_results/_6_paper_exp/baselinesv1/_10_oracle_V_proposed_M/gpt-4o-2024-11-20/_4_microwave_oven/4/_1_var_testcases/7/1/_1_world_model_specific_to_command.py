# The current code accurately models the necessary features described in the user manual required to execute the user command. 
# Below is the step-by-step process to achieve the requested task:

# Sequence of features needed to achieve the command:
# 1. Adjust upper heater temperature to 190 °C: "adjust_upper_heater_temperature"
# 2. Adjust lower heater temperature to 190 °C: "adjust_lower_heater_temperature"
# 3. Set the timer to 20 minutes: "adjust_timer"
# 4. Select the convection function: "select_function"

# Relevant raw user manual text:
# For upper and lower heater temperature knobs: "Temperature range: 70 °C - 230 °C"
# For timer: "Timer: The electric oven beeps when the timer reaches '0'. Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
# For function knob: "Function knob: ⌛ Convection (Lower & upper heater heating)."

# Relevant variable and feature mapping in the code:
# 1. "adjust_upper_heater_temperature" → variable_upper_heater_temperature
# 2. "adjust_lower_heater_temperature" → variable_lower_heater_temperature
# 3. "adjust_timer" → variable_timer
# 4. "select_function" → variable_function_knob

# Goal variable values to fulfill the command:
# variable_upper_heater_temperature = 190
# variable_lower_heater_temperature = 190
# variable_timer = "20"
# variable_function_knob = "Convection"

class ExtendedSimulator(Simulator): 
    pass