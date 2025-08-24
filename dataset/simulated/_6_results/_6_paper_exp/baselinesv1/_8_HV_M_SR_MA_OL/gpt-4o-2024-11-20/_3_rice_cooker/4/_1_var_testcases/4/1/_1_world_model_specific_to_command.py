# The current code accurately models the required appliance features and variables to achieve the command:
# "Prepare 'GRAINS' with a reservation timer set for 2 hours, then start the machine."
#
# Sequence of features and actions:
# 1. Use the "set_menu" feature to set the cooking mode to "grains".
#    - Feature: "set_menu"
#    - User manual: "Close the rice cooker lid and press the 'MENU' button. Select the 'GRAINS' function..."
#    - Code: feature_list["set_menu"]
#    - Goal variable value: Set `variable_menu_index` to `"grains"`.
# 
# 2. Use the "set_delay_time" feature to set the reservation timer to 2 hours.
#    - Feature: "set_delay_time"
#    - User manual: "Press the 'DELAY' button, the Time Display flashes, and then press the button 'DELAY' again to adjust the displayed reservation time."
#    - Code: feature_list["set_delay_time"]
#    - Goal variable value: Set `variable_delay_time` to `2`.
# 
# 3. Use the "start_cooking" feature to start the machine.
#    - Feature: "start_cooking"
#    - User manual: "Press the 'START' button, the cooking will be finished at the appointed time."
#    - Code: feature_list["start_cooking"]
#    - Goal variable values: Set `variable_start_running` to `"on"`.

class ExtendedSimulator(Simulator): 
    pass