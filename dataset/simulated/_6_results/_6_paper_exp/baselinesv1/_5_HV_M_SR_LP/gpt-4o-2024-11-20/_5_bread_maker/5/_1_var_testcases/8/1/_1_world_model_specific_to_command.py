# The current code for the Simulator accurately models the relevant appliance features as described in the user manual.
# Here is the sequence of features needed to achieve the command:
# 1. Select the Quick program.
#    - Feature: "set_menu"
#    - User manual text: "Choose a Programme with the MENU button."
# 2. Choose a loaf size of 900g.
#    - Feature: "set_loaf_size"
#    - User manual text: "Press LOAF SIZE button to select the Loaf Size (as needed)."
# 3. Set the crust color to Medium.
#    - Feature: "set_crust_color"
#    - User manual text: "Press COLOR button to select the Crust Colour (as needed)."
# 4. Set the delay timer to 2 hours.
#    - Feature: "set_delay_timer"
#    - User manual text: "Use these buttons when you would like to delay the completion of your bread."
# 5. Power on and start operation.
#    - Feature: "start_stop_program"
#    - User manual text: "Press START/STOP button to start or stop the Programmes."

# Goal variable values to achieve this command:
# Set variable_menu_index to "4" (Quick program).
# Set variable_loaf_size to "900g".
# Set variable_crust_color to "Medium".
# Set variable_delay_timer to "120" (2 hours).
# Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass