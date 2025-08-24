# The current implementation already models the necessary variables and features to achieve the requested user command. 
# Below is the sequence of features needed to accomplish the given command:

# Sequence of features needed:
# 1. Feature: "general_cooking"
#    - Adjust the temperature to 200°C (variable_temperature_dial)
#    - Set the function dial to 'Convection' (variable_function_dial)
#    - Set the selector dial to 'Top Heating' (variable_selector_dial)
#    - Set the timer to '10 minutes' (variable_timer_dial)

# Relevant user manual text:
# "1. Plug the power cable to the electric mains and switch it ON.
# 2. Turn the Temperature dial clockwise to the desired cooking temperature.
# 3. Turn the Function dial clockwise to the desired operation.
# 4. Turn the Selector dial clockwise to select top heating, bottom heating or both.
# 5. Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."

# Feature List in the code:
# feature_list["general_cooking"]

# The goal variable values to achieve the command are as follows:
goal_variable_values = {
    "variable_temperature_dial": "200°C",  # Set temperature to 200°C
    "variable_function_dial": "Convection",  # Set function to 'Convection'
    "variable_selector_dial": "Top Heating",  # Set selector to 'Top Heating'
    "variable_timer_dial": "10 minutes"  # Set timer to 10 minutes
}

class ExtendedSimulator(Simulator): 
    pass