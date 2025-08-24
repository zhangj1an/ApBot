# The current code already includes the necessary variables and features required to achieve the user command:
# "Prepare 'GRAINS' with a reservation timer set for 2 hours, then start the machine."
# Below is the sequence of features needed along with relevant excerpts from the user manual and the corresponding feature list.

# Sequence of features needed:
# 1. Adjust the menu index to "grains".
#    - User manual: "Close the lid and press the 'MENU' button. Select the 'GRAINS' function and press the 'START' button to enter the cooking state."
#    - Relevant feature list: feature_list["set_menu"]
# 2. Set the delay timer to 2 hours.
#    - User manual: "Press the ‘DELAY’ button, the Time Display flashes, and then press the button ‘DELAY’ again to adjust the displayed reservation time."
#    - Relevant feature list: feature_list["set_delay_time"]
# 3. Start the machine.
#    - User manual: "Press the 'START' button, the cooking will be finished at the appointed time."
#    - Relevant feature list: feature_list["start_cooking"]

# Goal variable values:
# 1. Set variable_menu_index to "grains".
# 2. Set variable_delay_time to "2".
# 3. Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass