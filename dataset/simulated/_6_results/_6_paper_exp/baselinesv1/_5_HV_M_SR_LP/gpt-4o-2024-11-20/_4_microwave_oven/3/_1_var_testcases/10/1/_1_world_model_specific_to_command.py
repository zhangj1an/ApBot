# User command: Turn on the microwave and adjust the upper tube temperature to 70°C. Select the cooking function as upper and lower heating tube, 
# set the lower tube temperature to 150°C, and set the timer for 50 minutes.

# Python comment: The given code is correct and all necessary features are implemented to achieve this specific command. 
# Following the user manual and the code:

# Sequence of features needed to achieve this command:
# 1. adjust_upper_tube_temperature: Turn the dials to adjust the upper tube temperature to 70°C.
# 2. adjust_function_selection: Turn the dials to select the function as "upper and lower heating tube."
# 3. adjust_lower_tube_temperature: Turn the dials to adjust the lower tube temperature to 150°C.
# 4. adjust_cooking_time_and_start: Turn the dials to set the timer for 50 minutes, during which the cooking starts automatically.

# Relevant raw user manual text:
# - "Upper tube temperature adjustment knob: Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# - "Function selection knob: Select cooking function."
# - "Lower tube temperature adjustment knob: Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# - "Time adjustment knob: Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
# - "Stay On: When 'Stay On' gear is selected, the electric oven is in a continuous working state."

# Feature_list names in the given code:
# - "adjust_upper_tube_temperature"
# - "adjust_function_selection"
# - "adjust_lower_tube_temperature"
# - "adjust_cooking_time_and_start"

# Goal variable values:
# - variable_upper_tube_temperature: 70
# - variable_function_selection: "upper_and_lower_tubes"
# - variable_lower_tube_temperature: 150
# - variable_time_adjustment: 50
# - variable_start_running: "on" (This is set during the time adjustment step automatically.)

class ExtendedSimulator(Simulator): 
    pass