# User manual: Press this button to switch the steriliser on and off.
# User manual: Press this button once for 10 minutes sterilisation and twice for 35 minutes sterilisation.
# User manual: Press this button alongside any of the functions above to allow items to be stored in the steriliser. 
# The steriliser will run a programme that emits 5 minutes of UV light and 5 minutes of drying every 2 hours, 
# to ensure items inside remain sterile.

# The sequence of features needed to achieve the command is as follows:
# 1. Activate the power: Use the feature "power_on_off" to turn the steriliser on.
# 2. Execute a short sterilisation cycle: Use the feature "sterilise_only_function" to set the duration to 10 minutes.
# 3. Enable storage mode: Use the feature "storage_function" to turn the storage mode on.

# The relevant feature list names in the given code are:
# - Feature: "power_on_off" for turning the steriliser on.
# - Feature: "sterilise_only_function" for setting a sterilisation duration.
# - Feature: "storage_function" for enabling storage mode.

# The raw user manual text describing these features has been quoted above.

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on" (use feature "power_on_off").
# - Set variable_sterilise_only_duration to "10 minutes" (use feature "sterilise_only_function").
# - Set variable_storage_mode to "on" (use feature "storage_function").

class ExtendedSimulator(Simulator): 
	pass