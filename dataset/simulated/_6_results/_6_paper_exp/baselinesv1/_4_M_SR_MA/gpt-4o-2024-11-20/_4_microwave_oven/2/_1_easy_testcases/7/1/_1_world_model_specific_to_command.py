# The current code accurately models the features and variables as per the user manual.
# Features needed to achieve the command:
# 1. "set_upper_element_temperature" to turn the upper element temperature to 450°F. 
# 2. "set_function_dial" to select the "Toast/Broil" function. 
# 3. "set_lower_element_temperature" to turn the lower element temperature to 450°F.
# 4. "set_timer" to set the timer to 20 minutes. 

# Raw user manual text describing the relevant features:
# 1. Upper element: "Temperature Dial for Upper Elements Only – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# 2. Function dial: "Function Dial – Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast."
# 3. Lower element: "Temperature Dial for Lower Elements Only – Use this dial to set the temperature for Keep Warm, Bake or Toast."
# 4. Timer dial: "Timer Dial – This dial must be set to a desired time to begin heating."

# Corresponding feature names in the given code:
# - set_upper_element_temperature
# - set_function_dial
# - set_lower_element_temperature
# - set_timer

# Goal variable values to achieve this command:
goal_variable_values = {
    "variable_upper_element_temperature": "450",
    "variable_function_dial": "Toast/Broil",
    "variable_lower_element_temperature": "450",
    "variable_timer": 20,
}

class ExtendedSimulator(Simulator):
    pass