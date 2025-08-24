# The given code accurately models the appliance feature as per the user manual. 
# Following the user manual description, here's the sequence of features and actions needed to achieve the user command:

# Sequence of Features:
# 1. "power_on_off" to turn on the steriliser.
# 2. "sterilise_only" to perform a short sterilisation cycle for 10 minutes.
# 3. "storage_mode" to set it to storage mode.

# Corresponding feature_list names in the given code:
# - "power_on_off"
# - "sterilise_only"
# - "storage_mode"

# User Manual Raw Text Quoted:
# 1. "Press this button to switch the steriliser on and off."
# 2. "Press this button once for 10 minutes sterilisation and twice for 35 minutes sterilisation."
# 3. "Press this button alongside any of the functions above to allow items to be stored in the steriliser. The steriliser will run a programme that emits 5 minutes of UV light and 5 minutes of drying every 2 hours, to ensure items inside remain sterile."

# Goal Variable Values:
# - variable_power_on_off = "on"
# - variable_sterilise_only_time = "10_minutes"
# - variable_storage_mode = "on"

class ExtendedSimulator(Simulator): 
    pass