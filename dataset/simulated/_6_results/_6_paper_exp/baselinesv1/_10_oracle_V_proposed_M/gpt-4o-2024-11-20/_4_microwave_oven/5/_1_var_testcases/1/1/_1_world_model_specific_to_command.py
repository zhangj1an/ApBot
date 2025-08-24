# The current implementation of Simulator correctly models the variables and features required for the user command.
# The following sequence of features and their corresponding variables are needed to achieve the user command:
#
# Sequence of features:
# 1. Adjust the function dial to "Convection" (`feature_list["adjust_function_dial"]`).
# 2. Adjust the temperature dial to "150°C" (`feature_list["adjust_temperature_dial"]`).
# 3. Adjust the selector dial to "Top & Bottom Heating" (`feature_list["adjust_selector_dial"]`).
# 4. Adjust the timer dial to "20 minutes" (`feature_list["adjust_timer_dial"]`).
#
# Relevant raw user manual text:
# - Function Dial: "Turn the Function dial clockwise to the desired operation."
# - Temperature Dial: "Turn the Temperature dial clockwise to the desired cooking temperature."
# - Selector Dial: "Turn the Selector dial clockwise to select top heating, bottom heating or both."
# - Timer Dial: "Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."
#
# Given feature_list names:
# - adjust_function_dial
# - adjust_temperature_dial
# - adjust_selector_dial
# - adjust_timer_dial
#
# Goal variable values to achieve the user command:
# - variable_function_dial = "Convection"
# - variable_temperature_dial = "150°C"
# - variable_selector_dial = "Top & Bottom Heating"
# - variable_timer_dial = "20 minutes"

class ExtendedSimulator(Simulator):
    pass