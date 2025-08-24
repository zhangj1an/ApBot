# The current code accurately models the relevant features of the appliance, enabling the execution of the user command:
# "Power up the washer and dry the bottles for 40 minutes." 

# Relevant features:
# 1. "power_on_off" feature: Toggles the appliance's power state (variable_power_on_off).
#    User manual excerpt: "Press this button to switch the steriliser on and off."
#    Feature name in code: `power_on_off`
# 
# 2. "drying_only_function" feature: Adjusts the drying duration.
#    User manual excerpt: "Press this button once for 30 minutes drying, twice for 40 minutes drying and three times for 50 minutes drying."
#    Feature name in code: `drying_only_function`

# To execute the command, follow this sequence:
# Step 1: Use the "power_on_off" feature to turn on the appliance (variable_power_on_off = "on").
# Step 2: Use the "drying_only_function" feature to set the drying time to 40 minutes (variable_drying_only_duration = "40 minutes").

# Goal variable values:
# variable_power_on_off = "on"
# variable_drying_only_duration = "40 minutes"

class ExtendedSimulator(Simulator): 
    pass