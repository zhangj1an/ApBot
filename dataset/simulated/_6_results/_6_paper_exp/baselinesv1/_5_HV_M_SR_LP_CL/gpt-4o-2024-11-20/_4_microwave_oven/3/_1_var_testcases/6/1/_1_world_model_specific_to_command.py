# The provided code already accurately and completely models the relevant appliance features needed to achieve the requested user command.
# Sequence of features needed to achieve this command:
# 1. Feature: "adjust_upper_tube_temperature"
#    - Action: turn_upper_tube_temperature_adjustment_dial_clockwise or turn_upper_tube_temperature_adjustment_dial_anticlockwise
#    - User Manual Reference: "Adjust the upper tube temperature. The adjustable temperature range is 70°C - 230°C."
#    - Corresponding Feature in Code: "adjust_upper_tube_temperature"
#
# 2. Feature: "adjust_function_selection"
#    - Action: turn_function_selection_dial_clockwise or turn_function_selection_dial_anticlockwise
#    - User Manual Reference: "Select cooking function." (e.g., upper and lower heating tubes)
#    - Corresponding Feature in Code: "adjust_function_selection"
#
# 3. Feature: "adjust_lower_tube_temperature"
#    - Action: turn_lower_tube_temperature_adjustment_dial_clockwise or turn_lower_tube_temperature_adjustment_dial_anticlockwise
#    - User Manual Reference: "Adjust the lower tube temperature. The adjustable temperature range is 70°C - 230°C."
#    - Corresponding Feature in Code: "adjust_lower_tube_temperature"
#
# 4. Feature: "adjust_cooking_time_and_start"
#    - Action: turn_time_adjustment_dial_clockwise or turn_time_adjustment_dial_anticlockwise
#    - User Manual Reference: "Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
#    - Corresponding Feature in Code: "adjust_cooking_time_and_start"

# Goal Variable Values to Achieve the Command:
# - Set variable_upper_tube_temperature to 150°C.
# - Set variable_function_selection to "upper_and_lower_tubes".
# - Set variable_lower_tube_temperature to 190°C.
# - Set variable_time_adjustment to 30 minutes.
# - Ensure variable_start_running is set to "on".

class ExtendedSimulator(Simulator):
    pass