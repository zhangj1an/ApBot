# As per the user command: Switch on, select 'Wash, Sterilize, Dry', and begin the washing procedure.

# Explanation: 
# The current code correctly models the following appliance functionalities according to the user manual:
# 1. Switching on the appliance: Feature `power_control` is properly defined with action `press_and_hold_power_button` connected to the variable `variable_power_on_off` to toggle the power state.
# 2. Selecting wash mode: Feature `choose_wash_mode` allows adjusting `variable_wash_mode` using action `press_wash_mode_button`. The user command requires setting it to "Wash, Sterilize, Dry".
# 3. Starting the washing procedure: Feature `start_cycle` correctly adjusts `variable_start_running` using action `press_start_pause_button`. It sets `variable_start_running` to "on".

# Quoting relevant user manual text:
# 1. "Press and hold the `Power` button for 3 seconds to turn on the Bottle Washer Pro®."
# 2. "Touch the `wash mode` button to choose a wash cycle."
# 3. "Press the `Start/Pause` button to start the Bottle Washer Pro®."

# Corresponding feature list from the provided code:
# - `power_control` for turning on the appliance.
# - `choose_wash_mode` for setting the wash mode.
# - `start_cycle` for starting the washing process.

# The sequence of features needed to achieve this command:
# 1. Use feature `power_control` to turn `variable_power_on_off` to "on".
#    - Action: `press_and_hold_power_button`.
# 2. Use feature `choose_wash_mode` to set `variable_wash_mode` to "Wash, Sterilize, Dry".
#    - Action: `press_wash_mode_button`.
# 3. Use feature `start_cycle` to set `variable_start_running` to "on".
#    - Action: `press_start_pause_button`.

# Goal variable values:
# - `variable_power_on_off`: "on"
# - `variable_wash_mode`: "Wash, Sterilize, Dry"
# - `variable_start_running`: "on"

class ExtendedSimulator(Simulator): 
    pass