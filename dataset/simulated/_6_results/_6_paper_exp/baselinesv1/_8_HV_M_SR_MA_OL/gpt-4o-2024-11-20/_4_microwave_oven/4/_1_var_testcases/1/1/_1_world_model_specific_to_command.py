# The user manual describes the following relevant features:
# - Adjusting the function knob to the desired function (lower & upper heater).
# - Adjusting the upper heater temperature and lower heater temperature with separate dials.
# - Setting the timer with a dial knob.
# These are correctly modeled in the given code, and the variables required are also correctly defined.

# Relevant features needed to complete the user command:
# 1. "set_function_knob": Adjust the function knob to "Lower & Upper Heater".
# 2. "adjust_upper_heater_temperature": Set the upper heater temperature to "110 °C".
# 3. "adjust_lower_heater_temperature": Set the lower heater temperature to "110 °C".
# 4. "set_timer": Set the timer to "20 minutes".

# Verified that the user manual clearly describes all the above features which are already modeled in the code.
# Relevant user manual text:
# - Function knob:
#   □ Operates the lower heater
#   □ Operates the upper heater
#   □ Operates the lower & upper heater at the same time
# - Upper and lower heaters temperature knobs:
#   Temperature range: 70 °C - 230 °C
# - Timer:
#   Tips: To set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time.

# Feature list names from the code:
# - "set_function_knob" for selecting the function knob mode.
# - "adjust_upper_heater_temperature" for upper heater temperature setting.
# - "adjust_lower_heater_temperature" for lower heater temperature setting.
# - "set_timer" for adjusting the timer.

# Goal variable values to achieve the user command:
# - variable_function_knob = "Lower & Upper Heater"
# - variable_upper_heater_temperature = 110 (°C)
# - variable_lower_heater_temperature = 110 (°C)
# - variable_timer = "20" (minutes)

class ExtendedSimulator(Simulator): 
    pass