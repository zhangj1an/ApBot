# The given code accurately models the features and variables required to achieve the user command.
# It has variables for upper element temperature, lower element temperature, function dial, and timer,
# with corresponding features to adjust these parameters.
# The sequence of features needed to achieve the user command is as follows:

# 1. "set_upper_element_temperature": Use actions ["turn_upper_element_temperature_dial_clockwise"] to set to "450".
# 2. "set_lower_element_temperature": Use actions ["turn_lower_element_temperature_dial_clockwise"] to set to "450".
# 3. "set_function_dial": Use actions ["turn_function_dial_clockwise"] to set to "Toast/Broil".
# 4. "set_timer": Use actions ["turn_timer_dial_clockwise"] to set the timer to "20".

# Relevant user manual text:
# - "Set the upper heating element to desired temperature." (for variable_upper_element_temperature)
# - "Set the lower heating element to desired temperature." (for variable_lower_element_temperature)
# - "Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast." (for variable_function_dial)
# - "Turn the timer knob to 20. NOTE: If cook time is less than 20 minutes, you must turn Timer past the 20 minute mark to engage the timer then back to desired time." (for variable_timer)

# Feature list names in the given code:
# - "set_upper_element_temperature"
# - "set_lower_element_temperature"
# - "set_function_dial"
# - "set_timer"

# Goal variable values:
# - variable_upper_element_temperature: "450"
# - variable_lower_element_temperature: "450"
# - variable_function_dial: "Toast/Broil"
# - variable_timer: 20

class ExtendedSimulator(Simulator):
    pass