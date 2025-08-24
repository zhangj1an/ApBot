# The current code accurately models the features required to achieve the given user command.
# Here's the sequence of features needed to achieve the command:

# 1. Adjust the upper tube temperature to 150°C.
#    User manual text corresponding to this step:
#    "Upper tube temperature adjustment knob: Adjust the upper tube temperature. 
#     Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#    Corresponding feature_list name: "adjust_upper_tube_temperature".

# 2. Select the cooking function as "upper and lower heating tubes".
#    User manual text corresponding to this step:
#    "Function selection knob: Select cooking function. 
#     - ☐ The upper and lower heating tube are working during this function."
#    Corresponding feature_list name: "adjust_function_selection".

# 3. Adjust the lower tube temperature to 150°C.
#    User manual text corresponding to this step:
#    "Lower tube temperature adjustment knob: Adjust the lower tube temperature. 
#     Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#    Corresponding feature_list name: "adjust_lower_tube_temperature".

# 4. Set the cooking time to 20 minutes and start the appliance.
#    User manual text corresponding to this step:
#    "Time adjustment knob: Adjust cooking time. 
#     If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, 
#     then turn the time knob back to the desired time position.
#     When 'Stay On' gear is selected, the electric oven is in a continuous working state and the power indicator light is lit;
#     to end the work, manually turn the time knob back to the 'OFF' gear."
#    Corresponding feature_list name: "adjust_cooking_time_and_start".

# Goals for variables:
# variable_upper_tube_temperature = 150
# variable_function_selection = "upper_and_lower_tubes"
# variable_lower_tube_temperature = 150
# variable_time_adjustment = 20
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass