# The current code accurately models the necessary features needed to operate the appliance in accordance with the user command: "Turn on the microwave and heat up a bowl of soup with the upper element temperature set to 350°F, the function set to Bake, the lower element temperature set to 450°F, and the timer set to 30 minutes."

# Sequence of features needed to achieve the command:
# 1. Feature: "set_upper_element_temperature"
#    Action: Set the upper element temperature to 350°F.
#    Raw User Manual Text: "**HOW TO USE CONTROL PANEL** Temperature Dial for Upper Elements Only – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
#    Feature List Name: "set_upper_element_temperature"
#
# 2. Feature: "set_function_dial"
#    Action: Set the function to "Bake."
#    Raw User Manual Text: "**HOW TO USE CONTROL PANEL** Function Dial – Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast."
#    Feature List Name: "set_function_dial"
#
# 3. Feature: "set_lower_element_temperature"
#    Action: Set the lower element temperature to 450°F.
#    Raw User Manual Text: "**HOW TO USE CONTROL PANEL** Temperature Dial for Lower Elements Only – Use this dial to set the temperature for Keep Warm, Bake or Toast."
#    Feature List Name: "set_lower_element_temperature"
#
# 4. Feature: "set_timer"
#    Action: Set the timer to 30 minutes.
#    Raw User Manual Text: "**HOW TO USE CONTROL PANEL** Timer Dial – This dial must be set to a desired time to begin heating."
#    Feature List Name: "set_timer"

# Goal variable values to achieve the command:
# - Set `variable_upper_element_temperature` to "350".
# - Set `variable_function_dial` to "Toast/Broil" since "Bake" is included in this function setting.
# - Set `variable_lower_element_temperature` to "450".
# - Set `variable_timer` to "30".

class ExtendedSimulator(Simulator): 
    pass