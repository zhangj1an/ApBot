# The goal is to Turn on the machine and start the sterilize-only function.

# Verifying the user manual with the given feature list and variables:
# User manual text: 
# 1. "Press the On/Off (power symbol) button once and the function icons will light up. If there is no selection of function after pressing on/off button, the appliance will automatically switch off."
# 2. "Sterilize only function: Press the Sterilize button one time to initiate sterilization. The sterilization cycle will start automatically, and the appliance will beep 5 times and switch off automatically."
# 
# The provided feature list includes:
# - "power_on_off" feature to toggle the power state using the "press_on_off_button."
# - "sterilize_only" feature which models the sterilize-only function initiated by the "press_sterilize_only_button."
# Both features are present and accurately modelled.
#
# Sequence of features needed:
# 1. "power_on_off" to turn on the machine.
# 2. "sterilize_only" to start the sterilize-only function.

# Goal variable values:
# - Set `variable_power_on_off` to "on."
# - No variable adjustments required for `sterilize_only` since it is a single-action process.

class ExtendedSimulator(Simulator): 
    pass