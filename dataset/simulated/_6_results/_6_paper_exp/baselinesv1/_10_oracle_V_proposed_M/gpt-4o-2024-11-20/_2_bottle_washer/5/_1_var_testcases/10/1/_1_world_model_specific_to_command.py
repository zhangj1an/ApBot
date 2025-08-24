# The given code accurately models the relevant appliance features to achieve the user command.

# Sequence of features needed:
# 1. "drying_only": Set the drying time to 30 minutes.
# 2. "storage_mode": Enable the storage mode.

# Relevant text from the user manual:
# **Drying only function**
# Press this button once for 30 minutes drying, twice for 40 minutes drying and three times for 50 minutes drying.

# **Storage function**
# Press this button alongside any of the functions above to allow items to be stored in the steriliser. The steriliser will run a programme that emits 5 minutes of UV light and 5 minutes of drying every 2 hours, to ensure items inside remain sterile.

# Feature list names in the given code:
# 1. "drying_only"
# 2. "storage_mode"

# Goal variable values to achieve this command:
# 1. Set `variable_drying_only_time` to "30_minutes".
# 2. Set `variable_storage_mode` to "on".

class ExtendedSimulator(Simulator): 
    pass