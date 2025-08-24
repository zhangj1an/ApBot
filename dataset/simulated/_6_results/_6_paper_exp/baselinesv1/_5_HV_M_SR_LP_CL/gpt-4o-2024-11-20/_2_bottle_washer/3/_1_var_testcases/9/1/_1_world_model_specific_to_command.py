# The user command is to turn on the appliance, set 'Wash Only' mode, and initiate the cleaning cycle.

# Sequence of features needed to achieve the command based on the user manual:
# 1. Feature: "power_control" - Turn on the appliance using the "press_and_hold_power_button" action.
# 2. Feature: "choose_wash_mode" - Set the wash mode to 'Wash Only' using the "press_wash_mode_button" action.
# 3. Feature: "start_cycle" - Start the cleaning cycle using the "press_start_pause_button" action.

# Relevant user manual text for each step:
# 1. Power Control: "Press and hold the "Power" button for 3 seconds to turn on the Bottle Washer Pro®."
# 2. Choose wash mode: "Touch the “wash mode” button to choose a wash cycle." (Cycle options include 'Wash Only'.)
# 3. Start Cycle: "Press the “Start/Pause” button to start the Bottle Washer Pro®."

# Corresponding feature_list names in the given code:
# - "power_control"
# - "choose_wash_mode"
# - "start_cycle"

# Goal variable values to achieve the command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_wash_mode` to "Wash Only".
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass