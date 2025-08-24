# The requested command involves the following sequence of features:
# 1. Set the upper element temperature.
#    User Manual: **Temperature Dial for Upper Elements Only** – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie.
#    Feature: "set_upper_element_temperature".
# 2. Set the function dial to Bake.
#    User Manual: **Function Dial** – Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast.
#    Feature: "set_function_dial".
# 3. Set the lower element temperature.
#    User Manual: **Temperature Dial for Lower Elements Only** – Use this dial to set the temperature for Keep Warm, Bake or Toast.
#    Feature: "set_lower_element_temperature".
# 4. Set the timer to 40 minutes.
#    User Manual: **Timer Dial** – This dial must be set to a desired time to begin heating.
#    Feature: "set_timer".

# The current code has accurately modelled all the necessary variables and features described in the user manual for achieving the requested command.
# Therefore, no modifications or new features are required.

# The goal variable values for achieving the command are as follows:
# 1. Set variable_upper_element_temperature to "350".
# 2. Set variable_function_dial to "Toast/Broil" (not "Bake" explicitly, as per user manual, this is the closest option).
# 3. Set variable_lower_element_temperature to "450".
# 4. Set variable_timer to 40.

class ExtendedSimulator(Simulator):
    pass