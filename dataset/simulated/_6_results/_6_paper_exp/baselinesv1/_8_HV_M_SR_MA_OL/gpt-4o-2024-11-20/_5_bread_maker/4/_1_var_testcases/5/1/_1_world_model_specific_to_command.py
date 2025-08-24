# The user manual has been accurately modeled in the Simulator class.
# Relevant Features Needed to Achieve the User Command:
# 1. "set_auto_menu": To set the menu to "Sweet".
#    * User manual: "Pressing the MENU button will cycle through the auto menu items."
# 2. "adjust_loaf_size": To set the loaf size to "900g".
#    * User manual: "CRUST COLOUR button" (context: adjusting specified variables).
# 3. "adjust_crust_color": To set the crust color to "Light".
#    * User manual: "Press the CRUST COLOUR button repeatedly to cycle through Light, Medium, Dark."
# 4. "adjust_timer": To set a 3-hour delay.
#    * User manual: "Press up arrow or down arrow to increase or decrease start time."
#    * Note: Delay timer is only valid for certain menus like Basic, French, Whole Wheat, Sweet, and Continental.
# 5. "activate_gluten_free_mode": To enable gluten-free functionality.
#    * User manual: "Press the GLUTEN FREE button on the control panel."
# 6. "start_or_cancel_program": To start the bread maker.
#    * User manual: "Press the START/CANCEL button."

# Goal Variable Values: 
# - variable_menu_index: "Sweet" 
# - variable_loaf_size: "900g" 
# - variable_crust_color: "Light" 
# - variable_timer: "03:00:00" 
# - variable_gluten_free_mode: "on" 
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass