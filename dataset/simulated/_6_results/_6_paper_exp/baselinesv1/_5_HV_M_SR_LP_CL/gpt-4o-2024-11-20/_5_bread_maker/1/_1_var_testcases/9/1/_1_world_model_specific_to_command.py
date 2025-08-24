# All the required features and variables in the given code match the functional requirements described in the user manual.
# The sequence of features needed to achieve the user command is:
# 1. "adjust_menu": Set variable_menu_index to "Basic".
#    - User manual text: "**Basic**: Kneading, rising and baking normal bread. You may also add ingredients to increase flavor."
# 2. "adjust_crust_color": Set variable_crust_color to "Dark".
#    - User manual text: "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
# 3. "adjust_loaf_size": Set variable_loaf_size to "2.0LB".
#    - User manual text: "Press this button to select the desired size of the loaf."
# 4. "adjust_delay_time": Set variable_delay_time to 360 (6 hours).
#    - User manual text: "Begin by determining the when a freshly baked loaf of bread is desired, then press the “+” and “–” buttons to set the required time in 10-minute increments."
# 5. "start_stop_bread_maker": Start the bread-making process by setting variable_start_running to "on".
#    - User manual text: "To start a program, press the START/STOP button once."

# After confirming the provided feature list covers all of the above, the goal variable values required to achieve the user command are:
# - variable_menu_index = "Basic"
# - variable_crust_color = "Dark"
# - variable_loaf_size = "2.0LB"
# - variable_delay_time = 360
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass