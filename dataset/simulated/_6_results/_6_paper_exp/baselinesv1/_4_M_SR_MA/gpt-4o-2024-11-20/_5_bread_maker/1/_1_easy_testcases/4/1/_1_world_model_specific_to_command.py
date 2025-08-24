# Python comment:
# The given code correctly models all the necessary variables and features described in the user manual to execute the user command to quickly prepare a small loaf of sweet bread with a medium crust color, loaf size 1.5lb, delay timer 6 hours, and start the bread maker. 

# Features needed to achieve the command:
# 1. "adjust_menu" to set the menu to "Sweet".
#    Raw User Manual Text: "Press the Menu button until your desired program is selected. 5. Sweet: Kneading, rising, and baking sweet bread. You may also add ingredients to alter the flavor."
# 2. "adjust_crust_color" to set the crust color to "Medium".
#    Raw User Manual Text: "Use the COLOR button to select a LIGHT, MEDIUM, or DARK color for the crust. This button is not applicable for the Dough or Jam programs."
# 3. "adjust_loaf_size" to set the loaf size to "1.5LB".
#    Raw User Manual Text: "Press this button to select the desired size of the loaf."
# 4. "adjust_delay_time" to set the delay timer to 360 minutes (6 hours).
#    Raw User Manual Text: "Use this button to delay the start time for your desired program... Maximum delay time is 13 hours."
# 5. "start_stop_bread_maker" to start the bread maker.
#    Raw User Manual Text: "To start a program, press the START/STOP button once. A short beep will be heard and the two dots on the LCD screen will begin to flash, the working light will illuminate, and the program will start."

# Feature-list names for the above steps:
# "adjust_menu"
# "adjust_crust_color"
# "adjust_loaf_size"
# "adjust_delay_time"
# "start_stop_bread_maker"

# Goal variable values:
# variable_menu_index: "Sweet"
# variable_crust_color: "Medium"
# variable_loaf_size: "1.5LB"
# variable_delay_time: 360
# variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass