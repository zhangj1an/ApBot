# The current code accurately models the relevant appliance features based on the user manual to achieve the command:
# Turn on the appliance, set 'Wash Only' mode, and initiate the cleaning cycle.

# The sequence of features needed to achieve this command:
# 1. Feature: "power_on_off"
#    User manual: "Press and hold the 'Power' button for 3 seconds to turn on the Bottle Washer Pro®."
#    Feature_list name: "power_on_off"
#
# 2. Feature: "set_wash_mode"
#    User manual: "Touch the 'wash mode' button to choose a wash cycle."
#    Feature_list name: "set_wash_mode"
#
# 3. Feature: "start_appliance"
#    User manual: "Press the 'Start/Pause' button to start the Bottle Washer Pro®."
#    Feature_list name: "start_appliance"

# Goal variable values to achieve the command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_wash_mode` to "Wash Only".
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator):
    pass