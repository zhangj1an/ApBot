# User command checks
# The original code already models the necessary features and variables to achieve the given user command.
# The sequence of features needed to achieve the command is:
# 1. "general_cooking" - to adjust temperature, function, selector mode, and timer as described in the user command.

# The relevant raw user manual text:
# "HOW TO USE:
# 1. Plug the power cable to the electric mains and switch it ON.
# 2. Turn the Temperature dial clockwise to the desired cooking temperature.
# 3. Turn the Function dial clockwise to the desired operation.
# 4. Turn the Selector dial clockwise to select top heating, bottom heating or both.
# 5. Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."

# The feature list name used in the current code: "general_cooking".

# Goal variable values to achieve this command:
# variable_temperature_dial = "150°C"
# variable_function_dial = "Convection"
# variable_selector_dial = "Top & Bottom Heating"
# variable_timer_dial = "20 minutes"

class ExtendedSimulator(Simulator): 
    pass