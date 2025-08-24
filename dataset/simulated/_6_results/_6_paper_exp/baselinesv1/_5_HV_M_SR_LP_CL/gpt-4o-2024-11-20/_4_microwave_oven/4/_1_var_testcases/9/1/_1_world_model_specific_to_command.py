# Python comments explaining the requested user command:
# 
# To achieve the user command: "Turn on the microwave to warm tortillas. Set the upper heater temperature to 110 °C, the lower heater temperature to 110 °C, the timer to 60 minutes, and use the lower heater function."
# 
# Below is the sequence of features needed based on the current implementation:
# 
# 1. Set the function knob to "Lower Heater" using the feature: feature_list["set_function_knob"].
#    - User Manual Text: “Function knob: □ Operates the lower heater.”
# 
# 2. Adjust the upper heater temperature to 110 °C using the feature: feature_list["adjust_upper_heater_temperature"].
#    - User Manual Text: “Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C.”
# 
# 3. Adjust the lower heater temperature to 110 °C using the feature: feature_list["adjust_lower_heater_temperature"].
#    - User Manual Text: Same as above.
# 
# 4. Set the timer to 60 minutes using the feature: feature_list["set_timer"].
#    - User Manual Text: “Timer: Select desired baking time.”
# 
# Assuming the current implementation is correct as per the user manual descriptions, no additional variables or features need to be created or modified. 
#
# The goal variable values are as follows:
# - variable_function_knob = "Lower Heater"
# - variable_upper_heater_temperature = 110
# - variable_lower_heater_temperature = 110
# - variable_timer = "60"

class ExtendedSimulator(Simulator): 
    pass