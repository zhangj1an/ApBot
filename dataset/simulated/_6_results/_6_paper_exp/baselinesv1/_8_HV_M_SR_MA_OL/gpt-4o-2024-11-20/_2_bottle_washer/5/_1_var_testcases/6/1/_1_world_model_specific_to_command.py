# User command: Activate the washer and dry items for 50 minutes, then ensure they stay sterile with storage mode.

# The current code accurately models the relevant appliance features as described in the user manual. Below, we list the sequence of features needed to achieve this command.

# **Sequence of Features**
# 1. Activate the washer by toggling the power state from "off" to "on".
#    - Feature: `power_on_off`
#    - User manual text: "Press this button to switch the steriliser on and off."
#    - Feature list: `power_on_off`
#
# 2. Adjust the drying only duration to 50 minutes.
#    - Feature: `drying_only_function`
#    - User manual text: "Press this button once for 30 minutes drying, twice for 40 minutes drying and three times for 50 minutes drying."
#    - Feature list: `drying_only_function`
#
# 3. Turn on storage mode.
#    - Feature: `storage_function`
#    - User manual text: "Press this button alongside any of the functions above to allow items to be stored in the steriliser. The steriliser will run a programme that emits 5 minutes of UV light and 5 minutes of drying every 2 hours, to ensure items inside remain sterile."
#    - Feature list: `storage_function`

# **Goal Variable Values**
# - `variable_power_on_off` = "on"
# - `variable_drying_only_duration` = "50 minutes"
# - `variable_storage_mode` = "on"

class ExtendedSimulator(Simulator): 
    pass