# The given code models the relevant appliance feature accurately to achieve the user command.
# Sequence of Features Needed:
# 1. "set_upper_element_temperature" (to set the upper element to 350°F)
# 2. "set_lower_element_temperature" (to set the lower element to 450°F)
# 3. "set_function_dial" (to set the function to "Convection")
# 4. "set_timer" (to set the timer to 30 minutes)

# Quoted User Manual Text Relevant to Features:
# - Temperature Dial for Upper Elements Only – "Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# - Temperature Dial for Lower Elements Only – "Use this dial to set the temperature for Keep Warm, Bake or Toast."
# - Function Dial – "Use this dial to set Convection, Rotisserie or Convection Rotisserie."
# - Timer Dial – "This dial must be set to a desired time to begin heating."

# Feature List Names in Code:
# - "set_upper_element_temperature"
# - "set_lower_element_temperature"
# - "set_function_dial"
# - "set_timer"

# Goal Variable Values:
# - Set `variable_upper_element_temperature` to "350".
# - Set `variable_lower_element_temperature` to "450".
# - Set `variable_function_dial` to "Convection".
# - Set `variable_timer` to 30 (in minutes).

class ExtendedSimulator(Simulator): 
    pass