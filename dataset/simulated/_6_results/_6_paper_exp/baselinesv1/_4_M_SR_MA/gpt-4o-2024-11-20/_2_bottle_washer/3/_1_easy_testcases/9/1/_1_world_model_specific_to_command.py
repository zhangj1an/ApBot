# The current code already models the appliance features accurately according to the user manual.
# Sequence of features needed to achieve the user command:
# 1. "power_control": Turn on the appliance by pressing and holding the power button.
# 2. "choose_wash_mode": Set the wash mode to "Wash Only" using the wash mode button.
# 3. "start_cycle": Start the cleaning cycle by pressing the start/pause button.

# Relevant raw text from the user manual:
# 1. Power Control: "Press and hold the 'Power' button for 3 seconds to turn on the Bottle Washer Pro®."
# 2. Choose Wash Mode: "Touch the 'wash mode' button to choose a wash cycle."
# 3. Start Cycle: "Press the 'Start/Pause' button to start the Bottle Washer Pro®."

# Relevant feature_list name from the code:
# "power_control"
# "choose_wash_mode"
# "start_cycle"

# Goal variable values to achieve the command:
# Set variable_power_on_off to "on".
# Set variable_wash_mode to "Wash Only".
# Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass