# The provided code models relevant features to achieve the user command. Specifically:
# - Adjusting temperature, function dial, selector dial, and timer are correctly covered by the following features:
#   - "general_cooking" allows setting the temperature to 200°C, function dial to 'Convection', selector dial to 'Top Heating', and timer to '10'.
#
# Sequence of features needed to achieve this command:
# - Use "general_cooking" feature to adjust all required dials and settings.
#
# Relevant user manual text that describes these features:
# - **HOW TO USE**:
#   2. Turn the Temperature dial clockwise to the desired cooking temperature.
#   3. Turn the Function dial clockwise to the desired operation.
#   4. Turn the Selector dial clockwise to select top heating, bottom heating or both.
#   5. Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately.
#
# Corresponding feature in the given code:
# - feature_list["general_cooking"]

# Goal variable values to achieve this command:
# - variable_temperature_dial set to "200°C"
# - variable_function_dial set to "Convection"
# - variable_selector_dial set to "Top Heating"
# - variable_timer_dial set to "10 minutes"

class ExtendedSimulator(Simulator): 
    pass