# The given code correctly models the relevant appliance features from the user manual to achieve the user command.
# Here's how the sequence of features aligns with the required steps:

# User command steps:
# 1. Set the upper heater temperature to 110 °C.
# (Relevant feature: "adjust_upper_heater_temperature")
# 2. Set the lower heater temperature to 110 °C.
# (Relevant feature: "adjust_lower_heater_temperature")
# 3. Set the timer to 20 minutes.
# (Relevant feature: "adjust_timer")
# 4. Use the lower & upper heater function.
# (Relevant feature: "select_function")

# Corresponding raw user manual text:
# - "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# - "Timer: The electric oven beeps when the timer reaches '0'. Tips: to set baking time less than 20 minutes..."
# - "Function knob: □ Operates the lower heater □ Operates the upper heater □ Operates the lower & upper heater at the same time..."

# Relevant features:
# 1. "adjust_upper_heater_temperature": Adjusts the upper heater temperature.
# 2. "adjust_lower_heater_temperature": Adjusts the lower heater temperature.
# 3. "adjust_timer": Adjusts the baking timer.
# 4. "select_function": Selects the heating function.

# The goal variable values to achieve the command are:
# - variable_upper_heater_temperature = 110
# - variable_lower_heater_temperature = 110
# - variable_timer = "20"
# - variable_function_knob = "Lower & Upper Heater"

class ExtendedSimulator(Simulator): 
    pass