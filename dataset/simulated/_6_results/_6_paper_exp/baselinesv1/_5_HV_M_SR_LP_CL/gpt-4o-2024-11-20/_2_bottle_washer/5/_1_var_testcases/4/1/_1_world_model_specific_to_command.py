# The given code accurately models the relevant appliance feature that can be used to achieve the user command:
# "Start the washer, set sterilization for 35 minutes, and enable storage mode."

# Sequence of features needed to achieve this command:
# 1. "power_on_off" feature to toggle the power state to "on".
#    User manual text: "Press this button to switch the steriliser on and off."
#    Corresponding feature_list name: "power_on_off"
#
# 2. "sterilise_only_function" feature to set sterilization to 35 minutes.
#    User manual text: "Press this button once for 10 minutes sterilisation and twice for 35 minutes sterilisation."
#    Corresponding feature_list name: "sterilise_only_function"
#
# 3. "storage_function" feature to enable storage mode.
#    User manual text: "Press this button alongside any of the functions above to allow items to be stored in the steriliser. The steriliser will run a programme that emits 5 minutes of UV light and 5 minutes of drying every 2 hours, to ensure items inside remain sterile."
#    Corresponding feature_list name: "storage_function"

# The goal variable values to achieve this command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_sterilise_only_duration` to "35 minutes".
# - Set `variable_storage_mode` to "on".

class ExtendedSimulator(Simulator): 
    pass