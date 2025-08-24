# The current code correctly models the relevant appliance features and can be used to achieve the user command.

# Sequence of features needed to achieve this command:
# 1. "power_on_off" to turn on the steriliser. 
# 2. "sterilise_only_function" to sterilise the bottles for 10 minutes.

# Relevant sections from the raw user manual:
# - Power On/Off: "Press this button to switch the steriliser on and off."
# - Sterilise Only Function: "Press this button once for 10 minutes sterilisation and twice for 35 minutes sterilisation."

# Feature_list names in the given code:
# - "power_on_off"
# - "sterilise_only_function"

# Goal variable values to achieve this command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_sterilise_only_duration` to "10 minutes".

class ExtendedSimulator(Simulator): 
    pass