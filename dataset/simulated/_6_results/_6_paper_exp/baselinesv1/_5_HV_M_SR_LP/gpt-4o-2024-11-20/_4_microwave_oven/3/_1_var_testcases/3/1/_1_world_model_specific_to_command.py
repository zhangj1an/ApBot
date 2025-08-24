# The user manual allows users to set upper tube temperature, function selection, lower tube temperature, and cooking time. 
# However, there is no indication in the user manual that the microwave starts running by explicitly pressing a "start" button. 
# Instead, setting the "cooking time" seems to prompt the oven to transition into a "running" state. Additionally, the following features and variables are all correctly implemented in the code already.

# Relevant sequence to achieve the user command:
# 1. Adjust Upper Tube Temperature (feature: "adjust_upper_tube_temperature")
#    - Action: Turn the upper tube temperature adjustment dial clockwise or anticlockwise to set the temperature to 150°C.
#    - Raw user manual text: "Adjust the upper tube temperature: 70°C - 230°C."
#    - Code feature: "adjust_upper_tube_temperature"
# 2. Select Cooking Function (feature: "adjust_function_selection")
#    - Action: Turn the function selection dial clockwise or anticlockwise to set it to 'upper and lower heating tube'.
#    - Raw user manual text: "Select cooking function: ☐ The upper and lower heating tubes heat up at the same time."
#    - Code feature: "adjust_function_selection"
# 3. Adjust Lower Tube Temperature (feature: "adjust_lower_tube_temperature")
#    - Action: Turn the lower tube temperature adjustment dial clockwise or anticlockwise to set the temperature to 190°C.
#    - Raw user manual text: "Adjust the lower tube temperature: 70°C - 230°C."
#    - Code feature: "adjust_lower_tube_temperature"
# 4. Adjust Cooking Time and Start (feature: "adjust_cooking_time_and_start")
#    - Action: Turn the time adjustment dial clockwise or anticlockwise to set it to 30 minutes.
#    - Raw user manual text: "Adjust cooking time: If the cooking time is less than 10 minutes, turn the time knob to more than 10 minutes, then turn the time knob back to the desired time position."
#    - Code feature: "adjust_cooking_time_and_start"

# Goal variable values:
# - variable_upper_tube_temperature = 150
# - variable_function_selection = "upper_and_lower_tubes"
# - variable_lower_tube_temperature = 190
# - variable_time_adjustment = 30
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass