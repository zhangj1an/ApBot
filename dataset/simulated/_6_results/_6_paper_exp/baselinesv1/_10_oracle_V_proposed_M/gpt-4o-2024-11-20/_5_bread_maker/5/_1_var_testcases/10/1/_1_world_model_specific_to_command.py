# The given code has modeled the features and variables accurately for the user command:
# "Basic Bread with No Delay. Select the Basic program. Choose a loaf size of 700g.
# Set the crust color to Light. Set the delay timer to 3 hours. Power on and start the operation."

# Below is the sequence of features needed to achieve this command:
# 1. **Feature: set_program_menu**: Select the Basic program.
#    - User Manual: "Press the MENU button repeatedly to cycle through the options below."
#    - Relevant feature_list name: "set_program_menu".
#    - Goal variable value: `variable_menu_index = "1"`.

# 2. **Feature: adjust_loaf_size**: Choose a loaf size of 700g.
#    - User Manual: "Press LOAF SIZE button to select the Loaf Size (as needed)."
#    - Relevant feature_list name: "adjust_loaf_size".
#    - Goal variable value: `variable_loaf_size = "700g"`.

# 3. **Feature: adjust_crust_color**: Set the crust color to Light.
#    - User Manual: "Press COLOR button to select the Crust Colour (as needed)."
#    - Relevant feature_list name: "adjust_crust_color".
#    - Goal variable value: `variable_crust_color = "Light"`.

# 4. **Feature: adjust_delay_timer**: Set the delay timer to 3 hours (180 minutes).
#    - User Manual: "Use the timer buttons when you would like to delay the completion of your bread."
#    - Relevant feature_list name: "adjust_delay_timer".
#    - Goal variable value: `variable_delay_timer = 180`.

# 5. **Feature: start_stop_appliance**: Power on and start the operation.
#    - User Manual: "Press START/STOP button to start or stop the Programmes."
#    - Relevant feature_list name: "start_stop_appliance".
#    - Goal variable value: `variable_start_running = "on"`.

class ExtendedSimulator(Simulator): 
    pass