# The current code accurately models the appliance's features and steps necessary to achieve the user command.
# The user command is: Get a gluten-free loaf with a medium crust ready for lunch tomorrow, loaf size is 2.0lb, set the delay timer to 4 hours, and start the bread maker.

# Sequence of features needed to achieve the command:
# 1. Adjust the menu to "Gluten Free" using feature "adjust_menu".
# User manual text: "Use the Menu button to select a program. Each time it is pressed, the program will vary. Press the button repeatedly to cycle through the 12 programs on the LCD display. Select your desired program."
# Relevant feature_list: "adjust_menu"

# 2. Adjust the crust color to "Medium" using feature "adjust_crust_color".
# User manual text: "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
# Relevant feature_list: "adjust_crust_color"

# 3. Adjust the loaf size to "2.0LB" using feature "adjust_loaf_size".
# User manual text: "Press this button to select the desired size of the loaf. Please note the total operation time may vary among loaf sizes."
# Relevant feature_list: "adjust_loaf_size"

# 4. Set the delay timer to 4 hours (240 minutes) using feature "adjust_delay_time".
# User manual text: "Use the '+/-' buttons to set the required time in 10-minute increments. Total time should include the delay time and the baking time of the selected program."
# Relevant feature_list: "adjust_delay_time"

# 5. Start the bread maker using feature "start_stop_bread_maker".
# User manual text: "To start a program, press the START/STOP button once. A short beep will be heard, the working light will illuminate, and the program will start."
# Relevant feature_list: "start_stop_bread_maker"

# Goal variable values:
# variable_menu_index = "Gluten Free"
# variable_crust_color = "Medium"
# variable_loaf_size = "2.0LB"
# variable_delay_time = 240
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass