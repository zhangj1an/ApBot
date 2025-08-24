# The user manual provided is accurately modeled in the given code. The sequence of features needed to achieve the command
# "Turn on the microwave oven to keep dinner warm. Set the temperature to 100°C, function dial to 'Convection', selector dial to 'Bottom Heating', and timer to '40'."
# is as follows:

# 1. "general_cooking" feature is used to set all the configurations (temperature, function, selector, and timer).
# 2. The goal variable values after execution should be:
#    - variable_temperature_dial: "100°C"
#    - variable_function_dial: "Convection"
#    - variable_selector_dial: "Bottom Heating"
#    - variable_timer_dial: "40 minutes"

# Quoting relevant user manual text to ensure features are implemented correctly:
# User manual explains:
# - "Turn the Temperature dial clockwise to the desired cooking temperature."
# - "Turn the Function dial clockwise to the desired operation."
# - "Turn the Selector dial clockwise to select top heating, bottom heating, or both."
# - "Turn the Timer dial clockwise to the desired cooking duration."

class ExtendedSimulator(Simulator): 
    pass