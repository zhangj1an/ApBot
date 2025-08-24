# The current code accurately models the relevant appliance features needed to achieve the user command:
# Turn on the microwave oven to prepare fish sticks. 
# Set the temperature to 200°C, function dial to 'Convection', selector dial to 'Top & Bottom Heating', and timer to '20'.

# Sequence of features needed to achieve this command:
# 1. Use the "general_cooking" feature to set the temperature, function dial, selector dial, and timer.

# Relevant user manual text:
# "Turn the Temperature dial clockwise to the desired cooking temperature."
# "Turn the Function dial clockwise to the desired operation."
# "Turn the Selector dial clockwise to select top heating, bottom heating or both."
# "Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."

# Feature list name in the given code:
# feature_list["general_cooking"]

# Goal variable values to achieve this command:
# - variable_temperature_dial: "200°C"
# - variable_function_dial: "Convection"
# - variable_selector_dial: "Top & Bottom Heating"
# - variable_timer_dial: "20 minutes"

class ExtendedSimulator(Simulator): 
    pass