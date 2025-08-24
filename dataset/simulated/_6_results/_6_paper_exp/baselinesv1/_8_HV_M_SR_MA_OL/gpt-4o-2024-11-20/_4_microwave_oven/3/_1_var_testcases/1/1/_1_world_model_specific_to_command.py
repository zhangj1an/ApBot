# The given code already accurately models the necessary appliance features to achieve the user command.
# Below is the sequence of features and variable values required to execute the command.

# Sequence of features needed:
# 1. "adjust_upper_tube_temperature": Turn the upper tube temperature adjustment dial to set the upper tube temperature to 150°C.
# 2. "adjust_function_selection": Turn the function selection dial to set the cooking function to "upper_and_lower_tubes".
# 3. "adjust_lower_tube_temperature": Turn the lower tube temperature adjustment dial to set the lower tube temperature to 150°C.
# 4. "adjust_cooking_time_and_start": Turn the time adjustment dial to set the cooking time to 20 minutes, which automatically starts the oven.

# Relevant user manual text for features:
# - **Upper tube temperature adjustment knob**: "Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# - **Function selection knob**: "Select cooking function..."
# - **Lower tube temperature adjustment knob**: "Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# - **Time adjustment knob**: "Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position. When 'Stay On' gear is selected, the electric oven is in a continuous working state..."

# Corresponding feature_list names from the code:
# 1. "adjust_upper_tube_temperature"
# 2. "adjust_function_selection"
# 3. "adjust_lower_tube_temperature"
# 4. "adjust_cooking_time_and_start"

# Goal variable values to achieve the command:
variable_upper_tube_temperature.set_current_value(150)
variable_function_selection.set_current_value("upper_and_lower_tubes")
variable_lower_tube_temperature.set_current_value(150)
variable_time_adjustment.set_current_value(20)
variable_start_running.set_current_value("on")

class ExtendedSimulator(Simulator): 
    pass