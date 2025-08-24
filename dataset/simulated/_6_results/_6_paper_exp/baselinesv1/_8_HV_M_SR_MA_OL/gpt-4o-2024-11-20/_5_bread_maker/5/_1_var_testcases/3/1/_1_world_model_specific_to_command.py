# The manual features and variables were accurately modeled in the provided code.
# The sequence of features required to achieve the command "Light French Bread" are:
# 1. "set_menu": Choose the French program.
#    - Raw text: "Choose a Programme with the MENU button."
#    - Featured as "set_menu" in the code.
# 2. "set_loaf_size": Select 900g loaf size.
#    - Raw text: "Press LOAF SIZE button to select the Loaf Size (as needed)."
#    - Featured as "set_loaf_size" in the code.
# 3. "set_crust_color": Set crust color to Light.
#    - Raw text: "Press COLOR button to select the Crust Colour (as needed)."
#    - Modeled as "set_crust_color" in the code.
# 4. "set_delay_timer": Set delay timer to 5 hours.
#    - Raw text: "To set the Timer, determine when you would like your bread to be ready, then set the Timer."
#    - This is modeled in "set_delay_timer".
# 5. "start_stop_program": Power on and start baking.
#    - Raw text: "Press START/STOP button to start the breadmaker."
#    - Modeled in "start_stop_program".

# Goal variable values to implement this command:
# - variable_menu_index: Set to "2" (French program).
# - variable_loaf_size: Set to "900g".
# - variable_crust_color: Set to "Light".
# - variable_delay_timer: Set to 300 (5 hours in minutes).
# - variable_start_running: Set to "on".

class ExtendedSimulator(Simulator):
    pass