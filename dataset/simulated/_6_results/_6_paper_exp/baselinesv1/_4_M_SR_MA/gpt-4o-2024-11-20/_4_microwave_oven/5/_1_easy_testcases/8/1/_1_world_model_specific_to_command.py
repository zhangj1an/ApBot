# The given code accurately models the appliance features that are relevant for the provided user command: "Turn on the microwave oven to grill vegetables. Set the temperature to 200°C, function dial to 'Convection', selector dial to 'Top Heating', and timer to '30'."

# Relevant features:
# 1. general_cooking: 
#    - Allows setting the function dial, temperature, selector, and timer.
#    - Feature list name: "general_cooking" in the given code.
#    - User manual references:
#        - "Turn the Temperature dial clockwise to the desired cooking temperature."
#        - "Turn the Function dial clockwise to the desired operation."
#        - "Turn the Selector dial clockwise to select top heating, bottom heating or both."
#        - "Turn the Timer dial clockwise to the desired cooking duration."
#
# The necessary sequence of operations is as follows:
# - Set `variable_temperature_dial` to "200°C".
# - Set `variable_function_dial` to "Convection".
# - Set `variable_selector_dial` to "Top Heating".
# - Set `variable_timer_dial` to "30 minutes".

# Goal variable values to achieve the command:
# variable_function_dial = "Convection"
# variable_temperature_dial = "200°C"
# variable_selector_dial = "Top Heating"
# variable_timer_dial = "30 minutes"

class ExtendedSimulator(Simulator): 
    pass