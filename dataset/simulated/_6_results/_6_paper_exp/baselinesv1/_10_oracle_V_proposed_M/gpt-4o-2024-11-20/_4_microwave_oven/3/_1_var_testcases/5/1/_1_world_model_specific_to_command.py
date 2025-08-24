# The given code correctly models the required appliance features as described in the user manual to achieve the user command. 
# Below is the sequence of features needed to execute the command:
# 
# 1. Adjust the upper tube temperature:
#    - Feature: "adjust_upper_tube_temperature"
#    - Raw user manual description:
#      "Upper tube temperature adjustment knob: Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# 
# 2. Select the cooking function:
#    - Feature: "adjust_function_selection"
#    - Raw user manual description:
#      "Function selection knob: Select cooking function..."
#      The feature allows switching between different heating combinations, including "upper and lower heating tube" mode.
# 
# 3. Adjust the lower tube temperature:
#    - Feature: "adjust_lower_tube_temperature"
#    - Raw user manual description:
#      "Lower tube temperature adjustment knob: Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#
# 4. Adjust the time:
#    - Feature: "adjust_time_or_stay_on"
#    - Raw user manual description:
#      "Time adjustment knob: Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
#
# Goal variable values to achieve the command:
# - Set `variable_upper_tube_temperature` to 150 (within adjustable range of 70°C - 230°C).
# - Set `variable_function_selection` to "upper_and_lower_tubes".
# - Set `variable_lower_tube_temperature` to 230 (maximum adjustable temperature).
# - Set `variable_time_adjustment` to 20 minutes.

class ExtendedSimulator(Simulator):
    pass