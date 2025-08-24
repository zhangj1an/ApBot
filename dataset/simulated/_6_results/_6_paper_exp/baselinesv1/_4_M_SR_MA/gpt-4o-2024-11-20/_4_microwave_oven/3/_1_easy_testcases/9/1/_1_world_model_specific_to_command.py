# The requested Simulator code models all relevant features accurately. 
# Following are the features needed for the user command:
# 1. Set the "Upper tube temperature" using feature 'adjust_upper_tube_temperature', described in the user manual by: "Adjust the upper tube temperature. The adjustable temperature range is 70°C - 230°C."
# 2. Set the "Cooking function" using feature 'adjust_function_selection', described in the user manual by: "Select cooking function."
# 3. Set the "Lower tube temperature" using feature 'adjust_lower_tube_temperature', described in the user manual by: "Adjust the lower tube temperature. The adjustable temperature range is 70°C - 230°C."
# 4. Adjust the "Time" and start running using feature 'adjust_cooking_time_and_start', described in the user manual: "Adjust cooking time. If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position. When 'Stay On' gear is selected, the oven is in a continuous working state and the power indicator light is lit."

# Feature list names in the given code:
# "adjust_upper_tube_temperature", "adjust_function_selection", "adjust_lower_tube_temperature", "adjust_cooking_time_and_start"

# Goal variable values for the user command:
# variable_upper_tube_temperature: 110
# variable_function_selection: "upper_and_lower_tubes"
# variable_lower_tube_temperature: 150
# variable_time_adjustment: 20
# variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass