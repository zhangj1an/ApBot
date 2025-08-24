# The current code does not include functionality to start the appliance. 
# According to the user manual, there is no explicitly stated 'power on/off' button or toggle switch to start the appliance. 
# Therefore, we can't directly model this action as 'power on' without an associated action and variable.

# Here is the sequence of features already implemented in the code and relevant to the user command:
# - Adjust the function dial to 'Convection' using: "adjust_function_dial"
# - Adjust the temperature dial to '200°C' using: "adjust_temperature_dial"
# - Adjust the selector dial to 'Top & Bottom Heating' using: "adjust_selector_dial"
# - Adjust the timer to '20' using: "adjust_timer_dial"

# Raw user manual text for relevant actions:
# - "**Turn the Function dial clockwise to the desired operation.**"
# - "**Turn the Temperature dial clockwise to the desired cooking temperature.**"
# - "**Turn the Selector dial clockwise to select top heating, bottom heating, or both.**"
# - "**Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately.**"

# These features are correctly described in the given feature_list:
# - "adjust_function_dial"
# - "adjust_temperature_dial"
# - "adjust_selector_dial"
# - "adjust_timer_dial"

# Goal variable values to achieve the user command:
# - variable_function_dial: "Convection"
# - variable_temperature_dial: "200°C"
# - variable_selector_dial: "Top & Bottom Heating"
# - variable_timer_dial: "20 minutes"

class ExtendedSimulator(Simulator):
    pass