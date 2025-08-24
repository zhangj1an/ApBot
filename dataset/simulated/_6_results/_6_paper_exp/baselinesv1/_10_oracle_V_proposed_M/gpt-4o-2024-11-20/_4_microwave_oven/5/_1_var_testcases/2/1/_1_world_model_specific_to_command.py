# The current implementation accurately models the appliance features required to achieve the described user command. 
# The sequence of features needed to achieve the user command is as follows:

# Sequence of Features:
# 1. "adjust_temperature_dial" to set the temperature to 100°C.
# 2. "adjust_function_dial" to set the function dial to 'Convection'.
# 3. "adjust_selector_dial" to set the selector dial to 'Bottom Heating'.
# 4. "adjust_timer_dial" to set the timer to '40 minutes'.

# Relevant User Manual Text:
# - "Turn the Temperature dial clockwise to the desired cooking temperature."
# - "Turn the Function dial clockwise to the desired operation."
# - "Turn the Selector dial clockwise to select top heating, bottom heating or both."
# - "Turn the Timer dial clockwise to the desired cooking duration."

# Relevant feature_list names in the provided code:
# - "adjust_temperature_dial"
# - "adjust_function_dial"
# - "adjust_selector_dial"
# - "adjust_timer_dial"

# Goal Variable Values to Achieve the Command:
# - `variable_temperature_dial`: "100°C"
# - `variable_function_dial`: "Convection"
# - `variable_selector_dial`: "Bottom Heating"
# - `variable_timer_dial`: "40 minutes"

class ExtendedSimulator(Simulator):
    pass