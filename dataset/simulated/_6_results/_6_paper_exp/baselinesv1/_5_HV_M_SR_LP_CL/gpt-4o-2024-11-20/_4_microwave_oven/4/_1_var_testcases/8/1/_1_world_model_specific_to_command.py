# The current code correctly models the relevant features of the appliance as described in the user manual.
# Here is the sequence of features and steps needed to achieve the user command:
# 
# 1. "set_function_knob": Turn the dial to "Lower & Upper Heater" function.
#    Raw User Manual Text: "To reach quickly the temperature of 70 °C to 230 °C in the oven, set the function knob: □ Operates the lower & upper heater at the same time selection."
#    Feature List Name: feature_list["set_function_knob"]
# 
# 2. "adjust_upper_heater_temperature": Set the upper heater temperature to 230 °C.
#    Raw User Manual Text: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    Feature List Name: feature_list["adjust_upper_heater_temperature"]
# 
# 3. "adjust_lower_heater_temperature": Set the lower heater temperature to 230 °C.
#    Raw User Manual Text: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    Feature List Name: feature_list["adjust_lower_heater_temperature"]
# 
# 4. "set_timer": Set the timer to 40 minutes.
#    Raw User Manual Text: "The electric oven beeps when the timer reaches 0. Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
#    Feature List Name: feature_list["set_timer"]
# 
# The goal variable values to achieve this command are:
# - Set variable_function_knob to "Lower & Upper Heater".
# - Set variable_upper_heater_temperature to 230 °C.
# - Set variable_lower_heater_temperature to 230 °C.
# - Set variable_timer to "40".

class ExtendedSimulator(Simulator): 
    pass