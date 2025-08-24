# The provided code already models the relevant features accurately for the user command. Below is a step-by-step explanation and validation:

# Sequence of features needed to achieve the command:
# 1. **Set the function knob to convection**:
#    - Feature: "set_function_knob"
#    - Actions: ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"]
#    - Variable: "variable_function_knob"
#    - User manual text: "Set the function knob: ⌛ Convection (Lower & upper heater heating)"
#
# 2. **Adjust the upper heater temperature to 190 °C**:
#    - Feature: "adjust_upper_heater_temperature"
#    - Actions: ["turn_upper_temp_dial_clockwise", "turn_upper_temp_dial_anticlockwise"]
#    - Variable: "variable_upper_heater_temperature"
#    - User manual text: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
#
# 3. **Adjust the lower heater temperature to 190 °C**:
#    - Feature: "adjust_lower_heater_temperature"
#    - Actions: ["turn_lower_temp_dial_clockwise", "turn_lower_temp_dial_anticlockwise"]
#    - Variable: "variable_lower_heater_temperature"
#    - User manual text: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
#
# 4. **Set the timer to 40 minutes**:
#    - Feature: "set_timer"
#    - Actions: ["turn_time_dial_clockwise", "turn_time_dial_anticlockwise"]
#    - Variable: "variable_timer"
#    - User manual text: "Timer: The electric oven beeps when the timer reaches '0'. To set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."

# Goal variable values to achieve the command:
# - variable_function_knob: "Convection"
# - variable_upper_heater_temperature: 190
# - variable_lower_heater_temperature: 190
# - variable_timer: "40"

class ExtendedSimulator(Simulator): 
    pass