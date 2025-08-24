# Checking the user command against the user manual and given code:

# Raw user manual text on setting temperature and selecting functions:
# **Upper tube temperature adjustment knob**
# Adjust the upper tube temperature
# Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C.

# **Function selection knob**
# Select cooking function
# - ☐ The lower heating tube are working during this function.
# - ☐ The upper heating tube are working during this cycle.
# - ☐ The upper and lower heating tube are working during this function.
# - ☐ The upper and lower heating tube, along with the motor fan are working.
# - ☐ The upper heating tube, along with the Rotisserie Motor are working.

# **Lower tube temperature adjustment knob**
# Adjust the lower tube temperature
# Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C.

# **Time adjustment knob**
# Adjust cooking time
# If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position.

# In the given code:
# - variable_upper_tube_temperature, variable_function_selection, variable_lower_tube_temperature, variable_time_adjustment, and variable_start_running are accurately modeled.
# - The features needed for the command are modeled:
#   - "adjust_upper_tube_temperature" for setting upper tube temperature.
#   - "adjust_function_selection" for selecting the cooking function.
#   - "adjust_lower_tube_temperature" for setting lower tube temperature.
#   - "adjust_cooking_time_and_start" for setting the cooking time and starting.

# The given code is already accurate for implementing the user command.

# Sequence of features required to achieve the command:
# 1. "adjust_upper_tube_temperature"
# 2. "adjust_function_selection"
# 3. "adjust_lower_tube_temperature"
# 4. "adjust_cooking_time_and_start"

# Goal variable values:
# - Set variable_upper_tube_temperature to 150°C.
# - Set variable_function_selection to "upper_and_lower_tubes".
# - Set variable_lower_tube_temperature to 190°C.
# - Set variable_time_adjustment to 30 minutes and variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass