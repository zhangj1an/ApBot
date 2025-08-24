# The existing code accurately models the relevant appliance features necessary to fulfill the user command. 
# Below is the sequence of features needed to achieve the command:

# Sequence of features:
# 1. Adjust function knob to "Convection" mode:
#    Feature: "set_function_knob"
#    Raw user manual quote: "To reach quickly the temperature of 70 °C to 230 °C in the oven, set the function knob: Convection (Lower & upper heater heating)."
#
# 2. Set upper heater temperature to 190 °C:
#    Feature: "adjust_upper_heater_temperature"
#    Raw user manual quote: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#
# 3. Set lower heater temperature to 190 °C:
#    Feature: "adjust_lower_heater_temperature"
#    Raw user manual quote: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#
# 4. Set the timer to 20 minutes:
#    Feature: "set_timer"
#    Raw user manual quote: "Timer: The electric oven beeps when the timer reaches '0'. Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
#
# Goal variable values:
# - variable_function_knob = "Convection"
# - variable_upper_heater_temperature = 190
# - variable_lower_heater_temperature = 190
# - variable_timer = "20"

class ExtendedSimulator(Simulator): 
    pass