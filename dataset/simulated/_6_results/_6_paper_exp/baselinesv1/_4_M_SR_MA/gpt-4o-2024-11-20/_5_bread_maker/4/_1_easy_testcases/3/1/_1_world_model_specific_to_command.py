# The current code accurately models the appliance features described in the user manual
# and aligns with all steps needed to achieve the requested user command.

# Sequence of features needed to achieve the user command:
# 1. "set_auto_menu" - Set the menu to "Whole Wheat".
#    User Manual Reference: 
#    "1) Press the MENU button until the preferred auto menu number is shown on the display screen."
#    Corresponding feature_list name: "set_auto_menu".
#
# 2. "adjust_crust_color" - Set the crust color to "Dark".
#    User Manual Reference: 
#    "3. To change the crust colour, press the CRUST COLOUR button repeatedly to cycle through Light, Medium, Dark (and Rapid) on the display screen."
#    Corresponding feature_list name: "adjust_crust_color".
#
# 3. "adjust_loaf_size" - Set loaf size to "900g".
#    User Manual Reference: 
#    "4. To change the loaf size, press the LOAF SIZE button repeatedly to cycle through 450g, 680g or 900g on the display screen."
#    Corresponding feature_list name: "adjust_loaf_size".
#
# 4. "activate_gluten_free_mode" - Enable the gluten-free mode.
#    User Manual Reference:
#    "Press the GLUTEN FREE button on the control panel. GLUTEN FREE will display on the screen."
#    Corresponding feature_list name: "activate_gluten_free_mode".
#
# 5. "adjust_timer" - Adjust the delay start timer to 3 hours.
#    User Manual Reference:
#    "1. If desired, press the TIMER button to change the start time on the bread maker. 
#     2. The time displayed represents the finishing time... 
#     3. Press up arrow to increase the time in 10-minute increments or press down arrow to decrease the time in 10-minute increments."
#    Corresponding feature_list name: "adjust_timer".
#
# 6. "start_or_cancel_program" - Start the program.
#    User Manual Reference:
#    "Press START/CANCEL when selections are complete to begin the program."
#    Corresponding feature_list name: "start_or_cancel_program".

# Goal variable values to achieve this command:
# 1. variable_menu_index = "Whole Wheat"
# 2. variable_crust_color = "Dark"
# 3. variable_loaf_size = "900g"
# 4. variable_gluten_free_mode = "on"
# 5. variable_timer = "03:00:00" (3 hours delay)
# 6. variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass