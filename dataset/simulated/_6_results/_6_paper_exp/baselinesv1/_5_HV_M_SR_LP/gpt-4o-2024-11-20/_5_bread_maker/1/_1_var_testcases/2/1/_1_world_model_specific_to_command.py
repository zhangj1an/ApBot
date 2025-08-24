# The command is to prepare a French bread with a dark crust for dinner tonight, loaf size is 2.0lb, set the delay timer to 6 hours from now and start the bread maker.

# The current code is correctly modeling the features described in the user manual to achieve the command. Below is the sequence of steps and relevant features:

# 1. Adjust the menu to "French" for French bread.
#    User manual text: "The Menu button is used to select a program. Each time it is pressed, the program will vary. Press the button repeatedly to cycle through the 12 programs on the LCD display."
#    Relevant feature: "adjust_menu"

# 2. Set the crust to "Dark".
#    User manual text: "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
#    Relevant feature: "adjust_crust_color"

# 3. Set the loaf size to "2.0LB".
#    User manual text: "Press this button to select the desired size of the loaf."
#    Relevant feature: "adjust_loaf_size"

# 4. Set the delay timer to 6 hours (360 minutes from now).
#    User manual text: "Use this button to delay the start time for your desired program. At the completion of the total delay time, hot bread will be ready. Maximum delay time is 13 hours."
#    Relevant feature: "adjust_delay_time"

# 5. Start the bread maker.
#    User manual text: "To start a program, press the START/STOP button once."
#    Relevant feature: "start_stop_bread_maker"

# Goal variable values to achieve the command:
# - variable_menu_index: "French"
# - variable_crust_color: "Dark"
# - variable_loaf_size: "2.0LB"
# - variable_delay_time: 360 (6 hours in minutes)
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass