# Based on the user manual and the user command, the given code already accurately models the necessary appliance features.
# Below is the relevant sequence of features described for the user command, the raw user manual text, and feature_list names.

# Sequence of features:
# 1. Adjust upper tube temperature feature:
#    - Feature name: "adjust_upper_tube_temperature"
#    - User command: Set the upper tube temperature to 150°C
# 2. Adjust function selection feature:
#    - Feature name: "adjust_function_selection"
#    - User command: Select the function: upper and lower heating tube.
# 3. Adjust lower tube temperature feature:
#    - Feature name: "adjust_lower_tube_temperature"
#    - User command: Set the lower tube temperature to 230°C.
# 4. Adjust the cooking time and start running:
#    - Feature name: "adjust_cooking_time_and_start"
#    - User command: Set the cooking time to 20 minutes, turning on the appliance.

# Raw user manual text describing the relevant features:
# **Upper tube temperature adjustment knob**: "Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# **Function selection knob**: "Select cooking function: Upper heating tube, lower heating tube, upper and lower heating tubes, and so on."
# **Lower tube temperature adjustment knob**: "Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# **Time adjustment knob**: "Adjust the cooking time. If the cooking time is less than 10 minutes, turn the time knob back to the desired time position."
# **Stay On**: "When 'Stay On' gear is selected, the electric oven is in a continuous working state and the power indicator light is lit."

# Features in the given code:
# 1. Feature name: "adjust_upper_tube_temperature"
# 2. Feature name: "adjust_function_selection"
# 3. Feature name: "adjust_lower_tube_temperature"
# 4. Feature name: "adjust_cooking_time_and_start"

# Goal variable values:
# Set `variable_upper_tube_temperature` to `150°C`.
# Set `variable_function_selection` to `upper_and_lower_tubes`.
# Set `variable_lower_tube_temperature` to `230°C`.
# Set `variable_time_adjustment` to `20 minutes` and `variable_start_running` to `on`.

class ExtendedSimulator(Simulator): 
    pass