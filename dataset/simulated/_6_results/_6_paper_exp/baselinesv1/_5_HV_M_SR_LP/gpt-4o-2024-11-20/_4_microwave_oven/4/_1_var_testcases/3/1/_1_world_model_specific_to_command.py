# The given code already models the relevant appliance features required for the user command.
# Below is the sequence of features needed to achieve the command using the provided code.

# Sequence of features needed:
# 1. Feature: Set the function knob to "Convection" mode.
#    Raw user manual text: "Function knob:
#                             □ Operates the lower heater
#                             □ Operates the upper heater
#                             □ Operates the lower & upper heater at the same time
#                             ⌛ Convection (Lower & upper heater heating)
#                             ↻ Rotary (Upper heater heating) Fermentation (See P. EN19)"
#    Feature list name: "set_function_knob"
#
# 2. Feature: Set the upper heater temperature to 190 °C.
#    Raw user manual text: "Upper and lower heaters temperature knobs:
#                           Temperature range: 70 °C - 230 °C"
#    Feature list name: "adjust_upper_heater_temperature"
#
# 3. Feature: Set the lower heater temperature to 190 °C.
#    Raw user manual text: Same as above.
#    Feature list name: "adjust_lower_heater_temperature"
#
# 4. Feature: Set the timer to 40 minutes.
#    Raw user manual text: "Timer:
#                           The electric oven beeps when the timer reaches '0'. Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
#    Feature list name: "set_timer"

# Goal variable values to achieve the command:
# 1. Set `variable_function_knob` to "Convection".
# 2. Set `variable_upper_heater_temperature` to 190.
# 3. Set `variable_lower_heater_temperature` to 190.
# 4. Set `variable_timer` to "40".

class ExtendedSimulator(Simulator): 
    pass