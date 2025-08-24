# The given code is accurate and correctly models the appliance's features to achieve the user command.
# The sequence of features needed to achieve the command is:
# 1. "general_cooking" - to set the temperature to 200°C, the function dial to 'Convection',
#    selector dial to 'Top Heating', and timer to '10 minutes'.

# User Manual Raw Text:
# **HOW TO USE**
# 2. Turn the Temperature dial clockwise to the desired cooking temperature.
# 3. Turn the Function dial clockwise to the desired operation.
# 4. Turn the Selector dial clockwise to select top heating, bottom heating, or both.
# 5. Turn the Timer dial clockwise to the desired cooking duration.

# Feature List Name: "general_cooking"

# Goal Variable Values:
# variable_temperature_dial: "200°C"
# variable_function_dial: "Convection"
# variable_selector_dial: "Top Heating"
# variable_timer_dial: "10 minutes"

class ExtendedSimulator(Simulator):
    pass