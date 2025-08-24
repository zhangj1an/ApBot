# The current code correctly models the relevant appliance features according to the user manual
# Sequence of features needed to achieve the user command:
# 1. "power_on_off": To turn on the appliance.
# 2. "auto_mode": To select a 35-minute auto cycle.

# Relevant user manual text:
# - For power on/off: "Press this button to switch the steriliser on and off."
# - For auto mode: "Press this button to start a drying then sterilising cycle. Press once for 35 minutes cycle, 25 minutes drying and 10 minutes sterilising."

# Relevant feature_list names in the given code:
# - "power_on_off"
# - "auto_mode"

# Goal variable values to achieve this command:
# 1. Set `variable_power_on_off` to "on".
# 2. Set `variable_auto_mode_duration` to "35 minutes".

class ExtendedSimulator(Simulator): 
    pass