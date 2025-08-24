# The command is to prepare cookies by configuring element temperatures, function mode, and timer. 
# The described steps in the user manual are already modeled in the given Simulator.
# Below is the step-by-step mapping of user command to features and variables:

# 1. Set the upper element temperature to 350°F:
#    - Feature: "adjust_upper_element_temperature"
#    - User manual text: "Temperature Dial for Upper Elements Only – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie." 
#      Relevant feature list: "adjust_upper_element_temperature"

# 2. Set the function to Bake:
#    - Feature: "adjust_function_dial"
#    - User manual text: "Function Dial – Use this dial to set Convection, Rotisserie or Convection Rotisserie."
#      Relevant feature list: "adjust_function_dial"

# 3. Set the lower element temperature to 450°F:
#    - Feature: "adjust_lower_element_temperature"
#    - User manual text: "Temperature Dial for Lower Elements Only – Use this dial to set the temperature for Keep Warm, Bake or Toast."
#      Relevant feature list: "adjust_lower_element_temperature"

# 4. Set the timer for 40 minutes:
#    - Feature: "adjust_timer_dial"
#    - User manual text: "Timer Dial – This dial must be set to a desired time to begin heating."
#      Relevant feature list: "adjust_timer_dial"

# The current implementation correctly models all the required features for the command.

# The goal variable values to achieve this command are:
# variable_upper_element_temperature = "350"
# variable_function_dial = "Toast/Broil" (function is assumed as "Bake" under this mode)
# variable_lower_element_temperature = "450"
# variable_timer = 40

class ExtendedSimulator(Simulator): 
    pass