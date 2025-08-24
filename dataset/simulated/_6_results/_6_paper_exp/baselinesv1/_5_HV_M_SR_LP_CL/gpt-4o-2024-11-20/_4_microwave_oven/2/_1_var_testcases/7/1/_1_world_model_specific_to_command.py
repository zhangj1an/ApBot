# The provided code accurately models the appliance features described in the user manual for executing the user command to toast garlic bread. 
# 
# Sequence of features needed to achieve the user command:
# 1. "set_upper_element_temperature": Adjust the upper element temperature to 450°F.
# 2. "set_function_dial": Switch the function dial to "Toast/Broil".
# 3. "set_lower_element_temperature": Adjust the lower element temperature to 450°F.
# 4. "set_timer": Set the timer to 20 minutes.
#
# Relevant user manual text:
# - "Temperature Dial for Upper Elements Only – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# - "Function Dial – Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast."
# - "Temperature Dial for Lower Elements Only – Use this dial to set the temperature for Keep Warm, Bake or Toast."
# - "Timer Dial – This dial must be set to a desired time to begin heating."
# - "Note: If cook time is less than 20 minutes, you must turn Timer past the 20 minute mark to engage the timer then back to desired time."
#
# Feature list names in the code:
# - "set_upper_element_temperature"
# - "set_function_dial"
# - "set_lower_element_temperature"
# - "set_timer"
#
# Goal variable values to achieve this command:
# - variable_upper_element_temperature: "450"
# - variable_function_dial: "Toast/Broil"
# - variable_lower_element_temperature: "450"
# - variable_timer: 20

class ExtendedSimulator(Simulator): 
    pass