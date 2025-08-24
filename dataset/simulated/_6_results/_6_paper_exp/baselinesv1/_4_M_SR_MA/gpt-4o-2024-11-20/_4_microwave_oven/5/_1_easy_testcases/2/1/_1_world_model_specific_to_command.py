# The user manual indicates the procedure involves setting temperature, function dial, selector dial, and timer. 
# The current implementation correctly models these steps and includes the necessary features: `general_cooking`
# User command: Turn on the microwave oven to keep dinner warm. Set the temperature to 100°C, function dial to 'Convection',
# selector dial to 'Bottom Heating', and timer to '40'.

# According to the code, the relevant feature is:
# feature_list["general_cooking"], with the steps:
# step 1: adjust `variable_temperature_dial`
# step 2: adjust `variable_function_dial`
# step 3: adjust `variable_selector_dial`
# step 4: adjust `variable_timer_dial`

# User manual quotes:
# "2. Turn the Temperature dial clockwise to the desired cooking temperature."
# "3. Turn the Function dial clockwise to the desired operation."
# "4. Turn the Selector dial clockwise to select top heating, bottom heating or both."
# "5. Turn the Timer dial clockwise to the desired cooking duration."

# The given implementation is accurate and models the relevant steps, variables, and actions for the user command.

# Goal variable values to achieve the command:
# `variable_temperature_dial`: "100°C"
# `variable_function_dial`: "Convection"
# `variable_selector_dial`: "Bottom Heating"
# `variable_timer_dial`: "40 minutes"

class ExtendedSimulator(Simulator): 
    pass