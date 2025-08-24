# Python comments:
# The given code is missing features related to starting or stopping the oven, which is implicitly required as part of operating the oven or performing the requested user command.
# The user manual mentions "unplug the power cord after use" and the lack of an explicit power_on/off button or start_running button might indicate the oven automatically starts after setting all configurations.
# Another aspect to clarify is that "convection" mode differs from "lower & upper heater" mode, but both involve heating, so variable_function_knob is correct as is.

# Based on the user manual and analysis, no changes are strictly needed.
# Steps to achieve the user command:
# 1. Use the feature_list["adjust_upper_heater_temperature"] to set variable_upper_heater_temperature to 70 °C.
# 2. Use the feature_list["adjust_lower_heater_temperature"] to set variable_lower_heater_temperature to 70 °C.
# 3. Use the feature_list["set_timer"] to set variable_timer to "80" minutes.
# 4. Use the feature_list["set_function_knob"] to set variable_function_knob to "Lower & Upper Heater."

# User manual excerpts:
# ● Upper and lower heaters temperature knobs:
#   Temperature range: 70 °C - 230 °C
# ● Timer:
#   The electric oven beeps when the timer reaches "0". Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time. In case of “Stay On” mode, you have to disable the timer manually as the latter cannot be adjusted automatically.
# ● Function knob:
#   □ Operates the lower heater
#   □ Operates the upper heater
#   □ Operates the lower & upper heater at the same time
#   ⌛ Convection (Lower & upper heater heating)

# Related feature_list in the code:
# 1. "adjust_upper_heater_temperature"
# 2. "adjust_lower_heater_temperature"
# 3. "set_timer"
# 4. "set_function_knob"

# Command-related goal variable values:
# variable_upper_heater_temperature = 70
# variable_lower_heater_temperature = 70
# variable_timer = "80"
# variable_function_knob = "Lower & Upper Heater"

class ExtendedSimulator(Simulator): 
    """No changes needed; just refining compatibility."""
    pass