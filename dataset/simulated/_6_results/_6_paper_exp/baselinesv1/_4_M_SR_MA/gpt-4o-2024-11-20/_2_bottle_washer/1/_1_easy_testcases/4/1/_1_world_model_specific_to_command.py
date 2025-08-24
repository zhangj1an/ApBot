# User manual excerpt: 
# 1. "Press the On/Off (power symbol) button once and the function icons will light up. If there is no selection of function after pressing on/off button, the appliance will automatically switch off."
# 2. "Sterilize only function: Press the Sterilize Only button one time to initiate sterilization."

# The sequence of features required to achieve the command "Turn on the machine and start the sterilize-only function" is:
# 1. Use the "activate_sterilizer" feature to turn on the machine.
# 2. Use the "sterilize_only" feature to start the sterilize-only function.

# Relevant feature list:
# Feature name in current code: 
# 1. "activate_sterilizer": Handles the On/Off button to turn on the machine (variable: variable_power_on_off).
# 2. "sterilize_only": Initiates sterilization after selecting Sterilize Only functionality.

# Goal variable values:
# - Set variable_power_on_off to "on".
# - No additional variables need adjustment in "sterilize_only".

class ExtendedSimulator(Simulator): 
    pass