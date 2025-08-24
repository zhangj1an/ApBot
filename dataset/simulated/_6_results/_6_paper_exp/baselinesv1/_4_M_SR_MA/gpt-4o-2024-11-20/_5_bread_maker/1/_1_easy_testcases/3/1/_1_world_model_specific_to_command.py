# The provided code already accurately models the user manual's features relevant to the command. 
# Here is the sequence of features needed to achieve the command based on the user manual and the provided feature_list.

# Sequence of Features Needed:
# 1. Adjust the Menu to select "Whole Wheat".
#    User Manual: "**Whole Wheat**: Kneading, rising and baking of whole wheat bread."
#    Feature in code: "adjust_menu"

# 2. Adjust the Crust Color to "Light".
#    User Manual: "Use the Color button to select a LIGHT, MEDIUM or DARK color for the crust. This button is not applicable for the Dough or Jam programs."
#    Feature in code: "adjust_crust_color"

# 3. Adjust the Loaf Size to "1.5LB".
#    User Manual: "Press this button to select the desired size of the loaf. Please note the total operation time may vary among loaf sizes."
#    Feature in code: "adjust_loaf_size"

# 4. Set the Delay Timer to 240 minutes (4 hours).
#    User Manual: "Begin by determining when a freshly baked loaf of bread is desired, then press the '+' and '-' buttons to set the required time in 10-minute increments. Maximum delay time is 13 hours."
#    Feature in code: "adjust_delay_time"

# 5. Start the Bread Maker.
#    User Manual: "To start a program, press the START/STOP button once."
#    Feature in code: "start_stop_bread_maker"

# Goal variable values to achieve this command:
# - Set "variable_menu_index" to "Whole Wheat".
# - Set "variable_crust_color" to "Light".
# - Set "variable_loaf_size" to "1.5LB".
# - Set "variable_delay_time" to 240 (corresponds to 4 hours).
# - Set "variable_start_running" to "on".

class ExtendedSimulator(Simulator):
    pass