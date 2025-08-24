# The given code correctly models the relevant appliance features to achieve the user command. 
# The sequence of features required for achieving the command are:
# 1. Feature: "general_cooking" - Adjust "temperature", "function mode", "heating mode", and "timer".
# 2. Feature: "start" is not required since the timer sets the appliance to start working automatically.

# User manual raw text that describes relevant features:
# 1. "Turn the Temperature dial clockwise to the desired cooking temperature."
# 2. "Turn the Function dial clockwise to the desired operation."
# 3. "Turn the Selector dial clockwise to select top heating, bottom heating or both."
# 4. "Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."
# These match the following feature_list name: "general_cooking".

# Goal variable values to achieve the command:
# - variable_temperature_dial: "150°C"
# - variable_function_dial: "Convection"
# - variable_selector_dial: "Top & Bottom Heating"
# - variable_timer_dial: "10 minutes"

class ExtendedSimulator(Simulator):
    pass