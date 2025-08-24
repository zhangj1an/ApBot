# The current code is already accurate in modeling the appliance features to achieve the user command.
# Below is the sequence of features and variables needed to achieve the command.

# Sequence of features required to achieve the user command:
# 1. "set_upper_element_temperature" - Set the upper element temperature to 450°F.
# 2. "set_function_dial" - Set the function to "Toast/Broil".
# 3. "set_lower_element_temperature" - Set the lower element temperature to 450°F.
# 4. "set_timer" - Set the timer to 20 minutes.

# Relevant raw user manual text:
# - "Set the upper heating element to desired temperature."
# - "Set the function dial to Toast/Broil."
# - "Set the lower heating element to desired temperature."
# - "Turn the timer knob to your desired cooking time per your recipe."

# Corresponding features in the provided code:
# - Feature name: "set_upper_element_temperature" (variable: variable_upper_element_temperature)
# - Feature name: "set_function_dial" (variable: variable_function_dial)
# - Feature name: "set_lower_element_temperature" (variable: variable_lower_element_temperature)
# - Feature name: "set_timer" (variable: variable_timer)

# Goal variable values to achieve the command:
# - Set variable_upper_element_temperature to "450".
# - Set variable_function_dial to "Toast/Broil".
# - Set variable_lower_element_temperature to "450".
# - Set variable_timer to 20 (continuous value).

class ExtendedSimulator(Simulator): 
    pass