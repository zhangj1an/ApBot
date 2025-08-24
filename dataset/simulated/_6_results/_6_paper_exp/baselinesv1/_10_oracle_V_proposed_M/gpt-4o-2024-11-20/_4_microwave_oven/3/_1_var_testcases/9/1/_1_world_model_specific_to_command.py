# The given code already models all the relevant appliance features and variables to achieve the user command. 
# The sequence of features needed to achieve the user command is:
# 1. adjust_upper_tube_temperature 
# 2. adjust_function_selection
# 3. adjust_lower_tube_temperature
# 4. adjust_time_or_stay_on
# 
# Relevant raw user manual text:
# 1. "Adjust the upper tube temperature: The adjustable temperature range is 70°C - 230°C."
#    Corresponds to feature_list["adjust_upper_tube_temperature"].
# 2. "Select cooking function: ☐ The upper and lower heating tubes are working during this function."
#    Corresponds to feature_list["adjust_function_selection"].
# 3. "Adjust the lower tube temperature: The adjustable temperature range is 70°C - 230°C."
#    Corresponds to feature_list["adjust_lower_tube_temperature"].
# 4. "Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
#    Corresponds to feature_list["adjust_time_or_stay_on"].
#
# The goal variable values to achieve this command:
# - variable_upper_tube_temperature: Set to 110°C.
# - variable_function_selection: Set to "upper_and_lower_tubes".
# - variable_lower_tube_temperature: Set to 150°C.
# - variable_time_adjustment: Set to 20 minutes.

class ExtendedSimulator(Simulator): 
    pass