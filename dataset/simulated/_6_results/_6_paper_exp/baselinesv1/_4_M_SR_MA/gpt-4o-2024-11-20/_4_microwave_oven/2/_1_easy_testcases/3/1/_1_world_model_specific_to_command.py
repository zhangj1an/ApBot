# The current implementation accurately models the relevant appliance features necessary for this user command.
# Below is the sequence of features needed to achieve the command:
# 1. Adjust the upper element temperature using the feature "set_upper_element_temperature".
# 2. Adjust the function dial using the feature "set_function_dial".
# 3. Adjust the lower element temperature using the feature "set_lower_element_temperature".
# 4. Adjust the timer using the feature "set_timer".

# Relevant user manual excerpts:
# 1. "Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# 2. "Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast."
# 3. "Use this dial to set the temperature for Keep Warm, Bake or Toast."
# 4. "This dial must be set to a desired time to begin heating."
# 
# Corresponding feature list in the code:
# - "set_upper_element_temperature"
# - "set_function_dial"
# - "set_lower_element_temperature"
# - "set_timer"

# Goal variable values:
# - Set variable_upper_element_temperature to "350".
# - Set variable_function_dial to "OFF" (since Bake does not require the function dial to be adjusted).
# - Set variable_lower_element_temperature to "350".
# - Set variable_timer to 40.

class ExtendedSimulator(Simulator):
    pass