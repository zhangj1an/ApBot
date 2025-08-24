# The current code correctly models the variables and features from the user manual needed to achieve the given command. 
# Below is the sequence of features and actions needed to perform the command:

# Sequence of features:
# 1. Set function knob to "Lower & Upper Heater".
# 2. Adjust the upper heater temperature to 70 °C.
# 3. Adjust the lower heater temperature to 70 °C.
# 4. Set the timer to 80 minutes.

# User Manual Raw Text:
# **Function Knob**:
# □ Operates the lower heater
# □ Operates the upper heater
# □ Operates the lower & upper heater at the same time
# ⌛ Convection (Lower & upper heater heating)
# ↻ Rotary (Upper heater heating) Fermentation (See P. EN19)
#
# **Upper and Lower heaters temperature knobs**:
# Temperature range: 70 °C - 230 °C
#
# **Timer**:
# The electric oven beeps when the timer reaches "0". Tips: to set baking time less than 20 minutes,
# turn up the knob beyond 40 minutes then return to the desired time.

# Feature List:
# 1. The feature "set_function_knob" models the function knob adjustment.
# 2. The feature "adjust_upper_heater_temperature" models the adjustment of the upper heater temperature.
# 3. The feature "adjust_lower_heater_temperature" models the adjustment of the lower heater temperature.
# 4. The feature "set_timer" models the timer setting.

# Goal Variable Values:
# variable_function_knob: "Lower & Upper Heater"
# variable_upper_heater_temperature: 70
# variable_lower_heater_temperature: 70
# variable_timer: "80"

class ExtendedSimulator(Simulator): 
    pass