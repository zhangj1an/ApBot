# The given code does not include any mention of turning on or off the appliance, which is necessary to align it with the user manual. 
# Furthermore, the user manual does not specify any overall power control 
# for the appliance before setting the temperature, function, selector, and timer. 
# This omission, however, is justified since the appliance directly begins operation upon those settings. 
# Hence, the relevant features regarding the user's command are appropriately covered in the given features. 

# The sequence of features needed to achieve this command is:
# 1. Set the temperature to 200°C using the `general_cooking` feature (`variable_temperature_dial`).
# 2. Set the function dial to 'Convection' using the `general_cooking` feature (`variable_function_dial`).
# 3. Set the selector dial to 'Top & Bottom Heating' using the `general_cooking` feature (`variable_selector_dial`).
# 4. Set the timer to '20 minutes' using the `general_cooking` feature (`variable_timer_dial`).

# Relevant user manual raw text (quoted):
# "2. Turn the Temperature dial clockwise to the desired cooking temperature."
# "3. Turn the Function dial clockwise to the desired operation."
# "4. Turn the Selector dial clockwise to select top heating, bottom heating or both."
# "5. Turn the Timer dial clockwise to the desired cooking duration. Heating will commence immediately."

# Feature list in the given code:
# feature_list["general_cooking"] = [
# {"step": 1, "actions": ["turn_temperature_dial_clockwise"], "variable": "variable_temperature_dial"},
# {"step": 2, "actions": ["turn_function_dial_clockwise"], "variable": "variable_function_dial"},
# {"step": 3, "actions": ["turn_selector_dial_clockwise"], "variable": "variable_selector_dial"},
# {"step": 4, "actions": ["turn_timer_dial_clockwise"], "variable": "variable_timer_dial"}
# ]

# Goal variable values for the user's command:
# - variable_temperature_dial: "200°C"
# - variable_function_dial: "Convection"
# - variable_selector_dial: "Top & Bottom Heating"
# - variable_timer_dial: "20 minutes"

class ExtendedSimulator(Simulator):
    pass