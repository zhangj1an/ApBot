# The given code already accurately models the appliance feature required to achieve the user command. 
# Here is the sequence of features and their corresponding variable values to fulfill the task:

# Sequence of Features Needed:
# 1. Use feature "adjust_upper_element_temperature" to set the upper element temperature to 450°F.
# 2. Use feature "adjust_function_dial" to set the function to "Toast/Broil".
# 3. Use feature "adjust_lower_element_temperature" to set the lower element temperature to 450°F.
# 4. Use feature "adjust_timer_dial" to set the timer to 20 minutes.

# Relevant User Manual Text:
# - To set temperature: **Temperature Dial for Upper/Lower Elements Only** – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie.
# - Function Dial: **Function Dial** – Use this dial to set Convection, Rotisserie or Convection Rotisserie.
# - Timer: **Timer Dial** – This dial must be set to a desired time to begin heating.
#   **NOTE:** If cook time is less than 20 minutes, you must turn Timer past the 20 minute mark to engage the timer then back to desired time.

# Feature List Name in Code:
# - "adjust_upper_element_temperature"
# - "adjust_function_dial"
# - "adjust_lower_element_temperature"
# - "adjust_timer_dial"

# Goal Variable Values:
# - variable_upper_element_temperature: "450"
# - variable_function_dial: "Toast/Broil"
# - variable_lower_element_temperature: "450"
# - variable_timer: 20

class ExtendedSimulator(Simulator): 
    pass