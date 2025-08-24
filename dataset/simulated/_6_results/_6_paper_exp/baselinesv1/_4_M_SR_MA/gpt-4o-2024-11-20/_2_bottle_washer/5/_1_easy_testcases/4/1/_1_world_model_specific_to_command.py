# User command: Start the washer, set sterilization for 35 minutes, and enable storage mode. 
# 
# Features to achieve the command:
# 1. "power_on_off" -> to turn on the washer. 
# Raw text from user manual: "Press this button to switch the steriliser on and off."
# Feature list: "power_on_off"
#
# 2. "sterilise_only_function" -> to set sterilization for 35 minutes.
# Raw text from user manual: "Press this button once for 10 minutes sterilisation and twice for 35 minutes sterilisation."
# Feature list: "sterilise_only_function"
#
# 3. "storage_function" -> to enable storage mode.
# Raw text from user manual: "Press this button alongside any of the functions above to allow items to be stored in the steriliser. ..."
# Feature list: "storage_function"
#
# Goal Variable Values:
# Set `variable_power_on_off` to "on".
# Set `variable_sterilise_only_duration` to "35 minutes".
# Set `variable_storage_mode` to "on".

class ExtendedSimulator(Simulator): 
    pass