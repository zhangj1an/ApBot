# The given code correctly models the relevant appliance features described in the user manual to achieve the command.
# Below is the sequence of features, the relevant raw user manual text, and the feature names required:

# Sequence of features:
# 1. "power_on_off" - Turn on the appliance (variable_power_on_off to "on").
#    Raw user manual text: "Press this button to switch the steriliser on and off."
#    Feature name: "power_on_off"
# 2. "auto_mode" - Start a 60-minute auto cycle (variable_auto_mode_duration to "60 minutes").
#    Raw user manual text: "Press this button to start a drying then sterilising cycle. Press twice for 60 minutes cycle, 25 minutes drying and 35 minutes sterilising."
#    Feature name: "auto_mode"
# 3. "storage_function" - Activate storage mode (variable_storage_mode to "on").
#    Raw user manual text: "Press this button alongside any of the functions above to allow items to be stored in the steriliser."
#    Feature name: "storage_function"

# Goal variable values:
# 1. variable_power_on_off = "on"
# 2. variable_auto_mode_duration = "60 minutes"
# 3. variable_storage_mode = "on"

class ExtendedSimulator(Simulator): 
    pass