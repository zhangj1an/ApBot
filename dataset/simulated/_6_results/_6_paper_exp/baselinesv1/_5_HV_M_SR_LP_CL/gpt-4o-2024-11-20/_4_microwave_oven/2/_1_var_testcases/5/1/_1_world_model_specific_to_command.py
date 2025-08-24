# The given code correctly models the appliance's features, allowing it to achieve the requested user command.
# Following the user manual instructions, the steps required to achieve this command are:

# 1. Use "set_function_dial" feature to select "Rotisserie".
#    User manual: "**Rotisserie or Convection Rotisserie**: ... Set the function dial to rotisserie or convection rotisserie."
#    Feature: feature_list["set_function_dial"]

# 2. Use "set_upper_element_temperature" feature to set the upper element temperature to 450°F.
#    User manual: "**BROIL**: 1. Set the upper heating element to desired temperature."
#    Feature: feature_list["set_upper_element_temperature"]

# 3. Use "set_lower_element_temperature" feature to set the lower element temperature to 450°F.
#    User manual: "**BAKE**: 1. Set the upper and lower heating elements to 350°F."
#    Feature: feature_list["set_lower_element_temperature"]

# 4. Use "set_timer" feature to set the cook time to 60 minutes.
#    User manual: "Turn the timer knob to your desired cooking time per your recipe."
#    Feature: feature_list["set_timer"]

# The given code already includes these features and actions required to adjust the variables correctly. Thus, no changes are required.

# Variable goals:
# - variable_function_dial: "Rotisserie"
# - variable_upper_element_temperature: "450"
# - variable_lower_element_temperature: "450"
# - variable_timer: 60

class ExtendedSimulator(Simulator): 
    pass