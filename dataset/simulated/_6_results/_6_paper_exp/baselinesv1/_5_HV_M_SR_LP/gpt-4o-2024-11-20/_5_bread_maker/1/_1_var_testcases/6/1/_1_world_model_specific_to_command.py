# Python comments indicating the sequence of actions needed to achieve the user command:

# Sequence of features needed:
# Step 1: Adjust menu to "Sandwich"
# Feature: "adjust_menu"
# User manual: 
# "The Menu button is used to select a program. Each time it is pressed, the program will vary. Press the button repeatedly to cycle through the 12 programs on the LCD display. Select your desired program."

# Step 2: Adjust loaf size to "1.5LB"
# Feature: "adjust_loaf_size"
# User manual:
# "Press this button to select the desired size of the loaf. Please note the total operation time may vary among loaf sizes."

# Step 3: Adjust delay timer to 6 hours
# Feature: "adjust_delay_time"
# User manual:
# "Use this button to delay the start time for your desired program. Begin by determining when a freshly baked loaf of bread is desired, then press the “+” and “–” buttons to set the required time in 10-minute increments. Maximum delay time is 13 hours."

# Step 4: Start the bread maker
# Feature: "start_stop_bread_maker"
# User manual:
# "This button is used for starting and stopping the selected baking program. To start a program, press the START/STOP button once."

# Generate goal variable values to achieve user command:
# variable_menu_index = "Sandwich"
# variable_loaf_size = "1.5LB"
# variable_delay_time = 360 (6 hours delay time in minutes)
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass