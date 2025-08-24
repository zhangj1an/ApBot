# The current code models the necessary appliance variables and features correctly, based on the user manual's description. 
# For the user command to toast two slices of bread with the upper element temperature set to 450°F, 
# the function set to Toast/Broil, the lower element temperature set to 450°F, and the timer set to 10 minutes, 
# the following sequence of features will be used:
#
# 1. "set_upper_element_temperature": Adjust the upper element temperature to 450°F.
#      Relevant user manual text: "**Temperature Dial for Upper Elements Only** – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
#
# 2. "set_function_dial": Set the function dial to "Toast/Broil."
#      Relevant user manual text: "**Function Dial** – Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast."
#
# 3. "set_lower_element_temperature": Adjust the lower element temperature to 450°F.
#      Relevant user manual text: "**Temperature Dial for Lower Elements Only** – Use this dial to set the temperature for Keep Warm, Bake or Toast."
#
# 4. "set_timer": Set the timer to 10 minutes.
#      Relevant user manual text: "**Timer Dial** – This dial must be set to a desired time to begin heating. **NOTE:** If cook time is less than 20 minutes, you must turn Timer past the 20-minute mark to engage the timer then back to desired time."

# The feature names in the current code are:
# - "set_upper_element_temperature"
# - "set_function_dial"
# - "set_lower_element_temperature"
# - "set_timer"

# The goal variable values for this user command are:
# - Set variable_upper_element_temperature to "450"
# - Set variable_function_dial to "Toast/Broil"
# - Set variable_lower_element_temperature to "450"
# - Set variable_timer to 10

class ExtendedSimulator(Simulator): 
    pass