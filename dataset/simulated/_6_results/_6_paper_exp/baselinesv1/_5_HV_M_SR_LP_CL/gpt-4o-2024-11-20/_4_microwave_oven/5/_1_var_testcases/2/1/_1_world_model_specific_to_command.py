# The current code correctly modeled the relevant features and variables required to fulfill the user command:
# - The temperature is adjusted by the feature "general_cooking" with variable "variable_temperature_dial".
# - The function dial is adjusted by the same feature "general_cooking" using variable "variable_function_dial".
# - The selector dial is adjusted by the same feature "general_cooking" using variable "variable_selector_dial".
# - The timer is adjusted by the same feature "general_cooking" using variable "variable_timer_dial".

# The relevant sequences of features and steps to achieve this command are as follows:
# 1. Use "general_cooking" feature.
#    a. Step 1: Adjust temperature to 100°C - Action: "turn_temperature_dial_clockwise".
#    b. Step 2: Set function dial to "Convection" - Action: "turn_function_dial_clockwise".
#    c. Step 3: Set selector dial to "Bottom Heating" - Action: "turn_selector_dial_clockwise".
#    d. Step 4: Adjust timer to "40 minutes" - Action: "turn_timer_dial_clockwise".

# The user manual text that describes the feature:
# - "HOW TO USE" describes the steps to set temperature, function, selector dials, and timer dial to desired values.

# The feature_list name in the given code:
# - "general_cooking"

# The goal variable values to achieve the command:
# - variable_temperature_dial = "100°C"
# - variable_function_dial = "Convection"
# - variable_selector_dial = "Bottom Heating"
# - variable_timer_dial = "40 minutes"

class ExtendedSimulator(Simulator): 
    pass