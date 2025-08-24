# The existing simulator code correctly models the relevant appliance functionalities needed to achieve the command: 
# "Schedule 'STEAM' function to finish in 5 hours, then start the machine."

# Relevant feature sequence:
# 1. Use the "set_menu" feature to set the menu index to "steam."
#    - User manual: Close the lid, press the "MENU" button, and select "STEAM."
#    - Feature_list: "set_menu."
# 2. Use the "set_delay_time" feature to schedule the cooking time (5 hours).
#    - User manual: Press the “DELAY” button, adjust the displayed reservation time.
#    - Feature_list: "set_delay_time."
# 3. Use the "start_cooking" feature to begin the cooking process.
#    - User manual: Press the “START” button to start cooking.
#    - Feature_list: "start_cooking."

# Goal variable values to achieve this command:
# - Set variable_menu_index to "steam."
# - Set variable_delay_time to 5.
# - Set variable_start_running to "on."

class ExtendedSimulator(Simulator): 
    pass