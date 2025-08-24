# Python comment: 
# The given code already accurately models the relevant appliance features for the requested command: 
# "Select the 'WHITE RICE' function with a reservation timer set for 4 hours, then start the machine."

# Sequence of Features Needed:
# 1. Feature to select the 'WHITE RICE' function, which is modeled in "set_menu".
# 2. Feature to set the reservation timer, which is modeled in "set_reservation_time".
# 3. Feature to start the machine, which is modeled in "start_cooking".

# Relevant User Manual Text:
# 1. For menu selection: 
# "After closing the lid, select Quick Rice or other functions by using the Quick Rice or MENU button."
# 2. For reservation timer:
# "Set the timer for cooking completion. Press the 'DELAY' button, the Time Display flashes, and then press the button 'DELAY' again to adjust the displayed reservation time."
# 3. For starting:
# "Start cooking. Press the 'START' button, the cooking will be finished at the appointed time."

# Feature Names from Code:
# - "set_menu" (for selecting 'WHITE RICE')
# - "set_reservation_time" (for setting reservation timer to 4 hours)
# - "start_cooking" (to start the machine)

# Goal Variable Values:
# - variable_menu_index: "WHITE RICE"
# - variable_reservation_time: 4
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass