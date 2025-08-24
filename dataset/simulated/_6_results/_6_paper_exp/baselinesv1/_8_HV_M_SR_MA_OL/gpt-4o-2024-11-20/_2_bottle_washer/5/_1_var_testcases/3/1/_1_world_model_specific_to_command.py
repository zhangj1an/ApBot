# According to the user manual, the current code correctly models the appliance's features needed to achieve the user command.
# Sequence of features needed to achieve the command:
# 1. Feature: "power_on_off" - Turn the steriliser power on.
#    - Relevant user manual text: "Press this button to switch the steriliser on and off."
#    - Feature list name: "power_on_off"
# 2. Feature: "drying_only_function" - Set the drying function to 40 minutes.
#    - Relevant user manual text: "Press this button once for 30 minutes drying, twice for 40 minutes drying and three times for 50 minutes drying."
#    - Feature list name: "drying_only_function"

# Goal variable values:
# - variable_power_on_off set to "on"
# - variable_drying_only_duration set to "40 minutes"

class ExtendedSimulator(Simulator): 
    pass