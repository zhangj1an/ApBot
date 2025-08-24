# Python comment: The given code already accurately models the relevant appliance features to achieve the user command.
# Here is the sequence of features needed to accomplish the command:
# 1. "adjust_upper_tube_temperature" to set variable_upper_tube_temperature to 110°C.
# 2. "adjust_function_selection" to set variable_function_selection to "upper_and_lower_tubes".
# 3. "adjust_lower_tube_temperature" to set variable_lower_tube_temperature to 70°C.
# 4. "adjust_cooking_time_and_start" to set variable_time_adjustment to 50 minutes and consequently start the appliance.

# Raw User Manual Text:
# - "Upper tube temperature adjustment knob: Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# - "Function selection knob: Select cooking function. ☐ The upper and lower heating tubes heat up at the same time, and the food is evenly heated to achieve a perfect roasting effect."
# - "Lower tube temperature adjustment knob: Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# - "Time adjustment knob: Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
# - "Stay On: When 'Stay On' gear is selected, the electric oven is in a continuous working state and the power indicator light is lit; to end the work, manually turn the time knob back to the 'OFF' gear."

# Feature_list Names in the Given Code:
# - "adjust_upper_tube_temperature"
# - "adjust_function_selection"
# - "adjust_lower_tube_temperature"
# - "adjust_cooking_time_and_start"

# Goal Variable Values to Achieve the User Command:
# - variable_upper_tube_temperature: Set to 110.
# - variable_function_selection: Set to "upper_and_lower_tubes".
# - variable_lower_tube_temperature: Set to 70.
# - variable_time_adjustment: Set to 50.
# - variable_start_running: Set to "on".

class ExtendedSimulator(Simulator): 
    pass