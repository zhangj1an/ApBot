# The current code accurately models the relevant appliance features as specified in the user manual. 
# Here is the sequence of features needed to fulfill the user command:
# 1. Adjust the upper tube temperature knob to 150°C (feature: "adjust_upper_tube_temperature").
# 2. Select the cooking function as "upper and lower heating tube" (feature: "adjust_function_selection").
# 3. Adjust the lower tube temperature knob to 190°C (feature: "adjust_lower_tube_temperature").
# 4. Set the timer for 20 minutes (feature: "adjust_cooking_time_and_start").

# Relevant user manual text:
# 1. "Adjust the upper tube temperature: The adjustable temperature range is 70°C - 230°C."
# 2. "Select cooking function: The upper and lower heating tube are working during this function."
# 3. "Adjust the lower tube temperature: The adjustable temperature range is 70°C - 230°C."
# 4. "Adjust cooking time: If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."

# Relevant feature_list names in the current code:
# - "adjust_upper_tube_temperature"
# - "adjust_function_selection"
# - "adjust_lower_tube_temperature"
# - "adjust_cooking_time_and_start"

# Goal variable values:
# - variable_upper_tube_temperature = 150 (to set upper tube temperature)
# - variable_function_selection = "upper_and_lower_tubes" (to select cooking function)
# - variable_lower_tube_temperature = 190 (to set lower tube temperature)
# - variable_time_adjustment = 20 (to set timer)
# - variable_start_running = "on" (to start cooking)

class ExtendedSimulator(Simulator): 
    pass