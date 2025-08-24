# Python comment:
# Upon reviewing the user manual and the provided simulator code, I confirm that the code has correctly modeled the relevant features and variables to achieve the user command:
# "Start the microwave. Set the upper tube temperature to 150°C, select the cooking function as upper and lower heating tube, set the lower tube temperature to 190°C, and adjust the cooking time to 30 minutes."

# Sequence of features needed to achieve this command:
# 1. Use the "adjust_upper_tube_temperature" feature to set the upper tube temperature to 150°C.
# 2. Use the "adjust_function_selection" feature to set the cooking function to "upper and lower heating tube."
# 3. Use the "adjust_lower_tube_temperature" feature to set the lower tube temperature to 190°C.
# 4. Use the "adjust_cooking_time_and_start" feature to set the cooking time to 30 minutes and automatically start the microwave.

# Relevant user manual text and feature_list names:
# - User manual: "Adjust the upper tube temperature..." -> Feature: "adjust_upper_tube_temperature"
# - User manual: "The upper and lower heating tubes heat up at the same time..." -> Feature: "adjust_function_selection"
# - User manual: "Adjust the lower tube temperature..." -> Feature: "adjust_lower_tube_temperature"
# - User manual: "Adjust cooking time... The oven starts cooking." -> Feature: "adjust_cooking_time_and_start"

# Goal variable values:
# - variable_upper_tube_temperature: 150
# - variable_function_selection: "upper_and_lower_tubes"
# - variable_lower_tube_temperature: 190
# - variable_time_adjustment: 30
# - variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass