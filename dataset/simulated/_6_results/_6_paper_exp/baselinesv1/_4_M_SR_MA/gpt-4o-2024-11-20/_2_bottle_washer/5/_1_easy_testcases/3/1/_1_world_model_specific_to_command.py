# The current code accurately models the appliance features described in the user manual for the requested user command.

# Sequence of features needed to achieve the command:
# 1. Feature: "power_on_off" - Turn on the appliance.
#    - User manual text: "Press this button to switch the steriliser on and off."
#    - Relevant feature_list name in the code: "power_on_off"
#    - Goal variable value: variable_power_on_off = "on"
# 2. Feature: "drying_only_function" - Set the drying-only duration to 40 minutes.
#    - User manual text: "Press this button once for 30 minutes drying, twice for 40 minutes drying and three times for 50 minutes drying."
#    - Relevant feature_list name in the code: "drying_only_function"
#    - Goal variable value: variable_drying_only_duration = "40 minutes"

# Generate the goal variable values:
class ExtendedSimulator(Simulator): 
    pass