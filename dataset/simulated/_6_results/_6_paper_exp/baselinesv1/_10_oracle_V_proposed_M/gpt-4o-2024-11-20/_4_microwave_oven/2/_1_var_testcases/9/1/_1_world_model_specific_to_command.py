# The current code already accurately models the necessary appliance features to achieve the requested command based on the user manual.

# Sequence of features needed to achieve the command:
# 1. Adjust upper element temperature:
#    Turn the upper element temperature dial clockwise to set to "450°F".
#    - Feature name: "adjust_upper_element_temperature" in feature_list.
# 2. Adjust function dial:
#    Turn the function dial clockwise to set to "Toast/Broil".
#    - Feature name: "adjust_function_dial" in feature_list.
# 3. Adjust lower element temperature:
#    Turn the lower element temperature dial clockwise to set to "450°F".
#    - Feature name: "adjust_lower_element_temperature" in feature_list.
# 4. Adjust timer:
#    Turn the timer dial clockwise to set to "30 minutes".
#    - Feature name: "adjust_timer_dial" in feature_list.

# User manual text relevant to these features:
# - **Temperature Dial for Upper Elements Only:** Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie.
# - **Function Dial:** Use this dial to set Convection, Rotisserie, or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast.
# - **Temperature Dial for Lower Elements Only:** Use this dial to set the temperature for Keep Warm, Bake or Toast.
# - **Timer Dial:** This dial must be set to a desired time to begin heating. NOTE: If cook time is less than 20 minutes, you must turn Timer past the 20-minute mark to engage the timer and then back to the desired time.

# Goal variable values to achieve the command:
# - variable_upper_element_temperature: "450"
# - variable_function_dial: "Toast/Broil"
# - variable_lower_element_temperature: "450"
# - variable_timer: 30

class ExtendedSimulator(Simulator): 
    pass