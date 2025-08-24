# The provided code models the relevant appliance features accurately for the user command. 
# The sequence of features required to achieve the command is as follows:

# Feature 1: "set_upper_element_temperature"
# Raw text: "**BROIL**: Set the upper heating element to desired temperature. We do not recommend using convection when broiling."
# Feature name: "set_upper_element_temperature" in the given code.

# Feature 2: "set_function_dial"
# Raw text: "**BROIL**: Indicates the function set to Toast/Broil."
# Feature name: "set_function_dial" in the given code.

# Feature 3: "set_lower_element_temperature"
# Raw text: "**BROIL**: Set the lower heating element to the desired temperature when broiling if necessary."
# Feature name: "set_lower_element_temperature" in the given code.

# Feature 4: "set_timer"
# Raw text: "Turn the timer knob to 20. **NOTE**: If cook time is less than 20 minutes, you must turn Timer past the 20-minute mark to engage the timer then back to desired time."
# Feature name: "set_timer" in the given code.

# Goal Variable Values:
# 1. Set `variable_upper_element_temperature` to "450".
# 2. Set `variable_function_dial` to "Toast/Broil".
# 3. Set `variable_lower_element_temperature` to "450".
# 4. Set `variable_timer` to "30" minutes.

class ExtendedSimulator(Simulator): 
    pass