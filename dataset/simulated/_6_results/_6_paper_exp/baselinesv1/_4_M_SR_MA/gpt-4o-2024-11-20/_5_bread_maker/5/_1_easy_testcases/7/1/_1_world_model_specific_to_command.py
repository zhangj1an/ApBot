# The following features from the user manual are already well modeled in the given code:
# 
# 1. "set_menu" feature: Raw text - "Press the MENU button repeatedly to cycle through the options below."
#    Feature: "set_menu"
#  
# 2. "set_loaf_size" feature: Raw text - "Press LOAF SIZE button to select the Loaf Size (as needed)."
#    Feature: "set_loaf_size"
# 
# 3. "set_crust_color" feature: Raw text - "Press COLOR button to select the Crust Colour (as needed)."
#    Feature: "set_crust_color"
# 
# 4. "set_delay_timer" feature: Raw text - "The time delay function allows you to delay the start time of baking by up to 12 hours."
#    Feature: "set_delay_timer"
# 
# 5. "start_stop_program" feature: Raw text - "Press START/STOP button to start or stop the Programmes."
#    Feature: "start_stop_program"
# 
# All relevant control panel operations necessary to achieve the user command have been included in the code.

# User Command: Dark Ultra Fast Bread (Dense). Select the Ultra Fast-2 program. Choose a loaf size of 900g. Set the crust color to Dark. Set the delay timer to 5 hours. Power on and start the bread maker operation.

# Sequence of features to achieve the command:
# 1. Use the "set_menu" feature to select the "Ultra Fast-2" program (menu index "7").
#    Relevant user manual text: "Press the MENU button repeatedly to cycle through the options below."
#    Feature: "set_menu"
# 
# 2. Use the "set_loaf_size" feature to set the loaf size to "900g."
#    Relevant user manual text: "Press LOAF SIZE button to select the Loaf Size (as needed)."
#    Feature: "set_loaf_size"
# 
# 3. Use the "set_crust_color" feature to set the crust color to "Dark."
#    Relevant user manual text: "Press COLOR button to select the Crust Colour (as needed)."
#    Feature: "set_crust_color"
# 
# 4. Use the "set_delay_timer" feature to set the delay timer to 5 hours (300 minutes).
#    Relevant user manual text: "Use the + and - buttons to adjust the time delay up to 12 hours in 10-minute steps."
#    Feature: "set_delay_timer"
# 
# 5. Use the "start_stop_program" feature to start the program.
#    Relevant user manual text: "Press START/STOP button to start or stop the Programmes."
#    Feature: "start_stop_program"
# 
# Target goal variable values for the command:
# - variable_menu_index: "7" (Ultra Fast-2)
# - variable_loaf_size: "900g"
# - variable_crust_color: "Dark"
# - variable_delay_timer: 300 (5 hours)
# - variable_start_running: "on"
#
# No modifications to the current code are required as it correctly models all necessary features to achieve the user command.

class ExtendedSimulator(Simulator): 
    pass