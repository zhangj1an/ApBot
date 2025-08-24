# The requested user command can be achieved with the features and variables already modeled in the given code.
# Here is the sequence of actions needed to achieve the user command:

# Sequence of features:
# 1. Set the function knob to "Lower Heater" via feature "set_function_knob".
# 2. Set the upper heater temperature to 70 °C via feature "adjust_upper_heater_temperature".
# 3. Set the lower heater temperature to 70 °C via feature "adjust_lower_heater_temperature".
# 4. Set the timer to 20 minutes via feature "set_timer".

# Relevant user manual quotes:
# - "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# - "Timer: The electric oven beeps when the timer reaches '0'."
# - "Function knob: □ Operates the lower heater □ Operates the upper heater."
# These features have been accurately modeled with:
# - "set_function_knob"
# - "adjust_upper_heater_temperature"
# - "adjust_lower_heater_temperature"
# - "set_timer"

# Goal Variable Values:
# - variable_function_knob = "Lower Heater"
# - variable_upper_heater_temperature = 70
# - variable_lower_heater_temperature = 70
# - variable_timer = "20"

class ExtendedSimulator(Simulator): 
    pass