# The current code and the user manual both align well to achieve the given user command. 
# Relevant user manual text: 
# 1. "**Temperature Dial for Upper Elements Only** – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# 2. "**Temperature Dial for Lower Elements Only** – Use this dial to set the temperature for Keep Warm, Bake or Toast."
# 3. "**Function Dial** – Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast."
# 4. "**Timer Dial** – This dial must be set to a desired time to begin heating."
#
# Feature list from the code:
# - "set_upper_element_temperature": Models setting the upper element temperature
# - "set_lower_element_temperature": Models setting the lower element temperature
# - "set_function_dial": Models setting the function mode (e.g., Toast/Broil)
# - "set_timer": Models setting the countdown timer

# The features in the code accurately reflect the steps needed for the command. 
# Required features for this command:
# 1. "set_upper_element_temperature" - Turn the upper element temperature to 450°F.
# 2. "set_function_dial" - Set the function mode to "Toast/Broil."
# 3. "set_lower_element_temperature" - Set the lower element temperature to 450°F.
# 4. "set_timer" - Adjust the timer to 20 minutes.

# Goal Variable Values:
# 1. Set `variable_upper_element_temperature` to "450".
# 2. Set `variable_function_dial` to "Toast/Broil".
# 3. Set `variable_lower_element_temperature` to "450".
# 4. Set `variable_timer` to 20.

class ExtendedSimulator(Simulator): 
    pass