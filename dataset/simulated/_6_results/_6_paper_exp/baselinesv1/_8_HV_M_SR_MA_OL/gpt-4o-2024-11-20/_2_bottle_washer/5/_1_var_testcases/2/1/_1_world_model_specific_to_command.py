# The given code correctly models the features needed to achieve the command according to the user manual.
# Steps to achieve the command:
# 1. Use the "power_on_off" feature to turn the appliance "on".
# 2. Use the "auto_mode" feature to set the auto mode to a "35-minute" cycle.

# Relevant user manual text:
# - **Power on/off**: Press this button to switch the steriliser on and off.
# - **Auto mode**: Press this button to start a drying then sterilising cycle. Press once for a 35-minute cycle.

# Corresponding feature_list names in the provided code:
# - "power_on_off"
# - "auto_mode"

# Goal variable values:
# - variable_power_on_off = "on"
# - variable_auto_mode_duration = "35 minutes"

class ExtendedSimulator(Simulator):
    pass