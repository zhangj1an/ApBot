# The given code accurately models the necessary appliance features required to achieve the user command. 
# Below is the sequence of features needed to execute the command and achieve the desired result.
# 
# Relevant user manual text and corresponding feature descriptions:
#
# 1. Adjust upper element temperature: 
#    User manual: 
#    "Set the upper heating element to desired temperature. We do not recommend using convection when broiling."
#    Feature list name: "set_upper_element_temperature"
#    Action required: "turn_upper_element_temperature_dial_clockwise" to set the upper element temperature to "450".
#
# 2. Adjust the function dial to "Toast/Broil":
#    User manual: 
#    "Set the function dial to Toast/Broil."
#    Feature list name: "set_function_dial"
#    Action required: "turn_function_dial_clockwise" to set the function dial to "Toast/Broil".
#
# 3. Adjust lower element temperature:
#    User manual:
#    "Set the lower heating element to desired temperature."
#    Feature list name: "set_lower_element_temperature"
#    Action required: "turn_lower_element_temperature_dial_clockwise" to set the lower element temperature to "450".
#
# 4. Set the timer:
#    User manual:
#    "Turn the timer knob to the desired cooking time per your recipe. NOTE: If cook time is less than 20 minutes, 
#     you must turn Timer past the 20 minute mark to engage the timer then back to desired time."
#    Feature list name: "set_timer"
#    Action required: "turn_timer_dial_clockwise" to set the timer to "20" minutes.
#
# Goals to achieve the user command:
# - Set `variable_upper_element_temperature` to "450".
# - Set `variable_function_dial` to "Toast/Broil".
# - Set `variable_lower_element_temperature` to "450".
# - Set `variable_timer` to 20.

class ExtendedSimulator(Simulator): 
    pass