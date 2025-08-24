# The existing code already captures the required features and variables accurately to meet the user command. 
# The user manual provides the following raw text describing relevant features:
# 1. "Set the upper heating element to desired temperature. We do not recommend using convection when broiling."
# 2. "Turn the function dial to 'Toast/Broil'."
# 3. "Set the lower heating element to desired temperature."
# 4. "Turn the timer knob to 20." 

# These match with the corresponding feature_list names:
# 1. set_upper_element_temperature
# 2. set_function_dial
# 3. set_lower_element_temperature
# 4. set_timer

# Sequence of features needed to achieve this command:
# - "set_upper_element_temperature": Turn the upper element temperature dial to 450°F.
# - "set_function_dial": Turn the function dial to 'Toast/Broil'.
# - "set_lower_element_temperature": Turn the lower element temperature dial to 450°F.
# - "set_timer": Turn the timer dial to 20 minutes.

# Below are the goal variable values to be set:
# 1. variable_upper_element_temperature: set to "450".
# 2. variable_function_dial: set to "Toast/Broil".
# 3. variable_lower_element_temperature: set to "450".
# 4. variable_timer: set to 20.

class ExtendedSimulator(Simulator): 
    pass