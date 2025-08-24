# The given code accurately models all the relevant appliance features described in the user manual to achieve the requested user command.
# Sequence of features needed to achieve the command:
# 1. "adjust_upper_tube_temperature": to set the upper tube temperature to 110°C
# 2. "adjust_function_selection": to select the cooking function as "upper and lower heating tube"
# 3. "adjust_lower_tube_temperature": to set the lower tube temperature to 70°C
# 4. "adjust_time_or_stay_on": to set the timer to 50 minutes

# Relevant raw user manual text:
# 1. "Upper tube temperature adjustment knob: Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# 2. "Function selection knob: Select cooking function. ☐ The upper and lower heating tubes heat up at the same time, and the food is evenly heated to achieve a perfect roasting effect."
# 3. "Lower tube temperature adjustment knob: Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
# 4. "Time adjustment knob: Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."

# Respective feature list names from the given code:
# - Feature for upper tube temperature adjustment: "adjust_upper_tube_temperature"
# - Feature for function selection: "adjust_function_selection"
# - Feature for lower tube temperature adjustment: "adjust_lower_tube_temperature"
# - Feature for time adjustment: "adjust_time_or_stay_on"

# Goal variable values to achieve the command:
# - variable_upper_tube_temperature: 110 (set to 110°C)
# - variable_function_selection: "upper_and_lower_tubes" (select upper and lower heating tubes)
# - variable_lower_tube_temperature: 70 (set to 70°C)
# - variable_time_adjustment: 50 (set the timer to 50 minutes)

class ExtendedSimulator(Simulator): 
    pass