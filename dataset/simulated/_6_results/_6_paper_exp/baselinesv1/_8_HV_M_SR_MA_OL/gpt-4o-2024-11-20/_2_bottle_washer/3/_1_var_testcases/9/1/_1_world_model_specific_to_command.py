# The given code correctly models the required features to achieve the user command: "Turn on the appliance, set 'Wash Only' mode, and initiate the cleaning cycle." 

# Below is the sequence of features needed to achieve this command:
# 1. Use the "power_control" feature to turn on the appliance.
#    User manual: "Press and hold the 'Power' button for 3 seconds to turn on the Bottle Washer Pro®."
#    Feature name in the given code: "power_control"

# 2. Use the "choose_wash_mode" feature to set the wash mode to 'Wash Only'.
#    User manual: "Touch the 'wash mode' button to choose a wash cycle."
#    Feature name in the given code: "choose_wash_mode"

# 3. Use the "start_cycle" feature to start the cleaning cycle.
#    User manual: "Press the 'Start/Pause' button to start the Bottle Washer Pro®."
#    Feature name in the given code: "start_cycle"

# The goal variable values to achieve this command: 
# - Set `variable_power_on_off` to "on".
# - Set `variable_wash_mode` to "Wash Only".
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass