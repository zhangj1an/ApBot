# Initial code misses nothing relative to the user manual for the requested command.
# Sequence of features needed to achieve the command:
# 1. "adjust_upper_tube_temperature" to set the upper tube temperature to 150°C.
#    - Quote: "Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#    - Feature list: "adjust_upper_tube_temperature"
# 2. "adjust_function_selection" to choose the cooking function as "upper_and_lower_tubes."
#    - Quote: "- ☐ The upper and lower heating tubes heat up at the same time, ... This mode is suitable for ... baked goods, such as bread."
#    - Feature list: "adjust_function_selection"
# 3. "adjust_lower_tube_temperature" to set the lower tube temperature to 150°C.
#    - Quote: "Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#    - Feature list: "adjust_lower_tube_temperature"
# 4. "adjust_cooking_time_and_start" to set the cooking time to 20 minutes and turn on the microwave.
#    - Quote: "If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
#    - Feature list: "adjust_cooking_time_and_start"

# Goal variable values:
# variable_upper_tube_temperature: set to 150°C
# variable_function_selection: set to "upper_and_lower_tubes"
# variable_lower_tube_temperature: set to 150°C
# variable_time_adjustment: set to 20 minutes
# variable_start_running: set to "on"

class ExtendedSimulator(Simulator):
    pass