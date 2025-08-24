# Python comment:
# The current code accurately models the appliance features to achieve the requested user command. 
# It includes features for selecting the menu, adjusting crust color, setting loaf size, 
# configuring delay time, and starting/stopping the bread maker. Based on the user manual:

# 1. **Menu Selection**
#    "The Menu button is used to select a program. Each time it is pressed, the program will vary. 
#    Press the button repeatedly to cycle through the 12 programs on the LCD display."
#    => Modeled as feature_list["adjust_menu"].

# 2. **Crust Color Selection**
#    "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
#    => Modeled as feature_list["adjust_crust_color"].

# 3. **Loaf Size Selection**
#    "Press this button to select the desired size of the loaf."
#    => Modeled as feature_list["adjust_loaf_size"].

# 4. **Delay Time Setup**
#    "Use this button to delay the start time for your desired program. 
#    Press the “+” and “–” buttons to set the required time in 10-minute increments."
#    => Modeled as feature_list["adjust_delay_time"].

# 5. **Starting the Bread Maker**
#    "To start a program, press the START/STOP button once. 
#    To stop the program, press the START/STOP button for approx. 2 seconds."
#    => Modeled as feature_list["start_stop_bread_maker"].

# The sequence of features required to achieve the user's command are:
# 1. Adjust Menu: Select "Whole Wheat".
# 2. Adjust Crust Color: Select "Light".
# 3. Adjust Loaf Size: Select "1.5LB".
# 4. Adjust Delay Time: Set to 4 hours.
# 5. Start the Bread Maker.

# Goal variable values to achieve the command:
# - `variable_menu_index` = "Whole Wheat"
# - `variable_crust_color` = "Light"
# - `variable_loaf_size` = "1.5LB"
# - `variable_delay_time` = 240 (4 hours in minutes)
# - `variable_start_running` = "on"

class ExtendedSimulator(Simulator): 
    pass