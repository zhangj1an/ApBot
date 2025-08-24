# The current code already models the relevant appliance features correctly to achieve the requested command.

# Features needed to achieve the command:
# 1. "power_on_off" to turn on the steriliser.
# 2. "auto_mode" to set a 35-minute auto cycle.

# Relevant user manual text:
# - "Press this button to switch the steriliser on and off." (power_on_off feature)
# - "Press this button to start a drying then sterilising cycle. Press once for 35 minutes cycle, 25 minutes drying and 10 minutes sterilising." (auto_mode feature)

# Features in feature_list:
# - "power_on_off" corresponds to the action for turning the steriliser on.
# - "auto_mode" allows setting the auto cycle duration to 35 minutes.

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on".
# - Set variable_auto_mode_duration to "35 minutes".

class ExtendedSimulator(Simulator): 
    pass