# The existing code accurately represents the features needed to accomplish the user command.
# Below is the sequence of features and the corresponding raw user manual text to achieve the command:

# User Command: Turn on the microwave oven to bake cookies. Set the temperature to 150°C, function dial to 'Convection', selector dial to 'Top & Bottom Heating', and timer to '20'.

# Sequence of Features:
# 1. "general_cooking"
#    Raw User Manual Text:
#    - "Turn the Temperature dial clockwise to the desired cooking temperature."
#    - "Turn the Function dial clockwise to the desired operation."
#    - "Turn the Selector dial clockwise to select top heating, bottom heating or both."
#    - "Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."
#    Feature Name in the Code: "general_cooking"

# Goal Variable Values:
# - Set variable_temperature_dial to "150°C"
# - Set variable_function_dial to "Convection"
# - Set variable_selector_dial to "Top & Bottom Heating"
# - Set variable_timer_dial to "20 minutes"

class ExtendedSimulator(Simulator): 
    pass