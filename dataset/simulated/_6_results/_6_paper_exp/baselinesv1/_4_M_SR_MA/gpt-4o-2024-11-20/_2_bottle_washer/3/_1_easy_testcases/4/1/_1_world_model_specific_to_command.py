# The current code correctly models all the relevant appliance features based on the user manual.
# The sequence of features required to achieve the user command is:
# 1. Activate the power of the appliance ("power_control").
# 2. Set the sterilize and dry cycle ("choose_sterilize_dry_mode").
# 3. Press start to begin the cycle ("start_cycle").
#
# Here is the relevant raw user manual text:
# 1. Power On/Off: "Press and hold the 'Power' button for 3 seconds to turn on the Bottle Washer Pro®."
# 2. Set Sterilize & Dry Mode: "Touch the Sterilize-Dry button 1 time, then press the Start/Pause button to start."
# 3. Start the cycle: "Press the 'Start/Pause' button to start the Bottle Washer Pro®."
#
# Corresponding feature_list names in the given code:
# - "power_control": Activates the appliance.
# - "choose_sterilize_dry_mode": Allows selecting "Sterilize & Dry" mode.
# - "start_cycle": Starts the washer.

class ExtendedSimulator(Simulator):
    pass