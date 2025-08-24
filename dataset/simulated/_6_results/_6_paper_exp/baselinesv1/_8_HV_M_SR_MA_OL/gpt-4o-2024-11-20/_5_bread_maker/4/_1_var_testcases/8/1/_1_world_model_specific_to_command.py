# Raw user manual text describing the relevant sequence of actions for the user command:
# "1. Open the lid of the bread maker and remove the bread pan using the handle."
# "2. Add ingredients to the bread pan in the order listed in the recipe."
# "3. Set the MENU button to the corresponding type of bread."
# "4. To change the crust colour, press the CRUST COLOUR button repeatedly."
# "5. To change the loaf size, press the LOAF SIZE button repeatedly."
# "6. If desired, press the TIMER button to change the start time."
# "7. Press the GLUTEN FREE button directly to activate the gluten-free mode."
# "8. Press START/CANCEL when selections are complete to begin the program."

# Relevant feature_list names from the given code:
# "set_auto_menu" for selecting the menu
# "adjust_crust_color" for setting the crust color
# "adjust_loaf_size" for adjusting the loaf size
# "adjust_timer" for setting the timer
# "activate_gluten_free_mode" for enabling gluten-free mode
# "start_or_cancel_program" for starting the program

# Sequence of features needed to execute the user command:
# 1. Use "set_auto_menu" to set the menu to "Whole Wheat."
# 2. Use "adjust_loaf_size" to set the loaf size to "680g."
# 3. Use "adjust_crust_color" to set the crust color to "Medium."
# 4. Use "adjust_timer" to set the timer to "02:00:00."
# 5. Use "activate_gluten_free_mode" to enable gluten-free mode.
# 6. Use "start_or_cancel_program" to start the program.

# Goal variable values to achieve the command:
# variable_menu_index = "Whole Wheat"
# variable_loaf_size = "680g"
# variable_crust_color = "Medium"
# variable_timer = "02:00:00"
# variable_gluten_free_mode = "on"
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass