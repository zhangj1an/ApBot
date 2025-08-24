# The given code accurately models the relevant appliance features described in the user manual
# to achieve the user command. Here's how the relevant sequence of features and steps align:

# Sequence of features needed to achieve this command:
# 1. Feature: adjust_upper_tube_temperature
#    Step: Use action "turn_upper_tube_temperature_adjustment_dial_clockwise" or "turn_upper_tube_temperature_adjustment_dial_anticlockwise" to set "variable_upper_tube_temperature" to 150°C.
#    User manual text: "**Upper tube temperature adjustment knob** - Adjust the upper tube temperature. The adjustable temperature range is 70°C - 230°C."
#    Feature name in the given code: "adjust_upper_tube_temperature".

# 2. Feature: adjust_function_selection
#    Step: Use action "turn_function_selection_dial_clockwise" or "turn_function_selection_dial_anticlockwise" to set "variable_function_selection" to "upper_and_lower_tubes".
#    User manual text: "**Function selection knob** - Select cooking function. Options include: lower heating tube, upper heating tube, upper and lower heating tube, etc."
#    Feature name in the given code: "adjust_function_selection".

# 3. Feature: adjust_lower_tube_temperature
#    Step: Use action "turn_lower_tube_temperature_adjustment_dial_clockwise" or "turn_lower_tube_temperature_adjustment_dial_anticlockwise" to set "variable_lower_tube_temperature" to 230°C.
#    User manual text: "**Lower tube temperature adjustment knob** - Adjust the lower tube temperature. The adjustable range is 70°C - 230°C."
#    Feature name in the given code: "adjust_lower_tube_temperature".

# 4. Feature: adjust_cooking_time_and_start
#    Step: Use action "turn_time_adjustment_dial_clockwise" or "turn_time_adjustment_dial_anticlockwise" to set "variable_time_adjustment" to 20 minutes.
#    User manual text: "**Time adjustment knob** - Adjust cooking time. If the cooking time is less than 10 minutes, turn the knob to more than 10 minutes, and then turn back to the desired time."
#    Feature name in the given code: "adjust_cooking_time_and_start".

# Goal variable values to achieve this command:
# - Set "variable_upper_tube_temperature" to 150.
# - Set "variable_function_selection" to "upper_and_lower_tubes".
# - Set "variable_lower_tube_temperature" to 230.
# - Set "variable_time_adjustment" to 20.
# - Set "variable_start_running" to "on".

class ExtendedSimulator(Simulator):
    pass