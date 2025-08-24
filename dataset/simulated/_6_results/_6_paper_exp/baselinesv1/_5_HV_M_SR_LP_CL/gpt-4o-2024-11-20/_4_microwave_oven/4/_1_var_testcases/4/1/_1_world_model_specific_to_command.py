# The given code correctly models the relevant appliance features needed to achieve the command.
# Here is the sequence of features required based on the user manual and the given feature_list:
# 
# Sequence of features:
# 1. Feature: "set_function_knob"
#    - **Action(s):** Turn the function dial to use the rotary function.
#    - **User Manual Text:**
#      "Function knob: ↻ Rotary (Upper heater heating) Fermentation."
#    - **Feature Code Name:** `set_function_knob`
#
# 2. Feature: "adjust_upper_heater_temperature"
#    - **Action(s):** Turn the upper temperature dial to set it to 110 °C.
#    - **User Manual Text:**
#      "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    - **Feature Code Name:** `adjust_upper_heater_temperature`
#
# 3. Feature: "adjust_lower_heater_temperature"
#    - **Action(s):** Turn the lower temperature dial to set it to 110 °C.
#    - **User Manual Text:**
#      "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    - **Feature Code Name:** `adjust_lower_heater_temperature`
#
# 4. Feature: "set_timer"
#    - **Action(s):** Turn the timer dial to 100 minutes.
#    - **User Manual Text:**
#       "Timer: The electric oven beeps when the timer reaches '0'. To set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
#    - **Feature Code Name:** `set_timer`
#
# Goal variable values:
# - `variable_function_knob`: "Rotary"
# - `variable_upper_heater_temperature`: 110
# - `variable_lower_heater_temperature`: 110
# - `variable_timer`: "100"

class ExtendedSimulator(Simulator): 
    pass