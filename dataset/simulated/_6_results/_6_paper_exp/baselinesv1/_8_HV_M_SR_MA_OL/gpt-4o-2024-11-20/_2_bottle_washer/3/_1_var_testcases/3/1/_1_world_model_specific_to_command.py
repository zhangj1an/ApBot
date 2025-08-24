# The current Simulator correctly models the features and variables required to achieve the user command:
# "Switch on the bottle washer and select 'Wash Only' mode for quick cleaning, and press start to begin."

# Relevant features:
# 1. "power_control" - To switch on the appliance using the power button.
# 2. "choose_wash_mode" - To select 'Wash Only' mode.
# 3. "start_cycle" - To press start and begin.

# Relevant user manual text:
# - Press and hold the “Power” button for 3 seconds to turn on the Bottle Washer Pro®.
# - Touch the “wash mode” button to choose a wash cycle. See page 3 for details.
# - Press the “Start/Pause” button to start the Bottle Washer Pro®.

# Corresponding features in code:
# - "power_control" models the power control functionality with the variable "variable_power_on_off".
# - "choose_wash_mode" allows selecting different wash modes using the variable "variable_wash_mode".
# - "start_cycle" initiates the cycle with the variable "variable_start_running".

# Goal variable values to achieve the command:
# - variable_power_on_off = "on" (to switch on the machine)
# - variable_wash_mode = "Wash Only" (to select the appropriate cycle)
# - variable_start_running = "on" (to start the machine)

class ExtendedSimulator(Simulator): 
    pass