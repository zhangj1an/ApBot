# The raw user manual description explains how to achieve the requested user command:
#   - Setting the upper heater temperature and lower heater temperature independently
#   - Setting the timer
#   - Selecting the rotary function

# Quoting relevant feature descriptions and the corresponding `feature_list` code:
# "To reach quickly the temperature of 70 °C to 230 °C in the oven, set the function knob:
#   □ Operates the lower & upper heater at the same time selection
#   or select ⌛ Convection, and the Upper and lower heater temperature knobs must be set to the same temperature at the same time."
# Related feature_list in the provided code: "adjust_upper_heater_temperature", "adjust_lower_heater_temperature"

# "Timer: The electric oven beeps when the timer reaches '0'. Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
# Related feature_list in the provided code: "set_timer"

# Function knob is set using this excerpt:
# "Function knob:
#   □ Operates the lower heater
#   □ Operates the upper heater
#   □ Operates the lower & upper heater at the same time
#   ⌛ Convection (Lower & upper heater heating)
#   ↻ Rotary (Upper heater heating) Fermentation"
# Related feature_list in the provided code: "set_function_knob"

# As analyzed, the simulator already models the features correctly and includes all relevant actions and variables.
# Below are the steps to achieve the user command:

# Sequence of features needed to achieve this command:
# 1. "adjust_upper_heater_temperature" - Use actions to set the upper heater temperature to 110 °C
# 2. "adjust_lower_heater_temperature" - Use actions to set the lower heater temperature to 110 °C
# 3. "set_timer" - Use actions to set the timer to 100 minutes
# 4. "set_function_knob" - Use actions to select the Rotary function

# Goal variable values:
# - `variable_upper_heater_temperature` = 110
# - `variable_lower_heater_temperature` = 110
# - `variable_timer` = "100"
# - `variable_function_knob` = "Rotary"

class ExtendedSimulator(Simulator): 
    pass