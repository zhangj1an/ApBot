# The current code already models all required appliance features accurately to fulfill the command:
# Sequence of features: "adjust_menu", "adjust_crust_color", "adjust_loaf_size", "adjust_delay_time", "start_stop_bread_maker".
# Raw user manual text:
# - Menu: "Press the Menu button until your desired program is selected."
# - Crust Color: "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust."
# - Loaf Size: "Press this button to select the desired size of the loaf."
# - Delay Function: "Begin by determining when a freshly baked loaf of bread is desired, then press the “+” and “–” buttons to set the required time in 10-minute increments."
# - Start/Stop: "Press the START/STOP button once. A short beep will be heard...the program will start."

# Feature List Names:
# - "adjust_menu"
# - "adjust_crust_color"
# - "adjust_loaf_size"
# - "adjust_delay_time"
# - "start_stop_bread_maker"

# Goal variable values for the command:
# - variable_menu_index = "Gluten Free"
# - variable_crust_color = "Medium"
# - variable_loaf_size = "2.0LB"
# - variable_delay_time = 240 (in minutes, corresponding to 4 hours)
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass