# The current code correctly models the appliance features needed to achieve this command. 
# Here's the logical sequence of features to execute the command:
# 1. Adjust the function dial: Turn it to 'Convection' using features from "adjust_function_dial".
# 2. Adjust the temperature dial: Turn it to '150°C' using features from "adjust_temperature_dial".
# 3. Adjust the selector dial: Turn it to 'Bottom Heating' using features from "adjust_selector_dial".
# 4. Adjust the timer dial: Turn it to '30 minutes' using features from "adjust_timer_dial".
#
# User Manual Relevant Text:
# - "Turn the Function dial clockwise to the desired operation."
# - "Turn the Temperature dial clockwise to the desired cooking temperature."
# - "Turn the Selector dial clockwise to select top heating, bottom heating, or both."
# - "Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."
#
# Relevant Feature List Names in the Given Code:
# - "adjust_function_dial"
# - "adjust_temperature_dial"
# - "adjust_selector_dial"
# - "adjust_timer_dial"
#
# Goal Variable Values:
# - variable_function_dial: "Convection"
# - variable_temperature_dial: "150°C"
# - variable_selector_dial: "Bottom Heating"
# - variable_timer_dial: "30 minutes"

class ExtendedSimulator(Simulator): 
    pass