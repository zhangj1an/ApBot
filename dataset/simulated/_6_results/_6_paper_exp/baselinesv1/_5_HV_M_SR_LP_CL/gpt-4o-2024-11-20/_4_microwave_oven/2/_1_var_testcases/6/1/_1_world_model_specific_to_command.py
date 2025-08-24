# The given code already models the appliance features correctly for the user command. 
# The sequence of features needed to achieve the command is as follows:
# 1. Use "set_upper_element_temperature" to set the upper element to 350°F.
#    User manual: "Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
#    Feature List Name: "set_upper_element_temperature"
# 2. Use "set_function_dial" to set the function to "Convection."
#    User manual: "Use this dial to set Convection, Rotisserie or Convection Rotisserie."
#    Feature List Name: "set_function_dial"
# 3. Use "set_lower_element_temperature" to set the lower element to 450°F.
#    User manual: "Use this dial to set the temperature for Keep Warm, Bake or Toast."
#    Feature List Name: "set_lower_element_temperature"
# 4. Use "set_timer" to set the timer to 30 minutes.
#    User manual: "This dial must be set to a desired time to begin heating."
#    Feature List Name: "set_timer"

# Goal variable values to achieve the command:
# variable_upper_element_temperature = "350"
# variable_function_dial = "Convection"
# variable_lower_element_temperature = "450"
# variable_timer = 30

class ExtendedSimulator(Simulator): 
    pass