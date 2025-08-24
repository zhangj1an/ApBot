# The given code already captures the relevant features required for the user command: 
# "Cook a batch of nachos by setting the upper element temperature to 450°F, function to Toast/Broil, lower element temperature to 450°F, and timer to 20 minutes".
# Here is the relevant user manual text to validate the features:

# User Manual Excerpts:
# 1. "Temperature Dial for Upper Elements Only" – "Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# 2. "Function Dial" – "Use this dial to set Convection, Rotisserie or Convection Rotisserie. This knob does not need to be set for Bake, Broil, Keep Warm, or Toast."
# 3. "Temperature Dial for Lower Elements Only" – "Use this dial to set the temperature for Keep Warm, Bake or Toast."
# 4. "Timer Dial" – "This dial must be set to a desired time to begin heating."
# 5. "NOTE: If cook time is less than 20 minutes, you must turn Timer past the 20 minute mark to engage the timer then back to desired time."

# Validating the feature_list:
# - "set_upper_element_temperature" corresponds to the temperature adjustment for upper elements (feature #1 in user manual).
# - "set_function_dial" corresponds to the function setting that includes Toast/Broil (feature #2 in user manual).
# - "set_lower_element_temperature" corresponds to the temperature adjustment for lower elements (feature #3 in user manual).
# - "set_timer" corresponds to the timer adjustment (feature #4 and #5 in user manual).

# Sequence of Features to Achieve the Command:
# 1. Adjust upper element temperature to 450°F: feature_list["set_upper_element_temperature"].
# 2. Adjust function dial to Toast/Broil: feature_list["set_function_dial"].
# 3. Adjust lower element temperature to 450°F: feature_list["set_lower_element_temperature"].
# 4. Set timer to 20 minutes: feature_list["set_timer"].

# Goal Variable Values to Achieve the Command:
# - variable_upper_element_temperature: "450".
# - variable_function_dial: "Toast/Broil".
# - variable_lower_element_temperature: "450".
# - variable_timer: 20.

class ExtendedSimulator(Simulator): 
    pass