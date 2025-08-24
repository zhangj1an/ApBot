# The user manual describes operating features and controls in a clear manner that have been properly modeled in the given code. 
# The command "Turn on the microwave to make a quick toast. Set the upper heater temperature to 150 °C, the lower heater temperature to 150 °C, the timer to 60 minutes, and use the upper heater function" matches the modeled feature list as follows:

# Sequence of features needed to achieve this command:
# 1. Set the upper heater temperature: Feature name - "adjust_upper_heater_temperature"
#    User manual quote: "● Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# 2. Set the lower heater temperature: Feature name - "adjust_lower_heater_temperature"
#    User manual quote: "● Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# 3. Set the timer: Feature name - "set_timer"
#    User manual quote: "● Timer: The electric oven beeps when the timer reaches '0' [...]"
# 4. Set the function to upper heater: Feature name - "set_function_knob"
#    User manual quote: "● Function knob: □ Operates the upper heater"

# The goal variable values to achieve the user command are:
# variable_upper_heater_temperature = 150
# variable_lower_heater_temperature = 150
# variable_timer = "60"
# variable_function_knob = "Upper Heater"

# Since the current implementation already contains accurate models for these features, no modifications are needed.

class ExtendedSimulator(Simulator): 
    pass