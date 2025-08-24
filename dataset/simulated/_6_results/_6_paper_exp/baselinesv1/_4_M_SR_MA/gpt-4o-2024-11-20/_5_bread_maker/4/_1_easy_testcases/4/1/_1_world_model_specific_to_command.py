# User command: Activate the Bread Maker and bake sweet bread with a rapid crust at 450g using the sweet menu and a 1-hour delay. Use gluten-free setting. Please ensure the appliance starts.

# After examining the user manual and the provided code, I confirm that the given code correctly models the features required to fulfill this command. Here's the reasoning:

# 1. Set the auto menu to "Sweet":
#    - User manual: "Press the MENU button until the preferred auto menu number is shown on the display screen."
#    - Feature: set_auto_menu
#    - Relevant feature in code: "set_auto_menu"

# 2. Adjust the crust color to "Rapid":
#    - User manual: "Press the CRUST COLOUR button repeatedly to cycle through Light, Medium, Dark (and Rapid) on the display screen."
#    - Feature: adjust_crust_color
#    - Relevant feature in code: "adjust_crust_color"

# 3. Adjust the loaf size to "450g":
#    - User manual: "Press the LOAF SIZE button repeatedly to cycle through 450g, 680g or 900g on the display screen."
#    - Feature: adjust_loaf_size
#    - Relevant feature in code: "adjust_loaf_size"

# 4. Set a 1-hour delay timer:
#    - User manual: "If desired, press the TIMER button to change the start time on the bread maker... The time can be delayed by up to 15 hours."
#    - Feature: adjust_timer
#    - Relevant feature in code: "adjust_timer"

# 5. Activate gluten-free mode:
#    - User manual: "Press the GLUTEN FREE button on the control panel. GLUTEN FREE will display on the screen."
#    - Feature: activate_gluten_free_mode
#    - Relevant feature in code: "activate_gluten_free_mode"

# 6. Start the program:
#    - User manual: "Press START/CANCEL when selections are complete to begin the program."
#    - Feature: start_or_cancel_program
#    - Relevant feature in code: "start_or_cancel_program"

# Sequence of features needed (in order):
# 1. Set the auto menu to "Sweet" (feature: set_auto_menu)
# 2. Adjust the crust color to "Rapid" (feature: adjust_crust_color)
# 3. Adjust the loaf size to "450g" (feature: adjust_loaf_size)
# 4. Set a 1-hour delay timer (feature: adjust_timer)
# 5. Activate gluten-free mode (feature: activate_gluten_free_mode)
# 6. Start the program (feature: start_or_cancel_program)

# Goal variable values to achieve the command:
# variable_menu_index: "Sweet"
# variable_crust_color: "Rapid"
# variable_loaf_size: "450g"
# variable_timer: "01:00:00"
# variable_gluten_free_mode: "on"
# variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass