# The current code accurately models the appliance features required to achieve the command.
# Here is a sequence of features to achieve the user command:

# Feature sequence:
# 1. "adjust_upper_tube_temperature"
#    - User manual text: "Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#    - Corresponding feature in the code: "adjust_upper_tube_temperature"
#    - Goal variable value: Set `variable_upper_tube_temperature` to "150".

# 2. "adjust_function_selection"
#    - User manual text: "Select cooking function: upper and lower heating tube are working during this function."
#    - Corresponding feature in the code: "adjust_function_selection"
#    - Goal variable value: Set `variable_function_selection` to "upper_and_lower_tubes".

# 3. "adjust_lower_tube_temperature"
#    - User manual text: "Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#    - Corresponding feature in the code: "adjust_lower_tube_temperature"
#    - Goal variable value: Set `variable_lower_tube_temperature` to "190".

# 4. "adjust_cooking_time_and_start"
#    - User manual text: "Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
#    - Corresponding feature in the code: "adjust_cooking_time_and_start"
#    - Goal variable value: Set `variable_time_adjustment` to "20" and `variable_start_running` to "on".

# Goal Variable Values:
# variable_upper_tube_temperature = 150
# variable_function_selection = "upper_and_lower_tubes"
# variable_lower_tube_temperature = 190
# variable_time_adjustment = 20
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass