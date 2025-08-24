# The current code already correctly models the relevant variables and features described in the user manual.

# The sequence of features needed to achieve the command is as follows:
# 1. Adjust the upper tube temperature knob to 150°C. 
#    - Feature: "adjust_upper_tube_temperature"
#    - User manual: "Adjust the upper tube temperature. Adjustable range is 70°C - 230°C."
# 2. Select the cooking function as the upper and lower heating tube.
#    - Feature: "adjust_function_selection"
#    - User manual: "Select cooking function. The upper and lower heating tubes heat up at the same time."
# 3. Set the lower tube temperature to 190°C.
#    - Feature: "adjust_lower_tube_temperature"
#    - User manual: "Adjust the lower tube temperature. Adjustable range is 70°C - 230°C."
# 4. Set the timer for 20 minutes.
#    - Feature: "adjust_cooking_time_and_start"
#    - User manual: "Set according to food attributes and personal preferences. Oven starts cooking."

# Goal variable values to achieve this command:
# - variable_upper_tube_temperature: 150
# - variable_function_selection: "upper_and_lower_tubes"
# - variable_lower_tube_temperature: 190
# - variable_time_adjustment: 20
# - variable_start_running: "on" (automatically set when adjusting the timer).

class ExtendedSimulator(Simulator):
    pass