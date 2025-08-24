# The given code already models the relevant appliance features needed to achieve the user command.
# Here is the sequence of features required to accomplish this command along with the raw user manual text and feature_list references:
# 
# 1. Adjust the upper tube temperature to 150°C:
#    - Relevant feature: "adjust_upper_tube_temperature"
#    - Raw user manual text: "Adjust the upper tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#
# 2. Select the cooking function as upper and lower heating tube:
#    - Relevant feature: "adjust_function_selection"
#    - Raw user manual text: "Select cooking function. ☐ The upper and lower heating tubes heat up at the same time, and the food is evenly heated to achieve a perfect roasting effect."
#
# 3. Set the lower tube temperature to 190°C:
#    - Relevant feature: "adjust_lower_tube_temperature"
#    - Raw user manual text: "Adjust the lower tube temperature. Please do not rotate to less than 70°C during cooking. The adjustable temperature range is 70°C - 230°C."
#
# 4. Set the cooking time to 30 minutes and start cooking:
#    - Relevant feature: "adjust_cooking_time_and_start"
#    - Raw user manual text: "Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
#    - Raw user manual text: "When 'Stay On' gear is selected, the electric oven is in a continuous working state."
#
# Here are the goal variable values that the current code will achieve to fulfill this user command:
# - variable_upper_tube_temperature: 150
# - variable_function_selection: "upper_and_lower_tubes"
# - variable_lower_tube_temperature: 190
# - variable_time_adjustment: 30
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass